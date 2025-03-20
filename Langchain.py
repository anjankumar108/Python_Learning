
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnableBranch
from langchain_core.pydantic_v1 import BaseModel


dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

API_KEY = os.getenv("GOOGLE_API_KEY")
        
# Set API Key
os.environ["GOOGLE_API_KEY"] = API_KEY

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Generate Response
# response = llm.invoke([HumanMessage(content="What is LangChain?")])
# print(response.content)

# template = """You are an expert AI assistant.
# Question: {question}
# Answer:"""


# prompt = "Generate functional test cases for the 'Login' feature, covering valid and invalid scenarios."

# response = llm.invoke(prompt)
# print(response)

# prompt = PromptTemplate(template=template,input_variables=['question'])
# formatedPrompt = prompt.format(question="What are different ways to use prompt template")
# print(formatedPrompt)


# chain = prompt | llm
# response = chain.invoke({"question": "What is Machine Learning?"})
# print(response)

# debug_prompt = """
# Step 1: Identify common bugs in the '{feature}' module.
# Step 2: Generate test cases to detect these bugs.
# Step 3: Suggest potential fixes.

# Now, apply these steps for '{feature}'.
# """
# response=llm.invoke(debug_prompt.format(feature="Order Processing"))
# print(response.content)


# few_shot_prompt = """
# Examples:
# 1. Feature: Login | Test: Invalid Password | Expected: Error message
# 2. Feature: Cart | Test: Adding more than stock limit | Expected: Stock limit error

# Now, generate test cases for '{feature}'.
# """
# response=llm.invoke(few_shot_prompt.format(feature="Payment Gateway"))
# print(response.content)

# test_case_prompt = PromptTemplate(
#     input_variables=["feature", "test_type"],
#     template="Generate {test_type} test cases for the '{feature}' feature."
# )
# # or test_case_prompt = PromptTemplate.from_template("Generate {test_type} test cases for the '{feature}' feature.")

# filled_prompt = test_case_prompt.format(feature="Checkout", test_type="performance")
# print(filled_prompt)

# chain = test_case_prompt | llm
# response = chain.invoke({"feature": "Checkout","test_type":"performance"})
# print(response.content)


# prompt = PromptTemplate.from_template("Generate test cases for the login functionality of a web application.")
# chain = prompt | llm
# response = chain.invoke({})
# print(response)  # Generates test cases for login functionality

# prompt1 = PromptTemplate.from_template("Describe the issue: {bug_description}")
# prompt2 = PromptTemplate.from_template("Generate detailed reproduction steps for: {bug_report}")

# describe_bug_chain = prompt1 | llm
# reproduce_chain = prompt2 | llm

# seq_chain = describe_bug_chain | reproduce_chain
# response = seq_chain.invoke({"bug_description": "Login button not working on mobile view"})
# print(response)  # Generates reproduction steps for the login issue

# defect_prompt = PromptTemplate.from_template("Summarize defects from test report: {report}")
# performance_prompt = PromptTemplate.from_template("Summarize performance issues from test report: {report}")

# defect_chain = defect_prompt | llm
# performance_chain = performance_prompt | llm

# parallel_chain = RunnableParallel(defects=defect_chain, performance=performance_chain)
# response = parallel_chain.invoke({"report": "Test run identified slow response times and two UI defects."})
# print(response)  # {'defects': 'Summary of UI defects', 'performance': 'Summary of performance issues'}

# functional_test_prompt = PromptTemplate.from_template("Generate functional test cases for {feature}.")
# performance_test_prompt = PromptTemplate.from_template("Generate performance test cases for {feature}.")

# def route_func(input):
#     return "functional" if "UI" in input["feature"] else "performance"

# functional_chain = functional_test_prompt | llm
# performance_chain = performance_test_prompt | llm

# branching_chain = RunnableBranch(
#     (lambda x: "UI" in x["feature"], functional_chain),
#     performance_chain  # Default branch is now just the chain itself
# )

# response = branching_chain.invoke({"feature": "Checkout UI"})
# print(response)  # Functional test cases for checkout UI

# class BugInput(BaseModel):
#     description: str

# def classify_bug(input: BugInput):
#     if "crash" in input.description.lower():
#         return "Critical"
#     elif "slow" in input.description.lower():
#         return "Performance"
#     else:
#         return "UI/Minor"

# bug_classification_chain = RunnableLambda(classify_bug)
# response = bug_classification_chain.invoke(BugInput(description="Application crashes on clicking submit button"))
# print(response)  # "Critical"