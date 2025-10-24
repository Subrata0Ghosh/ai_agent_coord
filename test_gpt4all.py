from gpt4all import GPT4All

# Use your downloaded model path
model_path = "/home/asus/.cache/huggingface/hub/models--orel12--ggml-gpt4all-j-v1.3-groovy/snapshots/9ff9297dc2b604b9845e8c3f38ec338fa5ea8179/ggml-gpt4all-j-v1.3-groovy.bin"

# Load model
model = GPT4All(model_path)

# Simple chat test
with model.chat_session():
    response = model.generate("Hello! Explain what a matching engine does in crypto trading.", max_tokens=200)
    print("AI:", response)
