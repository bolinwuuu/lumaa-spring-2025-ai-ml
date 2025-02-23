import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
import random

# load and preprocess data
def load_data(file_path='data/movie_500.csv'):
    df = pd.read_csv(file_path)
    return df.dropna()

# compute TF-IDF vectors
def vectorize_text(data):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(data)
    return vectorizer, tfidf_matrix

# recommend movies based on consine similarity with user input
def recommend(user_input, df, vectorizer, tfidf_matrix, top_n=5):
    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return df.iloc[top_indices], similarities[top_indices]

# load and transform data into TD-IDF
df = load_data()
vectorizer, tfidf_matrix = vectorize_text(df['overview'])

def main():
    if len(sys.argv) != 2:
        print("Usage: python recommend.py <user_input>")
        sys.exit(1)

    user_input = sys.argv[1]

    # get recommendations
    recommendations, scores = recommend(user_input, df, vectorizer, tfidf_matrix)

    print("Top Recommendations:")
    for i, (title, score) in enumerate(zip(recommendations['title'], scores), 1):
        print(f"{i}. {title}")

if __name__ == "__main__":
    main()