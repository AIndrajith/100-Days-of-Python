import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

data = load_data("stock_data.csv")
print(data.head())