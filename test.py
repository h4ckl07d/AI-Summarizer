import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Loaded key:", api_key)
print("Length:", len(api_key) if api_key else 0)

genai.configure(api_key="YOUR_KEY")

model = genai.GenerativeModel("gemini-2.0-flash-lite")

response = model.generate_content(
    "Explain blockchain in one sentence."
)

print(response.text)
print(api_key[:6])