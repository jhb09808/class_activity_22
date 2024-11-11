# Home.py
import streamlit as st

st.set_page_config(page_title="My Dashboard", page_icon="📊", layout="wide")

st.title("Welcome to My Dashboard")
st.write("Navigate using the sidebar to explore different pages.")

# pages/1_Data_Overview.py
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Data Overview")

# Load and display data
df = pd.read_csv("your_data.csv")
st.dataframe(df)

# Create and display a Plotly chart
fig = px.scatter(df, x="column1", y="column2")
st.plotly_chart(fig)

# pages/2_Deep_Dive.py
import streamlit as st
import plotly.graph_objects as go

st.title("Deep Dive Analysis")

# Add more complex visualizations and analysis here
