import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)


def ask_ollama(prompt: str) -> str:
    """
    Ask the local Ollama model (LLaMA3) for a response.
    Make sure Ollama is running: `ollama run llama3`
    """
    url = "http://localhost:11434/api/generate"
    payload = {"model": "llama3", "prompt": prompt}
    response = requests.post(url, json=payload, stream=True)

    result = ""
    for line in response.iter_lines():
        if line:
            data = line.decode("utf-8")
            if "response" in data:
                # Extract the text part
                try:
                    result += eval(data).get("response", "")
                except:
                    pass
    return result.strip()


def ask_openai(prompt: str) -> str:
    """
    Ask OpenAI's GPT model using API key.
    """
    response = openai_client.chat.completions.create(
        model="gpt-4.1-mini",   # can change to gpt-4.1 or gpt-4o
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content.strip()


def chatbot():
    print("🤖 Hybrid Chatbot (Ollama + OpenAI)")
    print("Type 'exit' to quit.\n")

    engine = input("Choose engine (ollama/openai): ").strip().lower()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        if engine == "ollama":
            reply = ask_ollama(user_input)
        elif engine == "openai":
            reply = ask_openai(user_input)
        else:
            reply = "❌ Invalid engine selected. Please restart."

        print(f"AI: {reply}\n")


if __name__ == "__main__":
    chatbot()
