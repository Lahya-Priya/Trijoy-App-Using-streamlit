import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def movie_recommender():
    st.title("Movie Recommendation System")
    st.write("Enter your favorite movie to get recommendations!")

    # Expanded list of movies, descriptions, and genres
    movies = [
        "Baahubali: The Beginning",
        "Baahubali: The Conclusion",
        "RRR",
        "Eega",
        "Ala Vaikunthapurramuloo",
        "Arjun Reddy",
        "Mahanati",
        "Jersey",
        "Kshana Kshanam",
        "Pelli Sandadi",
        "Magadheera",
        "Rangasthalam",
    ]
    
    descriptions = [
        "A historical epic about a king and his kingdom.",
        "The epic conclusion to the Baahubali saga.",
        "A story of revolution against the British empire during the time of India's freedom struggle.",
        "A fantasy thriller where a man is reincarnated as a fly.",
        "A family drama about love and relationships.",
        "A love story of a man who is rebellious and passionate.",
        "A biographical film on the legendary actress Savitri.",
        "A story of a cricketer's journey from obscurity to fame.",
        "A thriller about a kidnapping and its consequences.",
        "A romantic drama about young love.",
        "A fantasy epic set in the kingdom of the Kshana Kshanam.",
        "A historical drama about a king's rise to power.",
        "A political drama about a man fighting for justice.",
    ]
    
    genres = [
        "Action, Drama",
        "Action, Drama",
        "Action, Drama, Historical",
        "Sci-Fi, Thriller",
        "Romance, Drama",
        "Drama, Romance",
        "Biography, Drama",
        "Drama, Sport",
        "Thriller, Drama",
        "Romance, Drama",
        "Action, Drama",
        "Action, Drama",
    ]
    
    # Taking the user's input for their favorite movie
    user_movie = st.text_input("Your Favorite Movie:")

    # If the user enters a movie, process the recommendation
    if user_movie:
        # Combine descriptions and genres for a better recommendation system
        enhanced_descriptions = [descriptions[i] + " " + genres[i] for i in range(len(movies))]
        
        # Convert the text data into a matrix of token counts
        vectorizer = CountVectorizer().fit_transform(enhanced_descriptions)
        
        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(vectorizer)
        
        try:
            # Find the index of the movie the user entered
            movie_index = movies.index(user_movie)
            
            # Get similarity scores for the movie
            similarities = similarity_matrix[movie_index]
            
            # Sort the movies based on similarity scores (excluding the input movie)
            recommendations = sorted(
                [(movies[i], similarities[i], descriptions[i]) for i in range(len(movies)) if i != movie_index],
                key=lambda x: x[1],
                reverse=True
            )
            
            st.write("Recommended Movies based on your choice:")

            # Show top 5 recommendations with descriptions
            for rec_movie, _, rec_description in recommendations[:5]:  # Show top 5 recommendations
                st.write(f"**{rec_movie}**")
                st.write(f"Description: {rec_description}")
                
        except ValueError:
            st.warning("Sorry, the movie you entered is not in our database. Please check the spelling.")
