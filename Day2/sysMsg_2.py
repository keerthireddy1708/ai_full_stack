import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content":"you are teaching to the 5 year old child. "
        },
        {
            "role":"user",
            "content":"Explain ai"
        }
    ]
)
print(response["message"]["content"])