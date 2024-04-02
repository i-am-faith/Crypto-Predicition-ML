import streamlit as st
import plotly.express as px
from backend import get_data
import datetime  # Import datetime module for getting today's date

# Set page title and icon
st.set_page_config(
    page_title="Weather Prediction",
    page_icon="☁️",
)

# Navbar
page_options = ["Home", "About", "Contact"]
selected_page = st.sidebar.radio("Navigation", page_options)

if selected_page == "Home":
    st.title("Weather Forecast")
    local_image_path = "images/weather_photo.jpg"
    st.image(local_image_path, use_column_width=True)

    place = st.text_input(label="Place", placeholder="Enter A City...", key="city")
    days = st.slider(
        label="Forecast days",
        min_value=1,
        max_value=5,
        key="days-slider",
        help="Select the number of forecasted days",
    )
    option = st.selectbox(
        label="Select type of data to view",
        options=(["Temperature", "Sky"]),
        key="dataselect",
    )
    st.subheader(f"{option} for the next {days} day(s) in {place}")

    try:
        if place:
            filter_data = get_data(place, days)

            # Get today's date and weekday name
            today_date = datetime.datetime.today().date()
            today_weekday = datetime.datetime.today().strftime("%A")

            for day_num in range(days):
                # Calculate the date for each forecast day
                forecast_date = today_date + datetime.timedelta(days=day_num)
                forecast_weekday = forecast_date.strftime("%A")

                st.subheader(f"Day {day_num + 1} ({forecast_date}) - {forecast_weekday}")
                day_data = filter_data[day_num * 6: (day_num + 1) * 6]

                # Create a temperature plot
                if option == "Temperature":
                    temps = [dict["main"]["temp"] / 10 for dict in day_data]
                    times = [dict["dt_txt"].split()[1] for dict in day_data]
                    figure = px.line(
                        x=times,
                        y=temps,
                        labels={"x": "Time", "y": "Temperature (C)"},
                    )
                    st.plotly_chart(figure)

                elif option == "Sky":
                    sky_conditions = [dict["weather"][0]["main"] for dict in day_data]
                    images = {
                        "Clear": "images/clear.png",
                        "Clouds": "images/cloud.png",
                        "Rain": "images/rain.png",
                        "Snow": "images/snow.png",
                    }
                    image_paths = [images[condition] for condition in sky_conditions]
                    captions = [
                        f"{timestamp}: {condition}" for timestamp, condition in zip(
                            ["12am", "4am", "8am", "12pm", "4pm", "8pm"], sky_conditions
                        )
                    ]
                    st.image(image_paths, caption=captions, width=115)

    except KeyError:
        st.warning("PLEASE ENTER A VALID CITY!! ")
        st.warning(
            "If you are facing issues while searching for your City, you can try these methods:\n"
            "1. ✅ Double-check your spelling.\n"
            "2. ✅ Enter the appropriate city.\n"
            "3. ✅ It's possible that your requested geocode address is invalid"
        )

# About Page
elif selected_page == "About":
    st.title("About Us")

    st.write(
        "1. Welcome to Our Weather Prediction Application!\n"
        "2. I am Sourin Mukherjee with my team, dedicated to providing you with accurate and insightful weather predictions.\n"
        "3. ⚠️THIS WEBSITE IS USED FOR TRAINING AND DEVELOPMENT PURPOSES⚠️"
    )

    team_image = "images/project members.png"
    st.image(team_image, use_column_width=True)

    st.success("Thank you for choosing our Weather App!")

# Contact Page
elif selected_page == "Contact":
    st.title(":mailbox: Get In Touch With Us")
    st.write("Feel free to reach out to us with any questions, feedback, or inquiries.")

    contact_form = """
    <form action="https://formsubmit.co/sourin.mukherjee2105833@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f" <style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")
