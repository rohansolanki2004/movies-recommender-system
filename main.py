import streamlit as st
import pickle
import pandas as pd

def add_bg_from_url():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

with open('movies_dict.pkl', 'rb') as f:
    movies_dict = pickle.load(f)

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

movies = pd.DataFrame(movies_dict)

def recommend(movie):
    if movie not in movies['title'].values:
        return []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# ---------------- Streamlit UI ----------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

add_bg_from_url()

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar movie recommendations instantly!")

selected_movie_name = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)

    if recommendations:
        st.subheader("Recommended Movies:")
        for movie in recommendations:
            st.write("👉", movie)
    else:
        st.warning("No recommendations found.")
