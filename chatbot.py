import streamlit as st
import random

def simple_chatbot():
    st.title("Creative Chatbot")
    st.write("Ask me anything! I'm here to chat 😄")

    # Store user input
    user_input = st.text_input("You:")

    # Define a list of fun and creative responses
    responses = {
        "hello": ["Hi there! How can I assist you today?", "Hey! What's up?", "Hello! How are you today?"],
        "how are you": ["I'm just a bot, but I'm doing great! Thanks for asking!", "I'm functioning optimally! 😁", "Doing well, ready to help you!"],
        "bye": ["Goodbye! Have an amazing day ahead! 🌞", "Catch you later! 👋", "See you soon! Take care!"],
        "tell me a joke": [
            "Why don't skeletons fight each other? They don't have the guts! 😆", 
            "Why did the computer go to the doctor? Because it had a virus! 🤒", 
            "What do you get when you cross a snowman and a vampire? Frostbite! 🧛‍♂️❄️"
        ],
        "what is your name": ["I am Chatbot, your friendly assistant!", "Call me Chatbot! What's your name?", "I'm Chatbot, ready to chat! 😊"],
        "what can you do": ["I can chat, tell jokes, answer questions, and much more!", "I can help you with anything! Try asking me something fun.", "I can assist with answering queries or just talk with you! 😊"],
        "how old are you": ["I don't age, I'm eternal! 😄", "I was created just recently, but I don't keep track of time."],
        "what is love": ["Love is when you care about someone or something deeply. ❤️", "Love is a complex emotion. It's about connection and care."],
        "who are you": ["I am a chatbot, created to help and entertain you!", "I’m a friendly AI, ready to assist you with anything! 😎"],
        "thank you": ["You're welcome! 😄", "No problem, happy to help!", "Anytime! Let me know if you need anything else!"],
        "good morning": ["Good morning! Hope you have a wonderful day!", "Good morning! 🌅 Ready to start your day with some fun?"],
        "good night": ["Good night! Sweet dreams! 🌙", "Sleep well! Catch you later! 😴"],
    }

    # A fallback response if the input is not recognized
    def get_fallback_response():
        return random.choice([
            "I'm not sure how to respond to that. Can you rephrase?",
            "Oops! I didn't quite get that. Try asking something else!",
            "Hmmm... that’s a tricky one. Could you ask something else?"
        ])

    # Get the response based on user input, or fallback if not found
    if user_input:
        user_input = user_input.lower()  # Normalize to lowercase
        if user_input in responses:
            reply = random.choice(responses[user_input])  # Randomize responses for the same input
        else:
            reply = get_fallback_response()

        # Display the chatbot's reply in a text area
        st.text_area("Bot:", value=reply, height=100)

        # Optional: Display a different style for bot messages (colorful background)
        st.markdown("""
            <style>
                .css-1v3fvcr {
                    background-color: #f1f1f1; /* Light gray background */
                    padding: 10px;
                    border-radius: 10px;
                    border: 1px solid #ddd;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    font-family: 'Arial', sans-serif;
                }
                .css-1v3fvcr p {
                    color: #333;
                    font-size: 16px;
                }
            </style>
        """, unsafe_allow_html=True)
        
        # Adding some encouragement for users
        st.markdown("<br><br><p style='font-size:16px; color: #808080;'>Type something to chat with me!</p>", unsafe_allow_html=True)
