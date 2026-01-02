import ollama

while True:
    q = input("You: " )
    if q == "exit":
        break

    res = ollama.chat(
        model = "mistral",
        messages = [{"role":"user","content": q}]
    )
    print("Bot: ",res["message"]["content"])
