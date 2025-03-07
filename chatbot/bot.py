import requests

def chatbot():
    print("Chatbot is running! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        response = requests.post("http://127.0.0.1:8000/analyze", json={"message": user_input})
        data = response.json()
        
        print(f"Bot: Intent - {data['intent']}, Sentiment - {data['sentiment']}")

if __name__ == "__main__":
    chatbot()
