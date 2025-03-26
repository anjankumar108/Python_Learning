import os
import shutil
from typing import TypedDict, List, Any
from pathlib import Path
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
from dotenv import find_dotenv, load_dotenv
import streamlit as st

# Load environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found in environment variables")

os.environ["GOOGLE_API_KEY"] = API_KEY

# Configure Gemini components
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    client_options={"api_endpoint": "generativelanguage.googleapis.com"}
)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class RAGState(TypedDict):
    messages: List[Any]
    retrieved_documents: List[str]
    conversation_context: List[str]  # Track key discussion points

def retrieve_documents(state: RAGState) -> RAGState:
    last_message = state["messages"][-1]
    if isinstance(last_message, HumanMessage):
        query = last_message.content

        db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
        docs = db.similarity_search_with_relevance_scores(query, k=5)

        filtered_docs = []
        for doc, score in docs:
            if score > 0.5:
                filtered_docs.append({
                    "content": doc.page_content,
                    "metadata": doc.metadata,
                    "score": score
                })

        state["retrieved_documents"] = filtered_docs
    else:
        state["retrieved_documents"] = []

    return state

def extract_entities(text: str) -> List[str]:
    """Improved entity extraction with multi-word name support"""
    entities = []
    words = text.replace("?", " ").split()
    i = 0
    while i < len(words):
        if words[i].istitle():
            entity = [words[i]]
            j = i + 1
            while j < len(words) and (words[j].istitle() or words[j] in ["II", "III", "Jr.", "Sr."]):
                entity.append(words[j])
                j += 1
            entities.append(" ".join(entity))
            i = j
        else:
            i += 1
    return list(set(entities))

def extract_main_entity(conversation: str) -> str:
    """Enhanced entity scoring with relationship awareness"""
    entities = extract_entities(conversation)
    if not entities:
        return ""

    # Score entities with recency and relationship boosts
    entity_scores = {}
    reversed_entities = list(reversed(entities))

    for i, entity in enumerate(reversed_entities):
        score = (len(reversed_entities) - i) * 2  # Recency boost
        if any(keyword in conversation.lower() for keyword in ["husband", "wife", "father", "mother"]):
            if "'s" in entity:  # Relationship entity
                score += 5
        entity_scores[entity] = entity_scores.get(entity, 0) + score

    return max(entity_scores, key=entity_scores.get, default="")

def generate_response(state: RAGState) -> RAGState:
    # Get enhanced conversation context
    conversation_context = "\n".join(
        [f"{msg.content}" for msg in state["messages"][-4:]]
    )
    main_entity = extract_main_entity(conversation_context)

    if state["retrieved_documents"]:
        context = "\n".join(
            [f"Document {i+1}: {doc['content']}"
             for i, doc in enumerate(state["retrieved_documents"])]
        )
        prompt = f"""Analyze this conversation and documents to answer the question.

        Conversation History:
        {conversation_context}

        Relevant Documents:
        {context}

        Current Question: {state["messages"][-1].content}

        Rules:
        1. Resolve pronouns using: {main_entity or 'no specific entity'}
        2. For family relations, assume reference to {main_entity}
        3. If unsure, state assumption clearly
        4. Keep answers concise and based on the provided documents.
        """
    else:
        prompt = f"""Continue this conversation:

        Conversation History:
        {conversation_context}

        Current Question: {state["messages"][-1].content}

        Rules:
        1. Assume 'her/him' refers to {main_entity or 'most recent person'}
        2. For family questions, default to {main_entity}
        3. Keep answers under 2 sentences"""

    try:
        response = llm.invoke([HumanMessage(content=prompt)])

        # Force entity inclusion for pronouns
        if main_entity:
            response.content = response.content.replace(" her ", f" {main_entity}'s ")
            response.content = response.content.replace(" his ", f" {main_entity}'s ")
            if "which specific" in response.content.lower():
                response.content = f"{main_entity}'s {response.content.split(':')[-1].strip()}"

        state["messages"].append(response)

    except Exception as e:
        state["messages"].append(AIMessage(content="Sorry, I encountered an error processing your request."))

    return state

def process_documents(directory_path: str):
    try:
        if os.path.exists("./chroma_db"):
            shutil.rmtree("./chroma_db")

        all_chunks = []
        sources = []

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=["\n\n", "\n", " ", ""],
            length_function=len,
            keep_separator=False
        )

        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if not os.path.isfile(file_path) or not filename.lower().endswith(('.txt', '.md', '.csv')):
                continue

            try:
                with open(file_path, "r", encoding='utf-8') as f:
                    content = f.read().strip()
                    if not content:
                        continue

                    chunks = splitter.split_text(content)
                    all_chunks.extend(chunks)
                    sources.extend([filename] * len(chunks))

            except Exception as e:
                st.warning(f"Error processing {filename}: {str(e)}")
                continue

        if all_chunks:
            Chroma.from_texts(
                texts=all_chunks,
                embedding=embeddings,
                persist_directory="./chroma_db",
                metadatas=[{"source": source} for source in sources]
            )

    except Exception as e:
        st.error(f"Document processing failed: {str(e)}")
        raise

def create_workflow():
    workflow = StateGraph(RAGState)
    workflow.add_node("retrieve", retrieve_documents)
    workflow.add_node("generate", generate_response)
    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)
    return workflow.compile()

# Streamlit UI
def main():
    st.set_page_config(page_title="Document Chat", layout="wide")

    with st.sidebar:
        st.header("Settings")
        docs_path = st.text_input("Documents Path", str(Path.home() / "Downloads/RAG_TEST"))

        if st.button("Process Documents"):
            with st.spinner("Processing documents..."):
                process_documents(docs_path)
                st.success("Documents processed successfully!")

        # Add Clear Chat button
        if st.button("Clear Chat History"):
             st.session_state.messages = [] 
             st.session_state.retrieved_documents = []
             st.success("Chat history cleared!")

    st.title("Document Chat Assistant")
    st.markdown("Ask questions about your processed documents")

    if "rag_chain" not in st.session_state:
        st.session_state.rag_chain = create_workflow()
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "retrieved_documents" not in st.session_state:
        st.session_state.retrieved_documents = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Type your question here"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Searching documents..."):
            result = st.session_state.rag_chain.invoke({
                "messages": [HumanMessage(content=prompt)],
                "retrieved_documents": [],
                "conversation_context": []
            })

        response = result["messages"][-1].content
        with st.chat_message("assistant"):
            st.markdown(response)

            # Show source documents if available
            if result["retrieved_documents"]:
                with st.expander("View Source Documents"):
                    for doc in result["retrieved_documents"]:
                        st.markdown(f"**Source:** `{doc['metadata']['source']}`")
                        st.markdown(f"**Confidence:** {doc['score']:.2f}")
                        st.text(doc["content"][:200] + "...")
            else:
                st.caption("ℹ️ Answer generated using general knowledge")

        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()