import streamlit as st
import pandas as pd
import numpy as np
import random

def gerar_dados_fakes():
  # Generate a sample DataFrame
  np.random.seed(42)
  rows = 100  # Number of rows in the DataFrame

  data = {
      "Date": pd.date_range(start="2023-01-01", periods=rows, freq="D"),
      "Sales": np.random.randint(100, 1000, size=rows),
      "Category": [random.choice(["Electronics", "Clothing", "Home", "Books", "Toys"]) for _ in range(rows)],
      "Region": [random.choice(["North", "South", "East", "West"]) for _ in range(rows)],
      "Customer_Type": [random.choice(["New", "Returning"]) for _ in range(rows)],
  }

  df = pd.DataFrame(data)
  df['Month'] = df['Date'].dt.strftime('%B')

  return df
