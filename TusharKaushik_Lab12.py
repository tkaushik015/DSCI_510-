import streamlit as st  # Streamlit library for creating web apps
import pandas as pd  # Pandas library for data manipulation

# Function to load car dataset
@st.cache  # Streamlit's caching mechanism to load data only once
def fetch_car_dataset():
    # Load and return car data from a CSV file
    return pd.read_csv("car_data.csv")

# Fetching the car data using the defined function
car_dataset = fetch_car_dataset()

# Creating a sidebar for user inputs
st.sidebar.header("Customize Your Search")

# User input for filtering by car name
input_car_name = st.sidebar.text_input("Type Car Name (Optional)")

# User choice for car transmission type
transmission_choices = ['Manual', 'Automatic']
chosen_transmission = st.sidebar.multiselect("Select Transmission Type", transmission_choices, default=transmission_choices)

# User selection for car selling price range using a slider
price_range = st.sidebar.slider("Set Selling Price Range", min_value=0, max_value=30, value=(0, 20))

# User selection for car manufacturing year range
year_range = st.sidebar.slider("Set Manufacturing Year Range", min_value=2000, max_value=2024, value=(2000, 2024))

# Button to filter the dataset based on user inputs
if st.sidebar.button("Apply Filters"):
    # Making a copy of the dataset for filtering
    dataset_filtered = car_dataset.copy()

    # Filtering dataset based on user inputs
    if input_car_name:
        dataset_filtered = dataset_filtered[dataset_filtered['Car_Name'].str.contains(input_car_name, case=False)]
    
    dataset_filtered = dataset_filtered[dataset_filtered['Transmission'].isin(chosen_transmission)]
    dataset_filtered = dataset_filtered[(dataset_filtered['Selling_Price'] >= price_range[0]) & (dataset_filtered['Selling_Price'] <= price_range[1])]
    dataset_filtered = dataset_filtered[(dataset_filtered['Year'] >= year_range[0]) & (dataset_filtered['Year'] <= year_range[1])]

    # Displaying the filtered dataset
    st.write(dataset_filtered)
else:
    # Displaying the original dataset if no filters are applied
    st.write(car_dataset)
