import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content":" Define aI in two lines and three main types of ai .give in bullet points. "
        }
    ]
)
print(response["message"]["content"])