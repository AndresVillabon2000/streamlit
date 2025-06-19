import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#from time import sleep
#from sympy import simplify


# Título de  la página#
#st.write('Hola mundo')


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
steps=st.tabs(["Pestaña 1", "Pestaña 2", "Pestaña $\sqrt{9}$"])

#Sección 1
with steps[0]:
    n=st.number_input("Elige el número hermanos que tiene",min_value=0,max_value=10,step=1)

   

# Sección 2
with steps[1]:
    selected_x_var = st.selectbox('What do want the x variable to be?',['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
                                                                        'body_mass_g'])
    selected_y_var = st.selectbox('What about the y?',
                                  ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
                                   'body_mass_g'])
    penguins_df = pd.read_csv('penguins.csv')
    #selected_species = st.selectbox('What species would you like to visualize?',
    #                                ['Adelie', 'Gentoo', 'Chinstrap'])
    #penguins_df = penguins_df[penguins_df['species'] == selected_species]
    #fig, ax = plt.subplots()
    #ax = sns.scatterplot(x = penguins_df[selected_x_var], y = penguins_df[selected_y_var])
    #plt.title('Scatterplot of {} Penguins'.format(selected_species))
    sns.set_style('darkgrid')
    markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
    fig, ax = plt.subplots()
    ax = sns.scatterplot(data = penguins_df, x = selected_x_var,
                         y = selected_y_var, hue = 'species', markers = markers,
                         style = 'species')
    plt.xlabel(selected_x_var)
    plt.ylabel(selected_y_var)
    st.pyplot(fig)
        
# Sección 3
with steps[2]:
    st.title('SF Trees')
    trees_df = pd.read_csv('trees.csv')
    st.write(trees_df.head())
    st.write('This app analyses trees in San Francisco using'  
             ' a dataset kindly provided by SF DPW')
    df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh'])['tree_id'].count())
    df_dbh_grouped.columns = ['tree_count']
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.line_chart(df_dbh_grouped)
    with col2:
        st.bar_chart(df_dbh_grouped)
    with col3:
        st.area_chart(df_dbh_grouped)

    trees_df1 = trees_df.dropna(subset=['longitude', 'latitude'])
    trees_df1 = trees_df1.sample(n = 1000)
    st.map(trees_df1)



    st.text_input("Your name", key="name")

    st.session_state.name