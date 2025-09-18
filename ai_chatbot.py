import ollama
import PyPDF2
import requests
from bs4 import BeautifulSoup

# Step 1: Load PDF
def load_pdf(file_path):
    pdf_reader = PyPDF2.PdfReader(file_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Step 2: Load Webpage
def load_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = " ".join([p.get_text() for p in soup.find_all("p")])
    return text

# Step 3: Ask AI
def ask_ai(content, query):
    prompt = f"""
    You are a smart assistant. Use the following content to answer questions.

    Content:
    {content[:4000]}  # limiting to ~4k characters for LLaMA input

    Question: {query}
    """
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Step 4: Example usage
if __name__ == "__main__":
    # Load from PDF
    # pdf_text = load_pdf("sample.pdf")

    # OR load from Web
    pdf_text = load_webpage("https://www.samsung.com/in/")

    # Ask chatbot
    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = ask_ai(pdf_text, query)
        print("\nAI Answer:", answer, "\n")
