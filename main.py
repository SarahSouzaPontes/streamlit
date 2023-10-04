#pip install pandas numpy streamlit seaborn

import io

data = io.BytesIO(uploaded[r'C:\Users\Sarah.Pontes\Downloads\Call.csv'])
df = pd.read_csv(data)

#!pip install requests

import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
#import requests

st.title('Dashboard Cliente')

#convertendo colunas
#df['Answer Rate'] = df['Answer Rate'].str.rstrip("%").astype(float)/100

# Remove '%' symbol, convert to float, and handle non-numeric values
df['Answer Rate'] = pd.to_numeric(df['Answer Rate'].str.rstrip('%'), errors='coerce') / 100

col1, col2, col3 = st.columns(3)
col1.metric("Incoming Calls AVG", round(incoming_avg))
col2.metric("Answered Calls AVG", round(ansred_avg))
col3.metric("Answer Rate AVG", round(ans_avg))

st.line_chart(df[['Incoming Calls', 'Answered Calls']])