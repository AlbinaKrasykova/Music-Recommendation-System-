# Here I am adding a recom system engine with a Database Vector 
import pandas as pd
import plotly.graph_objects as go
#from streamlit_lottie 
import json

'''
1. Load Data
2. Clean Data 
3. Add Recom Engine Fucntion Item based since we dont ahve precious hsitry it is the eaissts 
4. StreamLit Musc interface + Vector Database 
5. Add emotion based recom system

Kaggle Spotfy Dataset: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
Spotify : https://developer.spotify.com/documentation/web-api
log in to spotify
Streamlit + Weaviate: https://weaviate-movie-magic.streamlit.app/?ref=blog.streamlit.io
Run app command 

+ python3 -m streamlit run
'''
#APP lib
import streamlit as st
st.header("Music Movie Recommendation System")