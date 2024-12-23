import streamlit as st
from auxiliar.aux_vendas import *


st.title("Teste Streamlit - Página 2")
df = gerar_dados_fakes(1000)

lista_de_meses = list(df['Month'].unique())
lista_de_meses.insert(0, 'Todos')

lista_de_categorias = list(df['Category'].unique())
lista_de_categorias.insert(0, 'Todos')

col_1, col_2 = st.columns(2)

with col_1:
  seletor_mes = st.selectbox("Selecione um mês", lista_de_meses)
with col_2:
  seletor_categoria = st.selectbox("Selecione uma categoria", lista_de_categorias)

filtered_df = df

if seletor_mes == 'Todos':
  pass
else:
  filtered_df = filtered_df.loc[df['Month'] == seletor_mes]

if seletor_categoria == 'Todos':
  pass
else:
  filtered_df = filtered_df.loc[df['Category'] == seletor_categoria]

st.dataframe(filtered_df,use_container_width= True)
