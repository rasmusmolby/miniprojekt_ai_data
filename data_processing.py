import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('NFL.csv')

print(df.info())
print(df.describe())

df.loc[df < 'NA'] = np.nan

def plot_missing_values(data):
    missing_counts = data.isnull().sum()
    
    plt.figure(figsize=(10, 5))
    missing_counts.plot(kind='bar', color='red')
    plt.xlabel("Features")
    plt.ylabel("Number of Missing Values")
    plt.title("Missing Values per Feature")
    plt.xticks(rotation=45)
    plt.show()

plot_missing_values(df)