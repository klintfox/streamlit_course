import streamlit as st
import pandas as pd
from PIL import Image
import os 

def main():
        
    st.title("Bienvenido - Formulario, Audio, Video Image y Dataframe")

    # Image
    st.header("Imagen")
    img= Image.open(os.path.join("resources","imagen.jpg"))
    st.image(img, use_column_width=True)
    
    st.header("Imagen desde la web")
    st.image("https://picsum.photos/800")
    
    #Video
    st.header("Video")
    with open(os.path.join("resources","video.mp4"), "rb") as video_file:
        st.video(video_file.read(), start_time=0, autoplay=True)
        
    # Musica
    st.header("Audio")
    with open(os.path.join("resources","musica.mp3"), "rb") as audio_file:
        st.audio(audio_file.read(), start_time=0, autoplay=True)
    

if __name__ == '__main__':
    main()