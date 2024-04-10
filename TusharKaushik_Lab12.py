import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv("car_data.csv")

data = load_data()

# Sidebar
st.sidebar.header("Filter Options")

# Text box to input car_name
car_name = st.sidebar.text_input("Enter Car Name (Optional)")

# Multiselect to choose Transmission type
transmission_options = ['Manual', 'Automatic']
selected_transmission = st.sidebar.multiselect("Choose Transmission Type", transmission_options, default=transmission_options)

# Slider to choose a range of selling_price
selling_price_range = st.sidebar.slider("Select Selling Price Range", min_value=0, max_value=30, value=(0, 20))

# Slider to choose a range of year
year_range = st.sidebar.slider("Select Year Range", min_value=2000, max_value=2024, value=(2000, 2024))

# Button to apply filters
if st.sidebar.button("Submit"):
    filtered_data = data.copy()

    # Apply filters
    if car_name:
        filtered_data = filtered_data[filtered_data['Car_Name'].str.contains(car_name, case=False)]
    
    filtered_data = filtered_data[filtered_data['Transmission'].isin(selected_transmission)]
    filtered_data = filtered_data[(filtered_data['Selling_Price'] >= selling_price_range[0]) & (filtered_data['Selling_Price'] <= selling_price_range[1])]
    filtered_data = filtered_data[(filtered_data['Year'] >= year_range[0]) & (filtered_data['Year'] <= year_range[1])]

    # Show filtered data
    st.write(filtered_data)
else:
    # Show original data
    st.write(data)
