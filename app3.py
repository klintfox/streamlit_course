import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt # none : 
from PyPDF2 import PdfReader # none : 
import os

logo = Image.open(os.path.join("resources","logo.ico"))

st.set_page_config(page_title="Stremlit", page_icon=logo, layout="wide")

@st.cache_data
def cargarImagen(image_file):
    img = Image.open(image_file)
    return image_file
    
def leer_pdf(file):
    pdfReader = PdfReader(file)
    count = len(pdfReader.pages)
    todo_texto = ""
    for i in range(count):
        pagina = pdfReader.pages[i]
        todo_texto += pagina.extract_text()
    return todo_texto

def guardar_archivo(upload_file):
    #Crear el directorio
    if not os.path.exists("temp"):
        os.mkdir("temp")
    
    #Guardar archivo en directorio
    with open(os.path.join("temp", upload_file.name), "wb") as f:
        f.write(upload_file.getbuffer())
    return st.success(f"Archivo guardado: {upload_file.name} en temp")

def main():
    st.title("Bienvendo - Carga y Guardado de Archivos")
    menu = ["Imagenes","Conjunto de Datos","Archivo de Documentos"]
    opcion = st.sidebar.selectbox("Menú", menu, )
    
    if opcion  == "Imagenes":
        st.subheader("Imagen")
        archivo_imagen = st.file_uploader("Subir Imagenes", type=["png","jpeg","jpg"])
        if archivo_imagen is not None:            
            detalle_archivos = {"nombre_archivo": archivo_imagen.name,
                                "tipo_archivo": archivo_imagen.type,
                                "tamaño_archivo": archivo_imagen.size }
            st.write(detalle_archivos)
            st.image(cargarImagen(archivo_imagen), width=500)
            guardar_archivo(archivo_imagen)
            
        
    elif opcion  == "Conjunto de Datos":
        st.subheader("Conjunto de Datos")
        archivo_datos = st.file_uploader("subir CSV o Excel", type=["csv","xls"])
        if archivo_datos is not None:
              detalle_archivos = {"nombre_archivo": archivo_datos.name,
                                "tipo_archivo": archivo_datos.type,
                                "tamaño_archivo": archivo_datos.size }
              st.write(detalle_archivos)
              if detalle_archivos["tipo_archivo"] == "text/csv":
                df = pd.read_csv(archivo_datos)
              elif detalle_archivos["tipo_archivo"] == "application/vnd.ms-excel":
                df = pd.read_excel(archivo_datos)
              else:
                  dt = pd.DataFrame()
              st.dataframe(df)
              guardar_archivo(archivo_datos)
                
        
        
    elif opcion  == "Archivo de Documentos":
        st.subheader("Archivo de Documentos")
        archivo_doc = st.file_uploader("Subir Documento", type=["docx","pdf","txt"])
        if st.button("Procesar"):
            if archivo_doc is not None:
                detalle_archivos = {"nombre_archivo": archivo_doc.name,
                                "tipo_archivo": archivo_doc.type,
                                "tamaño_archivo": archivo_doc.size }
                st.write(archivo_doc)
                if archivo_doc.type == "text/plain":
                    texto = str(archivo_doc.read(), "utf-8")
                    st.write(texto)
                    
                elif archivo_doc.type == "application/pdf":
                    texto = leer_pdf(archivo_doc)
                    st.write(texto)
                    
                elif archivo_doc.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    texto = docx2txt.process(archivo_doc)
                    st.write(texto)
                
                guardar_archivo(archivo_doc)
                    

if __name__ == '__main__':
    main()