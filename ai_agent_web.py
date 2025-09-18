import requests
from bs4 import BeautifulSoup
import ollama

# Step 1: Fetch a webpage
url = "https://www.tcs.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract text from paragraphs
text = " ".join([p.get_text() for p in soup.find_all("p")[:5]])

# Step 2: Send to LLaMA
response = ollama.chat(model="llama3", messages=[{"role": "user", "content": f"Summarize this: {text}"}])

print("AI Summary:\n", response['message']['content'])
