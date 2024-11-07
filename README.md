# Streamlit

Streamlit es un framework de código abierto para crear aplicaciones web interactivas de manera rápida y sencilla, especialmente diseñado para científicos de datos, ingenieros de machine learning y desarrolladores de Python. Streamlit permite convertir scripts de Python en aplicaciones web altamente interactivas con muy poca cantidad de código adicional, sin necesidad de conocimientos de HTML, CSS o JavaScript.

## Características principales de Streamlit:

- **Desarrollo rápido de aplicaciones:** Streamlit hace que el desarrollo de aplicaciones web sea increíblemente rápido. Con solo unas pocas líneas de código, puedes crear interfaces interactivas que se actualizan en tiempo real.

- **Interactividad en tiempo real:** Las aplicaciones construidas con Streamlit son altamente interactivas. Cualquier cambio en los widgets de la interfaz (como deslizadores, botones, entradas de texto, gráficos, etc.) actualiza instantáneamente el resultado en la página web sin necesidad de recargarla.

- **Integración con bibliotecas populares de Python:** Streamlit se integra de manera fluida con bibliotecas como Pandas (para el manejo de datos), Matplotlib, Plotly o Altair (para visualización de datos) y scikit-learn (para machine learning). Esto lo hace ideal para crear dashboards o interfaces interactivas que presenten resultados de análisis o modelos de machine learning.

- No requiere frontend: A diferencia de otros frameworks web, como Flask o Django, Streamlit no requiere que los desarrolladores trabajen en el frontend (HTML, CSS, JavaScript). Todo lo que necesitas es Python para crear la interfaz y gestionar la lógica.

- Facilidad para compartir y desplegar: Las aplicaciones creadas con Streamlit pueden ser desplegadas fácilmente en servidores o en plataformas como Streamlit Sharing, Heroku, o AWS. Además, las aplicaciones son accesibles a través de un navegador web, lo que facilita su compartición.

- **Composición de widgets interactivos:** Streamlit ofrece una variedad de widgets (como botones, deslizadores, casillas de verificación, entradas de texto, etc.) que permiten crear aplicaciones interactivas sin esfuerzo. Puedes crear interfaces de usuario complejas y dinámicas con solo unos pocos comandos en Python.

- **Visualización de datos de alto nivel:** La integración con bibliotecas de visualización de datos es muy sencilla. Puedes incrustar gráficos y visualizaciones en tu aplicación con apenas una línea de código, lo que es ideal para prototipos rápidos o presentaciones de análisis de datos.

## Documentación Git de Streamlit

https://github.com/streamlit/streamlit

## Instalación

1 Crea un entorno virtual (si aún no lo has hecho):

```sh
python -m venv venv
```

2 Activa el entorno virtual:

- En Windows:

```sh
.\venv\Scripts\activate
```

- En Mac/Linux:

```sh
source venv/bin/activate
```

- Instala las dependencias usando pip:

```sh
pip install streamlit black plotly docx2txt PyPDF2 openpyxl
```

## Correr aplicación

- Posicionarse sobre la raiz del proyecto y ejecutar el archivo python a probar por ejemplo:

```sh
streamlit run app0.py
```
*** 

## Assets

<p align="center">
### Formulario - App0.py

![Screenshot 1](https://github.com/klintfox/streamlit_course/blob/main/assets/0-0.PNG?raw=true)

![Screenshot 2](https://github.com/klintfox/streamlit_course/blob/main/assets/0-1.PNG?raw=true)

![Screenshot 3](https://github.com/klintfox/streamlit_course/blob/main/assets/0-2.PNG?raw=true)

![Screenshot 4](https://github.com/klintfox/streamlit_course/blob/main/assets/0-3.PNG?raw=true)

***
### Audio, Video Image y Dataframe - App1.py


![Screenshot 1](https://github.com/klintfox/streamlit_course/blob/main/assets/1-0.PNG?raw=true)

![Screenshot 2](https://github.com/klintfox/streamlit_course/blob/main/assets/1-1.PNG?raw=true)

***
### Charts - App2.py


![Screenshot 1](https://github.com/klintfox/streamlit_course/blob/main/assets/2-0.PNG?raw=true)

![Screenshot 2](https://github.com/klintfox/streamlit_course/blob/main/assets/2-1.PNG?raw=true)

***
### Carga y Guardado de Archivos - App3.py

![Screenshot 1](https://github.com/klintfox/streamlit_course/blob/main/assets/3-0.PNG?raw=true)

![Screenshot 2](https://github.com/klintfox/streamlit_course/blob/main/assets/3-1.PNG?raw=true)

![Screenshot 3](https://github.com/klintfox/streamlit_course/blob/main/assets/3-2.PNG?raw=true)
</p>

***