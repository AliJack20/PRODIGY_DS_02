import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

print(df.head())

print(df.shape)

print(df.isna().sum())  # Checks missing values

print()

print(df.duplicated().sum())  # Checks duplicate values in dataset

print()

print(df.describe())  # Statistics of the dataset


