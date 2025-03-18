
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Set API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBWAhYYQ4n89Qgu2N0ae6g-mpDIlbIRiuk"

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Generate Response
response = llm.invoke([HumanMessage(content="What is LangChain?")])
print(response.content)
