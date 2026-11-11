# 9. Complete Practical Project — Student Performance Data Analysis

Phase 03 Practical Project

Now let's combine all seven topics into one practical project.

Project: Student Performance Analysis

Objective: Analyze student performance and discover how attendance and study hours affect marks.

### Step 1: Create Dataset

```
import pandas as pdimport numpy as npdata = {    "Name": [        "Amir", "Rahul", "Mohit",        "Aman", "Priya", "Rahul"    ],    "Age": [20, 21, 22, 20, 21, 21],    "Study_Hours": [5, 3, 7, 2, 6, 3],    "Attendance": [90, 75, 95, 60, 85, 75],    "Marks": [85, 65, 95, np.nan, 80, 65]}df = pd.DataFrame(data)print(df)
```

### Step 2: Understand Dataset

```
print(df.head())print(df.shape)print(df.info())print(df.describe())
```

### Step 3: Data Cleaning

```
# Remove duplicatesdf = df.drop_duplicates()# Check missing valuesprint(df.isnull().sum())# Fill missing marks with mediandf["Marks"] = df["Marks"].fillna(    df["Marks"].median())
```

### Step 4: Find Outliers

```
Q1 = df["Marks"].quantile(0.25)Q3 = df["Marks"].quantile(0.75)IQR = Q3 - Q1lower = Q1 - 1.5 * IQRupper = Q3 + 1.5 * IQRprint(df[    (df["Marks"] < lower) |    (df["Marks"] > upper)])
```

### Step 5: Data Analysis

```
# Average marksprint("Average Marks:", df["Marks"].mean())# Highest marksprint("Highest Marks:", df["Marks"].max())# Lowest marksprint("Lowest Marks:", df["Marks"].min())# Average attendanceprint("Average Attendance:", df["Attendance"].mean())# Study hours and marks correlationprint(df[["Study_Hours", "Marks"]].corr())
```

### Step 6: Data Visualization

```
import matplotlib.pyplot as pltimport seaborn as sns# Marks distributionsns.histplot(df["Marks"], kde=True)plt.title("Student Marks Distribution")plt.show()# Study hours vs markssns.scatterplot(    data=df,    x="Study_Hours",    y="Marks")plt.title("Study Hours vs Marks")plt.show()# Attendance vs markssns.scatterplot(    data=df,    x="Attendance",    y="Marks")plt.title("Attendance vs Marks")plt.show()# Correlation heatmapsns.heatmap(    df.select_dtypes(include="number").corr(),    annot=True,    cmap="coolwarm")
```
### Step 7: Generate Insights

After analyzing the dataset, answer:

1. Which student scored the highest marks?
2. What is the average student performance?
3. Is there a relationship between attendance and marks?
4. Do students studying more hours tend to score higher?
5. Are there any unusual records?
6. What recommendations can improve student performance?

Project Complete

This project combines Data Cleaning, Missing Values, Duplicates, Outliers, Transformation concepts, EDA and Visualization.

Note: This is a small practice dataset. Its results are illustrative, not sufficient to establish general conclusions about student performance.