# src/data_visualization.py

import streamlit as st
import matplotlib.pyplot as plt

def plot_data(data):
    # Assume 'data' has a 'x' and 'y' column
    plt.plot(data['x'], data['y'])
    st.pyplot(plt)

def plot_histogram(data):
    # Assume 'data' has a 'score' column
    plt.hist(data['score'], bins=10)
    st.pyplot(plt)