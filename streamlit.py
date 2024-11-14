import streamlit as st
import pickle
from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd
import numpy as np 


def main():
    # Title of the app
    st.title("Movie Rating Prediction App")

    # Input fields for features
    st.write("Please enter the following details about the movie:")

    # Input fields for non-genre features
    numVotes = st.number_input("Number of Votes", min_value=0, max_value=1_000_000, value=100)
    releaseYear = st.number_input("Release Year", min_value=1900, max_value=2024, value=2020)
    num_genres = st.number_input("Number of Genres", min_value=1, max_value=10, value=1)

    # One-hot encoded genre fields (checkboxes for each genre)
    st.write("Select the genres for this movie:")

    genres = [
        'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary',
        'Drama', 'Family', 'Fantasy', 'Game-Show', 'History', 'Horror', 'Music', 'Musical',
        'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show',
        'Thriller', 'War', 'Western'
    ]

    # Create a dictionary to map user input to one-hot encoded values
    input_genres = {genre: st.checkbox(genre) for genre in genres}

    # Prepare the feature array for prediction
    features = np.array([[
        input_genres['Action'], input_genres['Adventure'], input_genres['Animation'],
        input_genres['Biography'], input_genres['Comedy'], input_genres['Crime'],
        input_genres['Documentary'], input_genres['Drama'], input_genres['Family'],
        input_genres['Fantasy'], input_genres['Game-Show'], input_genres['History'],
        input_genres['Horror'], input_genres['Music'], input_genres['Musical'],
        input_genres['Mystery'], input_genres['News'], input_genres['Reality-TV'],
        input_genres['Romance'], input_genres['Sci-Fi'], input_genres['Short'],
        input_genres['Sport'], input_genres['Talk-Show'], input_genres['Thriller'],
        input_genres['War'], input_genres['Western'], numVotes, releaseYear, num_genres
    ]])

    # Loading the saved model
    with open('best_model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)


    # Make a prediction when the button is clicked
    if st.button("Predict Average Rating"):
        prediction = loaded_model.predict(features)
        st.write(f"Predicted Average Rating: {prediction[0]:.2f}")

main()

