import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Leeemos el archivo original en formato parquet
df = pd.read_parquet('wine_reviews.parquet')

if st.checkbox('Mostrar Datos'):
    st.dataframe(df)

if st.checkbox('Mostrar Datos - Head o Tail'):
    if st.button('Mostrar Head'):
        st.write(df.head())
    if st.button('Mostrar Tail'):
        st.write(df.tail())

if st.checkbox('Mostrar Datos - Filas y Columnas'):
    dim = st.radio('Dimensiones de la Tabla de Datos:', ('Filas', 'Columnas'), horizontal=True)
    if dim == 'Filas':
        st.write('Cantidad de filas:', df.shape[0])
    else:
        st.write('Cantidad de columnas:', df.shape[1])

precio_limite = st.slider('Define precio maximo', 0, 4000, 250)

fig = plt.figure(figsize=(6,4))
sns.scatterplot(x='price', y='points', data=df[df['price']<precio_limite])
st.pyplot(fig)

countries_list = df['country'].unique().tolist()
countries = st.multiselect('Seleccione uno o varios paises:', countries_list, default=['Argentina', 'Chile', 'Spain'])
df_countries = df[df['country'].isin(countries)]

fig= plt.figure(figsize=(6,4))
sns.scatterplot(x='price', y='points', hue='country', data=df_countries)
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    df_countries = df[df['country']=='Argentina']
    fig=plt.figure()
    sns.scatterplot(x='price', y='points', data=df_countries)
    plt.title('Puntajes segun precio para vinos de Argentina')
    st.pyplot(fig)

with col2:
    df_countries = df[df['country']=='Chile']
    fig=plt.figure()
    sns.scatterplot(x='price', y='points', data=df_countries)
    plt.title('Puntajes segun precio para vinos de Chile')
    st.pyplot(fig)
