import streamlit as st
from auxiliar.aux_vendas import *


st.title("Teste Streamlit - Página 2")
df = gerar_dados_fakes()

lista_de_meses = list(df['Month'].unique())
lista_de_meses.insert(0, 'Todos')

lista_de_categorias = list(df['Category'].unique())
lista_de_categorias.insert(0, 'Todos')

seletor_mes = st.selectbox("Selecione um mês", lista_de_meses)
seletor_categoria = st.selectbox("Selecione uma categoria", lista_de_categorias)

if seletor_mes == 'Todos':
  filtered_df = df
else:
  filtered_df = df.loc[df['Month'] == seletor_mes]

if seletor_categoria == 'Todos':
  filtered_df = df
else:
  filtered_df = df.loc[df['Category'] == seletor_categoria]

st.dataframe(filtered_df,use_container_width= True)
