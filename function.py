# Here I am adding a recom system engine with a Database Vector 
import pandas as pd
import plotly.graph_objects as go
#from streamlit_lottie 
import json

#!/bin/bash

import mlcroissant as mlc
import pandas as pd

# Fetch the Croissant JSON-LD
croissant_dataset = mlc.Dataset('www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset/croissant/download')

# Check what record sets are in the dataset
record_sets = croissant_dataset.metadata.record_sets
print(record_sets)

# Fetch the records and put them in a DataFrame
record_set_df = pd.DataFrame(croissant_dataset.records(record_set=record_sets[0].uuid))
print(record_set_df.head())



 
'''
1. Load Data
2. Clean Data 
3. Add Recom Engine Fucntion Item based since we dont ahve precious hsitry it is the eaissts 
4. StreamLit Musc interface + Vector Database 
5. Add emotion based recom system
- python3 -m pip install mlcroissant


Kaggle Spotfy Dataset: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
emotion text classifer huggin face model : https://huggingface.co/michellejieli/emotion_text_classifier
face clasification: modle emotion detetcion : 
Spotify : https://developer.spotify.com/documentation/web-api
log in to spotify
Streamlit + Weaviate: https://weaviate-movie-magic.streamlit.app/?ref=blog.streamlit.io
Run app command 

+ python3 -m streamlit run
+pip install mlcroissant

'''
#APP lib
import streamlit as st
st.header("Music Movie Recommendation System")