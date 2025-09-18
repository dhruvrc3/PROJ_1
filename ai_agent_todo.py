import ollama
import json

email_text = """
Hi Team,
Please finish the AI Hackathon slides by Monday.
Dhruv, prepare the demo by Tuesday.
Shiv, check the dataset quality this week.
Regards,
Manager
"""

# Step 1: Ask LLaMA to extract tasks
prompt = f"Extract tasks with person and deadline from this email:\n{email_text}"

response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])

# Step 2: Print structured tasks
print("Extracted Tasks:\n", response['message']['content'])
