import os
import shutil
from typing import TypedDict, List, Any
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph.graph import StateGraph, END
from dotenv import find_dotenv, load_dotenv

# Load environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
API_KEY = os.getenv("GOOGLE_API_KEY")

# Validate API key
if not API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found in environment variables")

# Set API Key
os.environ["GOOGLE_API_KEY"] = API_KEY

# Configure Gemini components
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    client_options={"api_endpoint": "generativelanguage.googleapis.com"}
)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Define RAG state
class RAGState(TypedDict):
    messages: List[Any]
    retrieved_documents: List[str]

# Enhanced retrieval function
def retrieve_documents(state: RAGState) -> RAGState:
    """Retrieve documents with score filtering and logging."""
    try:
        last_message = state["messages"][-1]

        if isinstance(last_message, HumanMessage):
            query = last_message.content
            db = Chroma(
                persist_directory="./chroma_db",
                embedding_function=embeddings
            )

            # Get documents with scores and metadata
            docs = db.similarity_search_with_relevance_scores(query, k=5)

            # Filter and format results
            filtered_docs = []
            for doc, score in docs:
                if score > 0.5:  # Increase threshold for better quality
                    filtered_docs.append({
                        "content": doc.page_content,
                        "metadata": doc.metadata,
                        "score": score
                    })

            # Store in state and log
            state["retrieved_documents"] = filtered_docs
            print(f"\n🔍 Retrieved {len(filtered_docs)} documents for: '{query}'")

    except Exception as e:
        print(f"\n⚠️ Retrieval error: {str(e)}")
        state["retrieved_documents"] = []

    return state

# Modified response generation function
def generate_response(state: RAGState) -> RAGState:
    """Generate response using retrieved context."""
    try:
        if not state["retrieved_documents"]:
            state["messages"].append(AIMessage(
                content="I couldn't find relevant information to answer your question."
            ))
            return state

        context = "\n".join(
            [f"Document {i+1} (Confidence: {doc['score']*100:.1f}%): {doc['content']}"
             for i, doc in enumerate(state["retrieved_documents"])]
        )

        prompt = f"""You're a professional research assistant. Analyze this context and answer the question:

        Context:
        {context}

        Question: {state["messages"][-1].content}

        Requirements:
        1. Provide a complete, natural-sounding sentence
        2. Mention the confidence level
        3. Explain the context source
        4. Keep response under 2 sentences"""
        response = llm.invoke([
            HumanMessage(content=prompt)
        ])

        # After generating response
        if any(word in response.content.lower() for word in ["exact text", "verbatim"]):
            response.content = "The document contains information about Anjan's professional role."

        state["messages"].append(response)

    except Exception as e:
        state["messages"].append(AIMessage(
            content="Sorry, I encountered an error processing your request."
        ))

    return state

# Modified document processing pipeline
def process_documents(directory_path: str):
    """Process all text files in a directory with enhanced validation."""
    try:
        # Clean existing database
        if os.path.exists("./chroma_db"):
            shutil.rmtree("./chroma_db")

        all_chunks = []
        processed_files = 0
        sources = []

        # Process all files in directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Skip directories and non-text files
            if not os.path.isfile(file_path):
                continue
            if not filename.lower().endswith(('.txt', '.md', '.csv')):
                continue

            try:
                with open(file_path, "r", encoding='utf-8') as f:
                    content = f.read().strip()
                    if not content:
                        print(f"\n⚠️ Empty file skipped: {filename}")
                        continue

                    print(f"\n📄 Processing {filename}:")
                    print(content[:500] + "..." if len(content) > 500 else content)

                    # Split document with improved configuration
                    splitter = RecursiveCharacterTextSplitter(
                        chunk_size=300,
                        chunk_overlap=50,
                        separators=["\n\n", "\n", " ", ""],
                        length_function=len,
                        keep_separator=False
                    )
                    chunks = splitter.split_text(content)

                    if not chunks:
                        print(f"\n⚠️ No chunks generated for: {filename}")
                        continue

                    all_chunks.extend(chunks)
                    sources.extend([filename] * len(chunks))
                    processed_files += 1

            except Exception as e:
                print(f"\n⚠️ Error processing {filename}: {str(e)}")
                continue

        if not all_chunks:
            raise ValueError("No valid chunks generated from any files")

        print(f"\n✂️ Total chunks from {processed_files} files: {len(all_chunks)}")

        # Create vector store with metadata
        Chroma.from_texts(
            texts=all_chunks,
            embedding=embeddings,
            persist_directory="./chroma_db",
            metadatas=[{"source": source} for source in sources]
        )
        print("\n✅ Vector store created successfully from all documents")

    except Exception as e:
        print(f"\n❌ Document processing failed: {str(e)}")
        raise

# Workflow setup
def create_workflow():
    """Configure the RAG workflow."""
    workflow = StateGraph(RAGState)
    workflow.add_node("retrieve", retrieve_documents)
    workflow.add_node("generate", generate_response)

    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()

# Main execution
if __name__ == "__main__":
    try:
        # Process all documents in Downloads folder
        downloads_path = os.path.expanduser("~/Downloads/RAG_TEST")
        process_documents(downloads_path)

        # Initialize workflow
        rag_chain = create_workflow()

        # Test query
        test_query = "explain artificial intelligence"
        result = rag_chain.invoke({
            "messages": [HumanMessage(content=test_query)],
            "retrieved_documents": []
        })

        # Display results
        print("\n📝 Final Results:")
        print(f"\n🔎 Query: {test_query}")
        print(f"\n📚 Retrieved Documents ({len(result['retrieved_documents'])}):")
        for doc in result["retrieved_documents"]:
            print(f"\n⭐ Score: {doc['score']:.2f}")
            print(f"📄 Content: {doc['content'][:100]}...")

        print(f"\n💬 Response:\n{result['messages'][-1].content}")

    except Exception as e:
        print(f"\n❌ Main execution failed: {str(e)}")