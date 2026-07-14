# Install requirement if needed: pip install scikit-learn
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Dataset of movies and their genres/descriptions
movies = [
    {"id": 0, "title": "The Dark Knight", "genres": "action thriller dark hero superhero"},
    {"id": 1, "title": "Inception", "genres": "sci-fi thriller mind-bending dream maze"},
    {"id": 2, "title": "The Matrix", "genres": "sci-fi action futuristic virtual-reality"},
    {"id": 3, "title": "Toy Story", "genres": "animation comedy family toy friendly disney"},
    {"id": 4, "title": "The Lion King", "genres": "animation drama family animal disney musical"},
    {"id": 5, "title": "Interstellar", "genres": "sci-fi drama space universe physics exploration"},
    {"id": 6, "title": "The Hangover", "genres": "comedy funny vegas friendship"},
    {"id": 7, "title": "Avengers: Endgame", "genres": "action superhero adventure fantasy marvel"}
]

# 2. Extract descriptions for vectorization
descriptions = [movie["genres"] for movie in movies]

# 3. Use TF-IDF vectorizer to transform text features to matrices
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(descriptions)

# 4. Calculate Cosine Similarity Matrix
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_movies(movie_title, num_recommendations=2):
    # Find index of target movie
    movie_idx = None
    for i, m in enumerate(movies):
        if m["title"].lower() == movie_title.lower():
            movie_idx = i
            break
            
    if movie_idx is None:
        return f"Movie '{movie_title}' not found in database."
    
    # Get similarity scores for this movie
    scores = list(enumerate(similarity_matrix[movie_idx]))
    
    # Sort the movies based on similarity score (excluding the selected movie itself)
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    
    recommendations = []
    for idx, score in sorted_scores:
        recommendations.append((movies[idx]["title"], round(score, 3)))
        
    return recommendations

if __name__ == "__main__":
    print("=========================================")
    print("   RECOMMENDATION SYSTEM (Task 4)        ")
    print("=========================================")
    
    # List available movies
    print("Available Movies in Dataset:")
    for movie in movies:
        print(f"- {movie['title']}")
    print()
    
    # Test recommendations
    test_movie = "Inception"
    print(f"Recommendations for '{test_movie}':")
    recs = recommend_movies(test_movie, num_recommendations=2)
    for title, score in recs:
         print(f"-> {title} (Similarity Score: {score})")
