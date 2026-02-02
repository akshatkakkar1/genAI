
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Gemini LLM
llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
  
)

# Example usage
response = llm.invoke("What is the capital of india?")
print(response)