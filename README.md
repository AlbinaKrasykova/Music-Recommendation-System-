## Spotify Music-Recommendation-System

## Plan & Resources 

## Function:
1. Load Data
2. Clean Data 
3. Recommendation Engine Function 
4. StreamLit Music Interface + Vector Database 



## Extra Resources


- Kaggle Spotify Dataset - https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
- Emotion Text Classifier (Hugging Face)
- Face Classification: Emotion Detection Model
- Spotify API Documentation
- Streamlit + Weaviate Demo - https://weaviate-movie-magic.streamlit.app/?ref=blog.streamlit.io
- Tensoflow recommender - https://medium.com/@pauloyc/tensorflow-recommenders-for-powerful-recommendation-system-e3dec138a07f


## Presentation

https://www.canva.com/design/DAGeXdMbcKM/4dwXG-7sm0Mq5WutrqhTyA/edit?utm_content=DAGeXdMbcKM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Spotify credentials:
   ```
   SPOTIFY_CLIENT_ID=your_spotify_client_id_here
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```
