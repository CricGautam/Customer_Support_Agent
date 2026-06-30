from openai import OpenAI
from dotenv import load_dotenv
import os

print("Program started")

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)
while True:
    question=input("You: ")
    if question=="exit":
        break
    else:

        response = client.chat.completions.create(
    model="cohere/north-mini-code-20260617:free",
    max_tokens=300,
    messages=[
        {
            "role":"user",
         "content": question
         }
    ]
)
        print(response.choices[0].message.content)








