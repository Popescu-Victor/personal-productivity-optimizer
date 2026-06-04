import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from tkinter import filedialog


filepath = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])

df = pd.read_csv(filepath)

def calculate_tilt(df):
    pass


if __name__ == "__main__":
        df = pd.read_csv('your_data.csv')
        tilt = calculate_tilt(df)
        print(tilt)


