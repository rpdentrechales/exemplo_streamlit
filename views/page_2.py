import streamlit as st
from auxiliar.aux_vendas import *


st.title("Teste Streamlit - Página 2")
df = gerar_dados_fakes()

lista_de_meses = df['Month'].unique()
lista_de_meses.insert(0, 'Todos')

seletor_mes = st.selectbox("Selecione um mês", lista_de_meses)

filtered_df = df.loc[df['Month'] == seletor_mes]

st.dataframe(filtered_df,use_container_width= True)
