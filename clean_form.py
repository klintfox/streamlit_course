import os

import streamlit as st


def clear_form():
    st.session_state["foo"] = ""
    st.session_state["bar"] = ""
    
with st.form("myform"):
    f1, f2 = st.columns([1, 1])
    with f1:
        st.text_input("Foo", key="foo")
    with f2:
        st.text_input("Bar", key="bar")

    f3, f4 = st.columns([1, 1])
    with f3:
        submit = st.form_submit_button(label="Submit")
    with f4:
        clear = st.form_submit_button(label="Clear", on_click=clear_form)

if submit:
    st.write('Submitted')

if clear:
    st.write('Cleared')
    
st.write(st.session_state.foo)
st.write(st.session_state.bar)

