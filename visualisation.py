
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student": ["S1", "S2", "S3", "S4", "S5", "S6"],
    "Department": ["A", "A", "A", "B", "B", "B"],
    "Study_Hours": [1, 2, 3, 6, 7, 8],
    "Marks": [80, 85, 90, 50, 55, 60]
}

df = pd.DataFrame(data)

overall = df["Study_Hours"].corr(df["Marks"])

print("Combined Correlation:", round(overall, 4))

for dept, group in df.groupby("Department"):
    r = group["Study_Hours"].corr(group["Marks"])
    print("Department", dept, "Correlation:", round(r, 4))

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks",
    hue="Department",
    s=100
)

plt.title("Study Hours vs Marks by Department")
plt.xlabel("Study Hours per Week")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
