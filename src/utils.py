# src/utils.py

def generate_options(data):
    # Generate a list of unique items from the 'Name' column of 'data'
    options = data['Name'].unique().tolist()
    return options
