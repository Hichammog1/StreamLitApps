import streamlit as st
import pandas as pd

# Title of the page
st.title("Dropdown Search Page")

# Load data from CSV file
df = pd.read_csv('data.csv')

# Extracting data for each dropdown list from the dataframe
data1 = df['Fruit'].tolist()
data2 = df['Animal'].tolist()
data3 = df['Color'].tolist()
data4 = df['Vehicle'].tolist()
data5 = df['Food'].tolist()
data6 = df['Language'].tolist()

# Creating six dropdown lists with the data from the CSV
option1 = st.selectbox('Select a Fruit', data1)
option2 = st.selectbox('Select an Animal', data2)
option3 = st.selectbox('Select a Color', data3)
option4 = st.selectbox('Select a Vehicle', data4)
option5 = st.selectbox('Select a Food', data5)
option6 = st.selectbox('Select a Programming Language', data6)

# Search button
if st.button('Search'):
    st.write("You selected:")
    st.write(f"Fruit: {option1}")
    st.write(f"Animal: {option2}")
    st.write(f"Color: {option3}")
    st.write(f"Vehicle: {option4}")
    st.write(f"Food: {option5}")
    st.write(f"Programming Language: {option6}")
