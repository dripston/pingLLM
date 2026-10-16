import dotenv
import httpx
import os
from dotenv import load_dotenv
import argparse

load_dotenv()

api_key=os.getenv("GROQ_API_KEY")

if not api_key:
    print("error: api key is missing ,please set an api key in the .env")
    raise SystemError(1)
else:
    print("api key loaded")


parser=argparse.ArgumentParser(description="ask athe llm from your terminal")
parser.add_argument("question",help="the question to ask the llm")
parser.add_argument("--temp",type=float,default=0.2,help="controls randomness in the llm response")
parser.add_argument("--model",type=str,default="openai/gpt-oss-20b",help="controls the model")
args=parser.parse_args()
print(args.question)
url="https://api.groq.com/openai/v1/chat/completions"

headers={
    "authorization":f"Bearer {api_key}",
    "content-type":"application/json"
}

payload={
    "model":args.model,
    "messages": [
        {"role":"user","content":args.question}],
        "temperature":args.temp
}
response=httpx.post(
    url,
    headers=headers,
    json=payload,
    timeout=30.0
)

print("status ",response.status_code)
data = response.json()
answer = data["choices"][0]["message"]["content"]
print(answer)
