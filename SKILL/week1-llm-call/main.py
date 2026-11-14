import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from the .env file
load_dotenv()

# Read the OpenRouter API key securely
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY was not found. Check your .env file.")

# Initialize the OpenAI client with OpenRouter's base URL
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Send a prompt to a model on OpenRouter
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {"role": "user", "content": "What is Artificial Intelligence? Explain in simple words."}
    ]
)

# Display the generated answer
print("\nLLM Response:")
print(response.choices[0].message.content)