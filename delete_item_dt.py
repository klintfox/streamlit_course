import streamlit as st
import pandas as pd

# Configuración de la página
def configure_page():
    st.set_page_config(layout="wide")

# Inicializar sesión y datos
def initialize_session_data():
    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame({'horaInicio': [], 'horaFin': []})

# Limpiar formulario
def clear_form():
    st.session_state["foo"] = ""
    st.session_state["bar"] = ""

# Añadir nueva fila al DataFrame
def add_dfForm():
    horaInicio = st.session_state["foo"]
    horaFin = st.session_state["bar"]
    
    if horaInicio and horaFin:
        new_row = pd.DataFrame({'horaInicio': [horaInicio], 'horaFin': [horaFin]})
        st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)
        clear_form()

# Lógica de edición de filas
def handle_row_deletion():
    edited_rows = st.session_state["data_editor"]["edited_rows"]
    rows_to_delete = []

    for idx, value in edited_rows.items():
        if value["x"] is True:
            rows_to_delete.append(idx)

    # Eliminar filas seleccionadas
    if rows_to_delete:
        st.session_state["data"] = st.session_state["data"].drop(rows_to_delete, axis=0).reset_index(drop=True)

# Mostrar el editor de datos
def display_data_editor():
    columns = st.session_state["data"].columns
    column_config = {column: st.column_config.Column(disabled=True) for column in columns}

    # Crear una copia del DataFrame con la columna 'x' para marcar filas a eliminar
    modified_df = st.session_state["data"].copy()
    modified_df["x"] = False  # Columna para eliminar
    modified_df = modified_df[["x"] + modified_df.columns[:-1].tolist()]

    st.data_editor(
        modified_df,
        key="data_editor",
        on_change=handle_row_deletion,
        hide_index=True,
        column_config=column_config,
    )

# Crear formulario para ingresar horas
def create_time_form():
    # Crear columnas para las entradas de hora
    placeholder_for_horaInicio, placeholder_for_horaFin = st.columns(2)

    with placeholder_for_horaInicio:
        horaInicio = st.text_input('Ingrese la hora inicio', key='foo')

    with placeholder_for_horaFin:
        horaFin = st.text_input('Ingrese la hora fin', key="bar")

    return horaInicio, horaFin

# Función principal que organiza la app
def main():
    configure_page()
    initialize_session_data()

    # Crear formulario de horas
    horaInicio, horaFin = create_time_form()

    # Formulario para agregar los datos
    dfForm = st.form(key='dfForm')

    with dfForm:
        st.empty()  # Placeholder para las columnas de hora
        add_button = st.form_submit_button("Add", on_click=add_dfForm, disabled=not (horaInicio and horaFin))

    # Mostrar el editor de datos
    display_data_editor()

    # Agregar el botón de "Process" después de mostrar el DataFrame
    process_button = st.button("Process", type="primary")

    if process_button:
        st.success('Process')

if __name__ == "__main__":
    main()
