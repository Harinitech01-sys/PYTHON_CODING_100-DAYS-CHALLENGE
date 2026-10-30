import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

# EXPLORATORY DATA ANALYSIS (EDA)

import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display last 5 rows
print("Last 5 rows:")
print(df.tail())

# Dataset dimensions
print("Shape:")
print(df.shape)

# Column names
print("Columns:")
print(df.columns)

# Information about dataset
print("Dataset Information:")
df.info()

# Statistical summary
print("Statistical Summary:")
print(df.describe())

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Check duplicate values
print("Duplicate Values:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numerical values with mean
df = df.fillna(df.mean(numeric_only=True))

# Check missing values again
print("After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)
