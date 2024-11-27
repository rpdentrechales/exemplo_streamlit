import streamlit as st
from auxiliar.aux_vendas import *

df = gerar_dados_fakes()
st.title("Teste Streamlit - Página 2")

st.dataframe(df)
