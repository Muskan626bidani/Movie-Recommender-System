
import streamlit as st
import pickle
import pandas as pd
import requests
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('data.pkl','rb'))

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']

def recommend (movie):
  # find the index of array and then goes into similarity matix
  movies_list=similarity[movie];

  # movie_index=movies[movies['title'].values==movie].index[0]
  # distances=similarity[movie_index]
  # movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:7]
  recommend_movies=[]
  # recommend_movies_poster=[]
  for i in movies_list:
  #   # print(new_df['title'][i[0]])
  #   # movie_id=movies.iloc[i[0]].movie_id
    recommend_movies.append(i)
  #   recommend_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
  return recommend_movies
    # ,recommend_movies_poster


st.title('Movie Recommender System')
selected_movie=st.selectbox('which movie you like',(movies['title'].values))
if st.button('Recommend'):
    st.write('Similar Movie to: '+selected_movie)
    name=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(name[0])
        # st.image(poster[0])
    with col2:
        st.text(name[1])
        # st.image(poster[1])
    with col3:
        st.text(name[2])
        # st.image(poster[2])
    with col4:
        st.text(name[3])
        # st.image(poster[3])
    with col5:
        st.text(name[4])
        # st.image(poster[4])
