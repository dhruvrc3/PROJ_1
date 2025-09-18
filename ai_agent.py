print("🚀 AI Agent script started")
import ollama
import pytesseract
from PIL import Image


# 1. OCR Function (read text from an image)
def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

# 2. Ask LLM Function (send question to LLaMA3)
def ask_llm(prompt):
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

# 3. Agent: Reads image → Sends to AI → Gets result
def ai_agent(image_path, task):
    print("[*] Extracting text from image...")
    text = extract_text_from_image(image_path)

    print("[*] Sending to AI model...")
    prompt = f"The following text was extracted from an image:\n{text}\n\nTask: {task}"
    answer = ask_llm(prompt)

    return answer


# 🚀 Demo run
if __name__ == "__main__":
    # Replace with an image path that has text
    result = ai_agent("sample.png", "Summarize the content in 3 bullet points.")
    print("\nAI Agent Result:\n", result)
