# import google.generativeai as genai

# # Configure the API key
# genai.configure(api_key="AIzaSyBWAhYYQ4n89Qgu2N0ae6g-mpDIlbIRiuk")  # Replace with your key

# try:
#     # Method 1: Try the latest model naming convention
#     model = genai.GenerativeModel('gemini-1.5-pro')
    
#     # Function to generate responses
#     def generate_response(prompt):
#         response = model.generate_content(prompt)
#         return response.text

#     # Test the model
#     if __name__ == "__main__":
#         test_prompt = "Explain LangChain in simple terms."
#         response = generate_response(test_prompt)
#         print("Prompt:", test_prompt)
#         print("Response:", response)
        
# except Exception as e:
#     print(f"Error with first attempt: {e}")
#     print("\nTrying alternative approach...")
    
#     # Method 2: List available models and use one that's available
#     try:
#         available_models = genai.list_models()
#         print("Available models:")
#         for model_info in available_models:
#             print(f" - {model_info.name}")
        
#         # Try to find a Gemini model in the list
#         gemini_models = [m for m in available_models if "gemini" in m.name.lower()]
#         if gemini_models:
#             recommended_model = gemini_models[0].name
#             print(f"\nTrying with recommended model: {recommended_model}")
            
#             model = genai.GenerativeModel(recommended_model)
#             test_prompt = "Explain quantum computing in simple terms."
#             response = model.generate_content(test_prompt)
#             print("Response:", response.text)
#         else:
#             print("No Gemini models found in the available models list.")
#     except Exception as e2:
#         print(f"Error with second attempt: {e2}")
#         print("\nPlease check the Google AI documentation for the latest model names and API usage.")
        

# import os
# from dotenv import find_dotenv, load_dotenv

# dotenv_path = find_dotenv()

# load_dotenv(dotenv_path)

# API_KEY = os.getenv("GOOGLE_API_KEY")
        
# import google.generativeai as genai

# genai.configure(api_key=API_KEY)

# llm = genai.GenerativeModel("gemini-2.0-flash") 
# #gemini-2.0-flash
# response = llm.generate_content("What are AI agents?")
# print(response.text)        



# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import HumanMessage

# # Set API Key
# os.environ["GOOGLE_API_KEY"] = "AIzaSyBWAhYYQ4n89Qgu2N0ae6g-mpDIlbIRiuk"

# # Initialize LLM
# llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# # Generate Response
# response = llm.invoke([HumanMessage(content="What is LangChain?")])
# print(response.content)

