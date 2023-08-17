# src/data_loader.py

import pandas as pd

def load_data():
    data = pd.read_csv("data/data.csv")
    return data

def load_type_chart():
    # chart containing the type effectiveness 
    type_chart = pd.read_csv("data/type_chart.csv", sep=",", decimal=".")
    type_chart.set_index('Attacking', inplace=True, drop=True)
    return type_chart
