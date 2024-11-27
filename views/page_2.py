import streamlit as st
from auxiliar.aux_vendas import *


st.title("Teste Streamlit - Página 2")
df = gerar_dados_fakes()



st.dataframe(df,use_container_width= True)
