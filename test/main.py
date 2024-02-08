import streamlit as st

# Get the value of the "name" query parameter
name_value = st.text_input("Enter Name", value="", key="name")

# Display the value
st.write("Name:", name_value)
