import streamlit as st
import pickle
import pandas as pd
import requests

def feth_movie_posters(movie_id):
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4083f8b2ae6f110c19958122a23c7e85'.format(movie_id))
        data = response.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movie = []
    recommend_movie_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        recommend_movie.append((movies.iloc[i[0]].title))

        # fetch poster from api
        recommend_movie_posters.append(feth_movie_posters(movie_id)) 

    return recommend_movie, recommend_movie_posters



movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    '',
     movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image([posters[0]])

    with col2:
        st.text(names[1])
        st.image([posters[1]])

    with col3:
        st.text(names[2])
        st.image([posters[2]])


    with col4:
        st.text(names[3])
        st.image([posters[3]])


    with col5:
        st.text(names[4])
        st.image([posters[4]])




