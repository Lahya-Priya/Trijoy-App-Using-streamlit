import streamlit as st

# Dynamically import modules
try:
    from tic_tac_toe import tic_tac_toe
    from chatbot import simple_chatbot
    from movie_recommender import movie_recommender
except ModuleNotFoundError as e:
    st.error(f"Module not found: {e}")
    st.stop()

def main():
    # Sidebar with Title and Icons
    st.sidebar.title("🎮 Trijoy App")
    st.sidebar.markdown("""
        Welcome to the **Trijoy App**! 🎉  
        Choose a feature to explore and enjoy! 👇
    """)
    
    choice = st.sidebar.radio(
        "Select an option", 
        ["🔲 Tic Tac Toe", "🤖 Chatbot", "🎬 Movie Recommender"]
    )

    if choice == "🔲 Tic Tac Toe":
        st.sidebar.markdown("### Let's play Tic Tac Toe! ✨")
        tic_tac_toe()
    elif choice == "🤖 Chatbot":
        st.sidebar.markdown("### Chat with your friendly bot 🤖💬")
        simple_chatbot()
    elif choice == "🎬 Movie Recommender":
        st.sidebar.markdown("### Find your next movie 🎥🍿")
        movie_recommender()

if __name__ == "__main__":
    main()
