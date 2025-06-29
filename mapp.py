import pickle
import streamlit as st
import pandas as pd
import requests
import os
from pathlib import Path

def fetch_poster(imdb_id):
    """Fetch movie poster using OMDB API"""
    try:
        
        url = f"http://www.omdbapi.com/?i={imdb_id}&apikey=e1d6ad24"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
        
        data = response.json()
        
        if data.get('Response') == 'True' and data.get('Poster') != 'N/A':
            return data.get('Poster')
        else:
            return "https://via.placeholder.com/300x450?text=No+Image+Available"
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/300x450?text=Error+Loading+Image"
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return "https://via.placeholder.com/300x450?text=Error"

def load_data():
    """Load movie data and similarity matrix"""
    try:
       
        possible_paths = [
            
            ('movie_list.pkl', 'similarity.pkl'),
            
            ('model/movie_list.pkl', 'model/similarity.pkl'),
            
            ('/Users/sahirchoudhury/Movie_Recommender_System/model/movie_list.pkl', 
             '/Users/sahirchoudhury/Movie_Recommender_System/model/similarity.pkl')
        ]
        
        data, similarity = None, None
        
        for movie_path, sim_path in possible_paths:
            try:
                if os.path.exists(movie_path) and os.path.exists(sim_path):
                    with open(movie_path, 'rb') as f:
                        data = pickle.load(f)
                    with open(sim_path, 'rb') as f:
                        similarity = pickle.load(f)
                    st.success(f"Data loaded successfully from {movie_path}")
                    break
            except Exception as e:
                continue
        
        if data is None or similarity is None:
            st.error("Could not load data files. Please check file paths.")
            return None, None
            
        return data, similarity
        
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

def recommend(movie, data, similarity):
    """Recommend similar movies"""
    try:
        
        if movie not in data['title'].values:
            st.error(f"Movie '{movie}' not found in dataset.")
            return [], []
        
        
        index = data[data['title'] == movie].index[0]
        
        
        if isinstance(similarity, pd.DataFrame):
            similarity_row = similarity.iloc[index]
        else:
            similarity_row = similarity[index]
        
        
        distances = sorted(list(enumerate(similarity_row)), reverse=True, key=lambda x: x[1])
        
        recommended_movie_names = []
        recommended_movie_posters = []
        
        
        for i in distances[1:6]:
            movie_idx = i[0]
            movie_data = data.iloc[movie_idx]
            
            
            movie_title = movie_data['title']
            recommended_movie_names.append(movie_title)
            
            
            imdb_id = movie_data.get('imdb_id', '')
            if imdb_id:
                poster_url = fetch_poster(imdb_id)
            else:
                poster_url = "https://via.placeholder.com/300x450?text=No+IMDb+ID"
            
            recommended_movie_posters.append(poster_url)
        
        return recommended_movie_names, recommended_movie_posters
        
    except Exception as e:
        st.error(f"Error in recommendation: {e}")
        return [], []


def main():
    st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
    st.header('🎬 Movie Recommender System')
    
    
    with st.spinner('Loading movie data...'):
        data, similarity = load_data()
    
    if data is None or similarity is None:
        st.error("Failed to load data. Please ensure the pickle files are in the correct location.")
        st.info("Expected files: 'movie_list.pkl' and 'similarity.pkl'")
        return
    
    
    st.info(f"Dataset loaded: {len(data)} movies available")
    
    
    movie_list = sorted(data['title'].values)
    selected_movie = st.selectbox(
        "🎥 Type or select a movie from the dropdown", 
        movie_list,
        help="Start typing to search for a movie"
    )
    
    
    if st.button('🔍 Show Recommendations', type="primary"):
        if selected_movie:
            with st.spinner('Finding recommendations...'):
                recommended_movie_names, recommended_movie_posters = recommend(
                    selected_movie, data, similarity
                )
            
            if recommended_movie_names:
                st.subheader(f"🎯 Top 5 Recommendations for '{selected_movie}'")
                
                
                cols = st.columns(5)
                for i in range(len(recommended_movie_names)):
                    with cols[i]:
                        st.image(
                            recommended_movie_posters[i], 
                            caption=recommended_movie_names[i],
                            use_container_width=True
                        )
                        
            else:
                st.warning("Sorry, we couldn't find any recommendations for that movie.")
        else:
            st.warning("Please select a movie first.")

if __name__ == "__main__":
    main()