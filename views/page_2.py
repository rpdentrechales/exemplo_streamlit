import streamlit as st
from auxiliar.aux_vendas import *


st.title("Teste Streamlit - Página 2")
df = gerar_dados_fakes()

seletor_mes = st.selectbox("Selecione um mês", df['Month'].unique())

filtered_df = df.loc[df['Month'] == seletor_mes]

st.dataframe(filtered_df,use_container_width= True)
