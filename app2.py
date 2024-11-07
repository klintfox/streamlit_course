import streamlit as st
from PIL import Image
import plotly.express as px # none : 
import pandas as pd
import os

logo = Image.open(os.path.join("resources","logo.ico"))

st.set_page_config(page_title="Stremlit", page_icon=logo, layout="wide",
                   initial_sidebar_state="collapsed")

def main():
    st.title("Bienvenido - Charts")
    st.sidebar.header("Navegación")
    df = pd.read_csv(os.path.join("resources", "empleados.csv"))
    st.dataframe(df)
    
    #Gender pie chart
    df_count = df.groupby('Gender').count().reset_index()
    fig = px.pie(df_count, values="EmpID", names="Gender", title="Género")
    st.plotly_chart(fig)
    
    
    # Promedio
    df_avg =df.groupby('Dept')['Stress'].mean().reset_index()
    fig2 = px.bar(df_avg, "Dept", "Stress", color="Dept")
    st.plotly_chart(fig2)
    
    
if __name__ == '__main__':
    main()