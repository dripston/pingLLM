import dotenv
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("GROQ_API_KEY")

if not api_key:
    print("error: api key is missing ,please set an api key in the .env")
    raise SystemError(1)
else:
    print("api key loaded")


url="https://api.groq.com/openai/v1/chat/completions"

headers={
    "authorization":f"Bearer {api_key}",
    "content-type":"application/json"
}

payload={
    "model":"openai/gpt-oss-20b",
    "messages": [
        {"role":"user","content":"explain recursion in one line"}],
        "temperature":0.2
}
response=httpx.post(
    url,
    headers=headers,
    json=payload,
    timeout=30.0
)

print("status ",response.status_code)
print(response.json())