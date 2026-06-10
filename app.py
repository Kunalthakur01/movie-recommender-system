import streamlit as st
import pickle
import pandas as pd
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=cfe4ddf76fdc8b77d88b68a323b850e9&language=en-US"

        response = requests.get(
            url,
            verify=False,
            timeout=10
        )

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path

        # Default image if no poster exists
        return "https://via.placeholder.com/500x750?text=No+Poster"

    except Exception as e:
        print(f"Movie ID {movie_id}:", e)

        return "https://via.placeholder.com/500x750?text=No+Poster"
    
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in movie_list[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']

        recommended_movie_names.append(
            movies.iloc[i[0]]['title']
        )

        recommended_movie_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movie_names, recommended_movie_posters

st.title("Movies Recommender System")
movies_dict = pickle.load(open("movies_dict.pkl","rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl","rb"))


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)



if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
