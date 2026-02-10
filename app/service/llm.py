from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def call_llm(messages):
    prompt = "\n".join(
        f"{m['role']}: {m['content']}" for m in messages
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
