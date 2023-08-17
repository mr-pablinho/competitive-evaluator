import streamlit as st
from src.data_loader import load_data
from src.data_visualization import plot_data, plot_histogram
from src.utils import generate_options

# Load custom CSS
st.markdown("""
<style>
    /* Load external CSS */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
    /* Link to your local CSS file */
    .css-styles {
        font-family: 'Arial', sans-serif;
    }
</style>
""", unsafe_allow_html=True)


# Title and Subtitle
st.title("My Streamlit App")
st.subheader("An Example App with Title, Subtitle, Table, Plot, and Slider")

# Load data
data = load_data()

# Display Table
st.write("## Table")
st.table(data)

# Dropdown List to Select Plot Type
st.write("## Plot Type Selector")
plot_type = st.selectbox("Select a plot type:", ["Line Plot", "Histogram"])

# Display Plot Based on Selection
if plot_type == "Line Plot":
    st.write("## Line Plot")
    plot_data(data)
elif plot_type == "Histogram":
    st.write("## Histogram")
    plot_histogram(data)

# Sliding Menu to Select Items from a List
st.write("## Slider Menu")
options = generate_options(data)
selected_item = st.select_slider('Select an item:', options=options)

st.write("You selected:", selected_item)
