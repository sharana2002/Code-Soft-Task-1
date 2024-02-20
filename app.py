from flask import Flask, render_template, request

app = Flask(__name__)

# Define a dictionary of predefined responses
RESPONSES = {
    "hello": "Hello! How can I help you?",
    "how are you": "I'm just a computer program, but I'm functioning as intended. How can I assist you?",
    "bye": "Goodbye! Have a grpythoeat day!",
    "who is the prime minister of india": "Narendra Modi",
    "what is your name?": "I am a chatbot designed to assist you.",
    "what can you do?": "I can answer questions, provide information, and have conversations with you.",
    "thank you": "You're welcome!",
    "how old are you?": "I am just a program, so I don't have an age.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is the meaning of life?": "That's a philosophical question! Many people have different answers."
}

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form["msg"]
    # Check if user input matches predefined responses
    if user_input.lower() in RESPONSES:
        return RESPONSES[user_input.lower()]
    else:
        return "I'm sorry, I don't understand."

if __name__ == '__main__':
    app.run(debug=True)
