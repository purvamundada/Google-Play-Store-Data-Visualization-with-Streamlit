import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st

dataset = st.container()

with dataset:
  st.write("Google Playstore Dataset")
  df = pd.read_csv('/content/googleplaystore.csv')
  st.write(df.head())
  st.write("Category Distribution")
  st.bar_chart(df['Category'].value_counts())
  st.write("Rating Comparison")
  df_cleaned = df.dropna(subset=['Rating'])
  st.bar_chart(df_cleaned["Rating"].value_counts())
  st.write('Average Rating by Category')
  df_agg = df.groupby('Category', as_index=False)['Rating'].mean()
  df_agg = df_agg.sort_values(by='Rating', ascending=False)
  fig = px.bar(df_agg, x='Category', y='Rating', color_discrete_sequence=['skyblue'])
  st.plotly_chart(fig)
  
