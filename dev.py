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

# ==========================================
# CO2 - DATA VISUALIZATION
# Complete code for all 12 questions
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ------------------------------------------
# 1. CREATE SAMPLE DATASET
# ------------------------------------------

data = {
    'Product': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Sales': [100, 200, 150, 300, 250, 400],
    'Profit': [20, 50, 30, 80, 60, 100],
    'Quantity': [10, 20, 15, 30, 25, 40],
    'Category': ['Food', 'Clothes', 'Food',
                 'Electronics', 'Clothes', 'Electronics']
}

df = pd.DataFrame(data)

print("Sample Dataset:")
print(df)

# ==========================================
# Q3. LINE, SCATTER, HISTOGRAM, BOX,
# BAR AND PIE CHARTS
# ==========================================

plt.figure(figsize=(12, 8))

# Line chart
plt.subplot(2, 3, 1)
plt.plot(df['Product'], df['Sales'], marker='o')
plt.title("Line Chart")
plt.xlabel("Product")
plt.ylabel("Sales")

# Scatter plot
plt.subplot(2, 3, 2)
plt.scatter(df['Sales'], df['Profit'])
plt.title("Scatter Plot")
plt.xlabel("Sales")
plt.ylabel("Profit")

# Histogram
plt.subplot(2, 3, 3)
plt.hist(df['Sales'], bins=5)
plt.title("Histogram")

# Box plot
plt.subplot(2, 3, 4)
plt.boxplot(df['Sales'])
plt.title("Box Plot")

# Bar chart
plt.subplot(2, 3, 5)
plt.bar(df['Product'], df['Sales'])
plt.title("Bar Chart")

# Pie chart
plt.subplot(2, 3, 6)
plt.pie(df['Sales'], labels=df['Product'],
        autopct='%1.1f%%')
plt.title("Pie Chart")

plt.tight_layout()
plt.show()


# ==========================================
# Q6. 2 x 2 SUBPLOT LAYOUT
# ==========================================

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(df['Product'], df['Sales'])
plt.title("Line Chart")

plt.subplot(2, 2, 2)
plt.bar(df['Product'], df['Profit'])
plt.title("Bar Chart")

plt.subplot(2, 2, 3)
plt.hist(df['Sales'])
plt.title("Histogram")

plt.subplot(2, 2, 4)
plt.boxplot(df['Profit'])
plt.title("Box Plot")

plt.tight_layout()
plt.show()


# ==========================================
# Q8. STACKED BAR CHART
# ==========================================

food = [100, 150, 200]
clothes = [120, 180, 220]

years = ['2023', '2024', '2025']

plt.bar(years, food, label='Food')
plt.bar(years, clothes, bottom=food,
        label='Clothes')

plt.title("Stacked Bar Chart")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend()
plt.show()


# ==========================================
# Q10. PARETO CHART WITH CUMULATIVE %
# ==========================================

df_sorted = df.sort_values(
    by='Sales', ascending=False
)

df_sorted['Cumulative'] = df_sorted['Sales'].cumsum()

df_sorted['Cumulative_Percentage'] = (
    df_sorted['Cumulative'] /
    df_sorted['Sales'].sum()
) * 100

plt.bar(df_sorted['Product'], df_sorted['Sales'])

plt.plot(df_sorted['Product'],
         df_sorted['Cumulative_Percentage'],
         color='red', marker='o')

plt.title("Pareto Chart")
plt.xlabel("Product")
plt.ylabel("Sales / Cumulative Percentage")
plt.show()

print(df_sorted)


# ==========================================
# Q12. FREQUENCY POLYGON
# ==========================================

frequency, bins = np.histogram(
    df['Sales'], bins=4
)

midpoints = (bins[:-1] + bins[1:]) / 2

plt.plot(midpoints, frequency,
         marker='o')

plt.title("Frequency Polygon")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid()
plt.show()


# ==========================================
# Q14. CUMULATIVE TOTAL AND PERCENTAGE
# ==========================================

cumulative = df['Sales'].cumsum()

percentage = (
    cumulative / df['Sales'].sum()
) * 100

plt.plot(df['Product'], cumulative,
         marker='o', label='Cumulative Total')

plt.plot(df['Product'], percentage,
         marker='s', label='Cumulative Percentage')

plt.title("Cumulative Total and Percentage")
plt.xlabel("Product")
plt.legend()
plt.grid()
plt.show()


# ==========================================
# Q16. LINEAR SCALE VS LOGARITHMIC SCALE
# ==========================================

values = [10, 100, 1000, 10000, 100000]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(values, marker='o')
plt.title("Linear Scale")

plt.subplot(1, 2, 2)
plt.plot(values, marker='o')
plt.yscale('log')
plt.title("Logarithmic Scale")

plt.tight_layout()
plt.show()


# ==========================================
# Q20. 3D SCATTER PLOT
# ==========================================

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['Sales'],
           df['Profit'],
           df['Quantity'])

ax.set_xlabel("Sales")
ax.set_ylabel("Profit")
ax.set_zlabel("Quantity")

ax.set_title("3D Scatter Plot")
plt.show()


# ==========================================
# Q23. COMPARATIVE VISUALIZATION
# WITH ANNOTATIONS AND LEGENDS
# ==========================================

plt.plot(df['Product'], df['Sales'],
         marker='o', label='Sales')

plt.plot(df['Product'], df['Profit'],
         marker='s', label='Profit')

plt.annotate("Highest Sales",
             xy=('F', 400),
             xytext=('D', 350),
             arrowprops=dict(arrowstyle='->'))

plt.title("Sales vs Profit")
plt.xlabel("Product")
plt.ylabel("Amount")
plt.legend()
plt.grid()
plt.show()


# ==========================================
# Q26. INTERACTIVE VISUALIZATION USING PLOTLY
# ==========================================

import plotly.express as px

fig = px.bar(df, x='Product', y='Sales',
             color='Category',
             title='Interactive Sales Chart')

fig.show()


# ==========================================
# Q30. INTERACTIVE VISUALIZATION USING BOKEH
# ==========================================

from bokeh.plotting import figure, show
from bokeh.io import output_notebook

output_notebook()

p = figure(title="Interactive Sales Chart",
           x_range=df['Product'].tolist(),
           width=600, height=400)

p.vbar(x=df['Product'].tolist(),
       top=df['Sales'].tolist(),
       width=0.5)

p.xaxis.axis_label = "Product"
p.yaxis.axis_label = "Sales"

show(p)


# ==========================================
# Q36. REFERENCE LINES AND ANNOTATIONS
# ==========================================

plt.plot(df['Product'], df['Sales'],
         marker='o', label='Sales')

# Horizontal reference line
plt.axhline(y=200, color='red',
            linestyle='--',
            label='Reference Line')

# Annotation
plt.annotate("Maximum Sales",
             xy=('F', 400),
             xytext=('D', 350),
             arrowprops=dict(arrowstyle='->'))

plt.title("Reference Line and Annotation")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()

print("ALL 12 VISUALIZATIONS COMPLETED!")

 