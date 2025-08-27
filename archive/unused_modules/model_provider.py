from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Gemini API key from the environment
# gemini_api_key = os.getenv("GOOGLE_API_KEY ")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", 
                            #    api_key=gemini_api_key
                            )
