import pandas as pd
import streamlit as st
import numpy as np
#from time import sleep
#from sympy import simplify


# Título de  la página
st.set_page_config(layout="centered",
    page_title="Talento Tech",
    page_icon="🕰️"
)

# Columnas

t1, t2 = st.columns([0.3,0.7]) 

t1.image('index.jpg', width = 120)
t2.title("Visulización de datos")
t2.markdown(" **tel:** 3167465079 **| email:** andresvillabon2000@gmail.com ")

# Datos

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )



# Secciones
steps=st.tabs(["Pestaña 1", "Pestaña $\sqrt{4}$"])

#Sección 1
with steps[0]:
    st.write('Hola mundo')
   

# Sección 2
with steps[1]:
    st.text_input("Your name", key="name")
    st.session_state.name
