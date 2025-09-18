import PyPDF2
import ollama

# Step 1: Read PDF
pdf_reader = PyPDF2.PdfReader("sample.pdf")
text = ""
for page in pdf_reader.pages:
    text += page.extract_text()

# Step 2: Send to LLaMA
response = ollama.chat(model="llama3", messages=[{"role": "user", "content": f"Summarize this PDF: {text}"}])

print("AI PDF Summary:\n", response['message']['content'])