import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import os 

logo = Image.open(os.path.join("resources","logo.ico"))
st.set_page_config(page_title="Stremlit", page_icon=logo, layout="wide")

df = pd.read_csv(os.path.join("resources","data.csv"))

def main():
    st.title("Bienvenido - Formulario")
    
    #Formulario
    nombre = st.text_input("Ingresa tu nombre:")
    st.write(nombre)
    
    mensaje = st.text_area("Ingresa tu mensaje ", height=10)
    st.write(mensaje)
    
    numero = st.number_input("Ingresa un numero", 1.0, 25.0, step=1.0)
    st.write(numero)
    
    cita = st.date_input("Selecciona una fecha")
    st.write(cita)
    
    hora = st.time_input("Selecciona la hora")
    st.write(hora)
    
    color = st.color_picker("Selecciona el color")
    st.write(color)
    
    #SelectBox
    opcion  = st.selectbox(
        'Elige tu fruta favorita',
        ['Naranja','Pera','Papaya','Piña','Uva']
    )    
    st.write(f"tu fruta favorita es:  {opcion} ")
    
    #MultiSelect
    opciones = st.multiselect(
        'Elige tu color favorito',
        ['Rojo','Verde','Azul','Blanco','Amarillo','Morado','Negro']
    )
    st.write("Tus colores favoritos son:", opciones)
    
    #Slider
    edad = st.slider(
        'Seleciona tu edad',
        min_value=0,
        max_value=100,
        value=25, # valor inicial
        step=1
    )
    st.write(f"Tu edad es: {edad}")
    
    #Select Slider
    nivel = st.select_slider(
        'Selecciona tu nivel de satisfaccion',
        options=['Muy bajo','Bajo','Medio','Alto', 'Muy alto'],
        value='Medio'
    )
    st.write("Tu nivel de satisfaccion es: ", nivel)
            
    #DataFrame: 
    st.header("Dataframe:")
    st.dataframe(df)    
    st.write(df.head(10))
    st.json({"clave": "valor"})
    
    #Codigo: 
    codigo = """
    def saludar():
        print("Hola")
        """
    st.code(codigo, language="python")
    

if __name__ == '__main__':
    main()