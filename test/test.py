import numpy as np
import pandas as pd
import yfinance as yf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import streamlit as st

# Set page title and icon
st.set_page_config(
    page_title="Switch To Bit",
    page_icon="🪙",
)

# Streamlit Navbar
page_options = ["Home", "About", "Contact"]
selected_page = st.sidebar.radio("Navigation", page_options)

# Load Model
model = load_model('Bitcoin_Price_prediction_Model.h5')

# Home Page
if selected_page == "Home":
    st.header('Cryptocurrency Price Predictor')
    st.subheader('Crypto Price Data')

    # Initialize 'stock' with a default value
    stock = st.text_input('Enter Crypto ', 'DOGE-USD', key='crypto_input')

    try:
    
            # Set start and end dates
        start = '2013-01-01'
        end = '2023-12-31'

        # Use the 'stock', 'start', and 'end' variables in the yf.download function
        data = yf.download(stock, start, end)
        data = data.reset_index()

        # Display data table
        st.write(data)

        # Display Bitcoin Line Chart with legends for each column
        st.subheader('Bitcoin Line Chart')

        # Select specific columns for the line chart
        selected_columns = st.multiselect("Select Columns for Line Chart", data.columns)
        if selected_columns:
            # Create a line chart with legends for each selected column
            line_chart = st.line_chart(data[selected_columns])

            # Display legends
            line_chart.add_legend()
    
            # Display MinMaxScaler information
            st.subheader('MinMaxScaler Information')
    
            # Initialize MinMaxScaler
            scaler = MinMaxScaler(feature_range=(0, 1))

            # Exclude datetime column before further processing
            train_data = data.drop(columns=['Date'])

            # Further processing
            train_data_scale = scaler.fit_transform(train_data)
            # ... rest of the code remains unchanged

    except Exception as e:
        st.warning(
            "If you are facing issues while searching for your crypto, you can try these methods:\n"
            "1. ✅ Double-check your spelling.\n"
            "2. ✅ Enter the appropriate crypto ticker.\n"
            "3. ✅ It's possible that your requested crypto ticker is not available or the date range is not valid."
        )

# About Page
elif selected_page == "About":

    st.title("About Us")

    st.write(
        "Welcome to our Cryptocurrency Price Prediction Application! We are a passionate team of developers "
        "dedicated to providing you with accurate and insightful cryptocurrency price predictions."
    )

    st.subheader("Our Mission")
    st.write(
        "Our mission is to empower users with the tools and information needed to make informed decisions "
        "in the volatile cryptocurrency market. We strive to deliver reliable price predictions to assist you "
        "in your cryptocurrency investment journey."
    )

    st.subheader("Why Choose Us?")
    st.write(
        "1. **Accurate Predictions**: Our model is built on advanced machine learning techniques to provide accurate "
        "cryptocurrency price predictions.\n"
        "2. **User-Friendly Interface**: We've designed our application with a user-friendly interface to make it easy "
        "for both beginners and experienced users.\n"
        "3. **Constant Updates**: We stay up-to-date with the latest market trends to ensure our predictions are as "
        "relevant as possible."
    )



    st.success("Thank you for choosing our Cryptocurrency Price Prediction App!")



# Contact Page
elif selected_page == "Contact":
    import streamlit as st

    st.title("Contact Us")

    st.write("Feel free to reach out to us with any questions, feedback, or inquiries.")

    # Create form inputs
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message", height=150)

    # Add a submit button
    if st.button("Submit"):
        # You can add your logic to handle the form submission here
        # For example, sending an email, storing the form data, etc.

        # Display a success message after submission
        st.success("Your message has been submitted successfully!")





