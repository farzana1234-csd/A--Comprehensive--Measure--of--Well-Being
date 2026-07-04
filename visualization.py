import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
Development = pd.read_csv("dataset/hdi.csv")

# First 20 rows
data1 = Development.head(20)

# 1. Unique Country Values
print(data1["Country"].unique())

# 2. Mean Years of Schooling vs HDI
plt.figure(figsize=(8,5))
sns.stripplot(
    x=data1["Mean Years of Schooling (2021)"],
    y=data1["Human Development Index (2021)"]
)