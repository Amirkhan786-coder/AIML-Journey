# Phase 03 — Data Analysis (Complete Notes)



AI/ML Roadmap

Intermediate Level



Goal: Learn how to clean, understand, transform, analyze and visualize real-world datasets before applying Machine Learning algorithms.

## 1. Introduction to Data Analysis

### What is Data Analysis?

Definition: Data Analysis is the process of inspecting, cleaning, transforming and interpreting data to discover useful information, patterns and conclusions.

Easy Explanation (Hinglish):

Data Analysis ka simple meaning hai raw data ko samajhna aur usme se useful information nikalna.

For example, imagine you have a student dataset:

| Name  | Marks | Attendance |
| ----- | ----- | ---------- |
| Amir  | 85    | 90%        |
| Rahul | 65    | 75%        |
| Mohit | 92    | 95%        |
| Aman  | NaN   | 80%        |

You need to:

- Find missing marks.
- Remove duplicate records.
- Identify unusual values.
- Calculate average marks.
- Find students with highest marks.
- Create graphs to understand performance.

This complete process is called Data Analysis.

### Why is Data Analysis important?

1. Helps understand raw data.
2. Improves data quality.
3. Finds hidden patterns.
4. Detects errors and unusual values.
5. Supports better decision-making.
6. Prepares datasets for Machine Learning.

### Data Analysis Workflow

1\. Raw Data Collection

CSV, Excel, SQL, APIs

2\. Data Cleaning

Missing values, duplicates, errors

3\. Data Transformation

Formatting, encoding, scaling

4\. Exploratory Data Analysis (EDA)

Patterns, trends, relationships

5\. Data Visualization

Charts, graphs, dashboards

6\. Insights & Conclusions

Meaningful results and decisions

## 2. Data Cleaning

Very High Priority

### What is Data Cleaning?

Definition: Data Cleaning is the process of detecting and correcting inaccurate, incomplete, inconsistent or irrelevant data.

Hinglish: Real-world datasets mein bahut errors hote hain. Data Cleaning ka kaam un errors ko identify karke correct karna hai.

### Example

Original dataset:

| Name  | Age | City   |
| ----- | --- | ------ |
| Amir  | 20  | Delhi  |
| Rahul | 21  | delhi  |
| Mohit | -5  | Mumbai |
| Amir  | 20  | Delhi  |
| Aman  | NaN | Jaipur |

Problems:

- Duplicate records.
- Negative age.
- Missing age.
- Inconsistent city spelling.

After cleaning, the dataset becomes more reliable.

### Common Data Cleaning Tasks

1. Handling missing values.
2. Removing duplicates.
3. Correcting incorrect data.
4. Fixing inconsistent formats.
5. Detecting outliers.
6. Removing unnecessary columns.
7. Correcting data types.

### Important Pandas Functions

| Function               | Purpose                  |
| ---------------------- | ------------------------ |
| `df.head()`            | First 5 rows             |
| `df.info()`            | Dataset information      |
| `df.describe()`        | Statistical summary      |
| `df.isnull()`          | Detect missing values    |
| `df.dropna()`          | Remove missing rows      |
| `df.fillna()`          | Fill missing values      |
| `df.drop_duplicates()` | Remove duplicates        |
| `df.astype()`          | Change data type         |
| `df.replace()`         | Replace incorrect values |

### Practical Code

```
import pandas as pddata = {    "Name": ["Amir", "Rahul", "Mohit", "Amir"],    "Age": [20, 21, -5, 20],    "Marks": [85, 90, None, 85]}df = pd.DataFrame(data)# View datasetprint(df)# Dataset informationprint(df.info())# Remove duplicate recordsdf = df.drop_duplicates()# Replace invalid agedf.loc[df["Age"] < 0, "Age"] = Noneprint(df)
```

Important: Data cleaning does not mean deleting every unusual value. First understand whether a value is genuinely incorrect or represents a real situation.

## 3. Missing Values

Very High Priority

### What are Missing Values?

Definition: Missing values are data entries that are absent or unavailable in a dataset.

In Pandas, missing values are commonly represented as:

- `NaN`
- `None`
- `NaT` (for datetime data)

Example:

| Name  | Age | Salary |
| ----- | --- | ------ |
| Amir  | 20  | 25000  |
| Rahul | NaN | 30000  |
| Mohit | 22  | NaN    |
| Aman  | 21  | 28000  |

Here, Age and Salary contain missing values.

### Why do Missing Values occur?

1. User did not enter information.
2. Data collection errors.
3. Sensor failure.
4. Database problems.
5. Information was unavailable.
6. Data was lost during collection or processing.

### Step 1: Detect Missing Values

```
# Check missing valuesprint(df.isnull())# Count missing values per columnprint(df.isnull().sum())# Calculate missing percentageprint(df.isnull().mean() * 100)
```

### Step 2: Handle Missing Values

There are three common approaches.

Method 1: Remove Missing Values

`dropna()` removes rows containing missing values by default.

```
df.dropna(inplace=True)
```

Use when missing records are relatively few and removing them will not introduce bias.

Method 2: Fill Missing Values

`fillna()` replaces missing values.

```
df["Age"] = df["Age"].fillna(20)
```

Method 3: Fill Using Mean, Median and Mode

| Method | Meaning             | Best use                            |
| ------ | ------------------- | ----------------------------------- |
| Mean   | Average value       | Normally distributed numerical data |
| Median | Middle value        | Numerical data with outliers        |
| Mode   | Most frequent value | Categorical data                    |

Mean example:

```
df["Marks"] = df["Marks"].fillna(    df["Marks"].mean())
```

Median example:

```
df["Age"] = df["Age"].fillna(    df["Age"].median())
```

Mode example:

```
df["City"] = df["City"].fillna(    df["City"].mode()[0])
```

### Important: Types of Missing Data

| Type | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| MCAR | Missing Completely At Random                                 |
| MAR  | Missing At Random, depending on observed data                |
| MNAR | Missing Not At Random, depending on the missing value itself |

Interview point: Never blindly replace every missing value with zero. Choose a method based on the meaning and distribution of the data.

## 4. Duplicates

### What are Duplicate Values?

Definition: Duplicate records are repeated rows or entries that appear more than once in a dataset.

Example:

| ID | Name  | Marks |
| -- | ----- | ----- |
| 1  | Amir  | 85    |
| 2  | Rahul | 90    |
| 3  | Mohit | 75    |
| 1  | Amir  | 85    |

Here, the record for Amir is repeated.

### Why are Duplicates a Problem?

- Incorrect statistical calculations.
- Wrong average values.
- Biased Machine Learning models.
- Unreliable reports.
- Increased dataset size.

### Important Pandas Functions

1\. Detect duplicates

```
print(df.duplicated())
```

2\. Count duplicates

```
print(df.duplicated().sum())
```

3\. Remove duplicates

```
df.drop_duplicates(inplace=True)
```

4\. Check duplicates using specific columns

```
print(df.duplicated(subset=["Name"]))
```

5\. Keep the last occurrence

```
df.drop_duplicates(    keep="last",    inplace=True)
```

### Types of Duplicate Records

- Exact duplicates: All column values are the same.
- Partial duplicates: Some important column values repeat.
- Business duplicates: Same real-world entity appears with different formatting.

Real-world example: An online shopping database contains the same customer record multiple times. Removing unwanted duplicates helps maintain accurate customer information.

## 5. Outliers

High Priority for ML

### What are Outliers?

Definition: Outliers are observations that differ significantly from most other observations in a dataset.

Hinglish: Agar most students ke marks 50–90 ke beech hain aur ek student ke marks 500 hain, toh 500 suspicious outlier ho sakta hai.

Example:

`20, 22, 24, 25, 27, 29, 200`

Here, 200 is an unusually high value.

### Causes of Outliers

1. Human typing errors.
2. Sensor malfunction.
3. Data collection errors.
4. Rare but genuine events.
5. Natural variations in data.

### Methods to Detect Outliers

Method 1: IQR (Interquartile Range)

IQR is the difference between the third quartile and first quartile.

\\[ IQR=Q3-Q1 \\]

Outlier boundaries:

\\[ Lower=Q1-1.5(IQR) \\]

\\[ Upper=Q3+1.5(IQR) \\]

Values below Lower or above Upper are potential outliers.

Python:

```
Q1 = df["Salary"].quantile(0.25)Q3 = df["Salary"].quantile(0.75)IQR = Q3 - Q1lower = Q1 - 1.5 * IQRupper = Q3 + 1.5 * IQRoutliers = df[    (df["Salary"] < lower) |    (df["Salary"] > upper)]print(outliers)
```

Method 2: Z-Score

Z-score measures how many standard deviations a value is away from the mean.

\\[ Z=\frac{X-\mu}{\sigma} \\]

Common rule: A Z-score above 3 or below -3 may indicate an outlier.

```
from scipy.stats import zscoredf["z_score"] = zscore(df["Salary"])outliers = df[    df["z_score"].abs() > 3]print(outliers)
```

Method 3: Box Plot

Box plots visually identify unusual observations.

[Chapter 2: The Middle and the Mess — A Little Bit of Everything in Biostatistics for Health Science Students](https://images.openai.com/static-rsc-4/OUce9PnoLYaB4sJ8wuK0QkiKKkxwq41Hu_rmehZdZoEMsiwz4XmlTrRBSQ_8_8EZZkNLY2RKXF2JZAY_7aSvVtTt0RGgXbDCo3f4XNzVGlu6pc-ARWZr6zdQOnshg5obqFP3aTQ8aaG2h8XPeQ_K1L-c7Avhrmwxy8Mk09lkbNU?purpose=inline)

[paytonyau.github.io](https://paytonyau.github.io/biostats-book/chapters/02_middle.html?utm_source=chatgpt.com)

### How to Handle Outliers?

1. Remove incorrect observations.
2. Replace values when justified.
3. Apply capping or winsorization.
4. Use log transformation for highly skewed data.
5. Keep genuine extreme values.

Important: Every outlier is not an error. For example, a millionaire's salary may be a genuine extreme value.

## 6. Data Transformation

Very High Priority for ML

### What is Data Transformation?

Definition: Data Transformation is the process of converting data from one format, structure or scale into another format to make it suitable for analysis and Machine Learning.

Hinglish: Raw data ko analysis ya ML model ke according modify karna Data Transformation kehlata hai.

### Why is Data Transformation Important?

- Makes data consistent.
- Improves data quality.
- Converts categorical data into numerical values.
- Helps ML algorithms process data.
- Brings numerical features to comparable scales.
- Makes data easier to analyze.

### Important Types of Data Transformation

1\. Normalization

Normalization converts numerical values into a common range, commonly 0 to 1.

Formula:

\\[ X'=\frac{X-X\_{min}}{X\_{max}-X\_{min}} \\]

Example:

```
from sklearn.preprocessing import MinMaxScalerscaler = MinMaxScaler()df[["Marks"]] = scaler.fit_transform(    df[["Marks"]])print(df)
```

Use cases:

- Neural Networks.
- K-Nearest Neighbors.
- Distance-based algorithms.

2\. Standardization

Standardization transforms data so that it has approximately:

- Mean = 0
- Standard deviation = 1

Formula:

\\[ Z=\frac{X-\mu}{\sigma} \\]

Python:

```
from sklearn.preprocessing import StandardScalerscaler = StandardScaler()df[["Marks"]] = scaler.fit_transform(    df[["Marks"]])
```

Use cases:

- Logistic Regression.
- SVM.
- PCA.
- K-Means.

Normalization vs Standardization

| Normalization                  | Standardization                               |
| ------------------------------ | --------------------------------------------- |
| Usually scales between 0 and 1 | Mean 0, standard deviation 1                  |
| Uses min and max               | Uses mean and standard deviation              |
| Sensitive to extreme min/max   | Can also be affected by outliers              |
| Useful for bounded features    | Useful for many statistical and ML algorithms |

3\. Encoding Categorical Data

Machine Learning algorithms generally need numerical inputs. Encoding converts categorical values into numbers.

Example:

| Gender | Encoded |
| ------ | ------- |
| Male   | 0       |
| Female | 1       |

Two important methods:

Label Encoding

```
from sklearn.preprocessing import LabelEncoderle = LabelEncoder()df["Gender"] = le.fit_transform(    df["Gender"])
```

One-Hot Encoding

```
df = pd.get_dummies(    df,    columns=["City"],    dtype=int)print(df)
```

Example:

| City   | Delhi | Mumbai | Jaipur |
| ------ | ----- | ------ | ------ |
| Delhi  | 1     | 0      | 0      |
| Mumbai | 0     | 1      | 0      |
| Jaipur | 0     | 0      | 1      |

4\. Data Type Conversion

Convert data types according to requirements.

```
df["Age"] = df["Age"].astype(int)df["Salary"] = df["Salary"].astype(float)
```

5\. Date and Time Transformation

Extract useful information from date columns.

```
df["Date"] = pd.to_datetime(df["Date"])df["Year"] = df["Date"].dt.yeardf["Month"] = df["Date"].dt.monthdf["Day"] = df["Date"].dt.day
```

6\. Log Transformation

Used to reduce right skewness in highly skewed numerical data.

```
import numpy as npdf["Salary_log"] = np.log1p(df["Salary"])
```

### Important Note: Data Leakage

Never calculate preprocessing statistics using the complete dataset before splitting into training and testing sets.

Correct workflow:

1. Split training and testing data.
2. Fit scaler or encoder on training data.
3. Transform training data.
4. Transform testing data using the same fitted transformer.

This prevents information from the test dataset leaking into training.

## 7. EDA — Exploratory Data Analysis

Extremely High Priority

### What is EDA?

Definition: Exploratory Data Analysis (EDA) is the process of analyzing and investigating datasets using statistical methods and visualization techniques to understand their main characteristics.

Hinglish: EDA ka matlab hai dataset ko deeply explore karna, uske patterns, trends, relationships aur problems ko samajhna.

Before building an ML model, EDA helps you understand what your dataset actually contains.

### Objectives of EDA

1. Understand the dataset.
2. Identify missing values.
3. Detect duplicates.
4. Find outliers.
5. Understand data distribution.
6. Discover relationships between variables.
7. Identify important features.
8. Generate useful insights.

### Types of EDA

1\. Univariate Analysis

Analysis of a single variable.

Example: Analyze only student marks.

Questions:

- What is the average mark?
- What is the maximum mark?
- How are marks distributed?

```
print(df["Marks"].describe())print(df["Marks"].mean())print(df["Marks"].median())print(df["Marks"].mode())
```

Useful visualizations:

- Histogram.
- Box plot.
- Bar chart.

2\. Bivariate Analysis

Analysis of two variables to understand their relationship.

Example:

- Study hours vs marks.
- Salary vs experience.
- Attendance vs performance.

```
print(df[["Study_Hours", "Marks"]].corr())
```

Useful visualizations:

- Scatter plot.
- Line plot.
- Grouped bar chart.

3\. Multivariate Analysis

Analysis of three or more variables together.

Example:

- Study hours.
- Attendance.
- Previous marks.
- Final performance.

```
import seaborn as snsimport matplotlib.pyplot as pltsns.heatmap(    df.select_dtypes(include="number").corr(),    annot=True,    cmap="coolwarm")plt.show()
```

### Important EDA Steps

| Step | What to do                     |
| ---- | ------------------------------ |
| 1    | Load dataset                   |
| 2    | Understand rows and columns    |
| 3    | Check data types               |
| 4    | Check missing values           |
| 5    | Check duplicates               |
| 6    | Statistical analysis           |
| 7    | Univariate analysis            |
| 8    | Bivariate analysis             |
| 9    | Multivariate analysis          |
| 10   | Identify patterns and insights |

### Important Pandas Commands for EDA

```
# First 5 rowsdf.head()# Last 5 rowsdf.tail()# Dataset shapedf.shape# Column namesdf.columns# Dataset informationdf.info()# Statistical summarydf.describe()# Missing valuesdf.isnull().sum()# Duplicate countdf.duplicated().sum()# Unique valuesdf["City"].unique()# Frequency countdf["City"].value_counts()# Correlationdf.corr(numeric_only=True)
```

### Correlation

Correlation measures the strength and direction of a relationship between two numerical variables.

Correlation values range from -1 to +1.

| Value | Meaning                      |
| ----- | ---------------------------- |
| +1    | Perfect positive correlation |
| 0     | No linear correlation        |
| -1    | Perfect negative correlation |

[Correlation Coefficient: What it is, Formulas & Examples](https://images.openai.com/static-rsc-4/31rMp9Ful--M8eTog1g-uAQ0JNUL80WlesJz0mxsG_RZdpjUiOLyjWRu9XMJDuJEtcK8rTTsHnSYuJmChEG7gXb881e_jzPqefhbd0g2SqpGKy5qo4HHdVxpamsh0RU4MMtALh5FIthF3Uy7igZzNa8l3SOPdWtbrrOAkDwM72o?purpose=inline)

[questionpro.com](https://www.questionpro.com/blog/correlation-coefficient/?utm_source=chatgpt.com)

Example:

- More study hours and higher marks: potentially positive correlation.
- Higher price and lower demand: potentially negative correlation.
- Correlation does not prove causation.

### Real-World EDA Example

Suppose you have a student performance dataset containing:

- Student Name
- Age
- Attendance
- Study Hours
- Assignment Marks
- Final Marks

You can investigate:

1. Which student scored highest?
2. Does attendance affect performance?
3. Do study hours relate to final marks?
4. What is the average class performance?
5. Which students need improvement?
6. Are there missing or duplicate records?

This is practical EDA.

## 8. Data Visualization

Very High Priority

### What is Data Visualization?

Definition: Data Visualization is the graphical representation of data using charts, plots, graphs and dashboards.

Hinglish: Numbers ko graphs aur charts mein convert karna, taaki data easily samajh aaye, Data Visualization kehlata hai.

### Why is Data Visualization Important?

- Makes complex data easy to understand.
- Identifies patterns.
- Finds trends.
- Helps compare values.
- Communicates analytical findings.
- Supports decision-making.

### Important Python Libraries

| Library    | Purpose                     |
| ---------- | --------------------------- |
| Matplotlib | Basic and advanced plotting |
| Seaborn    | Statistical visualization   |
| Plotly     | Interactive charts          |
| Pandas     | Basic plotting              |
| Bokeh      | Interactive visualization   |

You have already studied Matplotlib and Seaborn in Phase 02. In Phase 03, focus on using them to solve real data-analysis problems.

### Important Types of Charts

1\. Line Plot

Used to show trends over time.

[Mastering Data Visualization with Python: An End-to-End Guide | by Nayeem Islam | Medium](https://images.openai.com/static-rsc-4/NSrKND9joRcCkH94SpQ5wlW7czCRUMBgOqWPrzts5wskj9lX5aIMzZvhUyPz3qGQVnmlHcW1qoePVGCgNDq1P4vFho5OiJbyAaD2YcyqxwO7uGQuj5AkRS44Jf0RFUwxR14HoCG5w958lnCd096oRshN73TI_rlpXBCk-C9Ns9w?purpose=inline)

[medium.com](https://medium.com/%40nomannayeem/mastering-data-visualization-with-python-an-end-to-end-guide-84334b28087c?utm_source=chatgpt.com)

```
import matplotlib.pyplot as pltmonths = ["Jan", "Feb", "Mar", "Apr"]sales = [100, 150, 120, 200]plt.plot(months, sales, marker="o")plt.title("Monthly Sales")plt.xlabel("Months")plt.ylabel("Sales")plt.show()
```

2\. Bar Chart

Used to compare categories.

[Band 7: The bar chart shows the number of students who like four different school subjects: Math, English, Science, and History. (User-Written IELTS Writing Task 1 Sample)](https://images.openai.com/static-rsc-4/yKKA-sSg2yMtRPqN9kXdPXywbF6YJ-ZqZw_8VBYaGYLx32kROZY-dXCIkG_imlbHFmjKlcaOd6fh-pXm4avUtCLw_3O9cmi35EquCblaNBO0PovRz71pfOL8YxdXaVLZ0Hb53-XwsS6HIplw29FJYa9LifHL6_vMjIdJ8ZJex1g?purpose=inline)

[engnovate.com](https://engnovate.com/ugc-ielts-writing-task-1-essays/the-bar-chart-shows-the-number-of-students-who-like-four-different-school-subjects-math-32d3113507eadd00/?utm_source=chatgpt.com)

```
categories = ["Python", "Java", "C++"]students = [50, 30, 20]plt.bar(categories, students)plt.title("Programming Language Preferences")plt.xlabel("Languages")plt.ylabel("Students")plt.show()
```

3\. Histogram

Used to understand numerical data distribution.

[A teacher has asked all the students in the class which d](https://images.openai.com/static-rsc-4/NSsUG_HSlFS556YYadtNisjY6h8gvGQ17b8szLDonWa1sDPyzpsrqO9TamLTemBrpfE6-FpptQocvBByDDRQqyPAbNLxB8bqwJDVypmySvjvCeVuZwZcltFnmk4NjXH8YauGwtL4eYrED7DeMBSGPgV38KwimFVicC7aK9W3oeI?purpose=inline)

[naxlex.com](https://www.naxlex.com/questions/a-teacher-has-asked-all-the-students-in-the-class-which-days-of-the-week?utm_source=chatgpt.com)

```
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]plt.hist(marks, bins=5)plt.title("Marks Distribution")plt.xlabel("Marks")plt.ylabel("Frequency")plt.show()
```

4\. Scatter Plot

Used to understand relationships between two numerical variables.

[How to Create Scatter Plots in Excel: Step-by-Step Guide (2026)](https://images.openai.com/static-rsc-4/Ra-bPMehcllEjHZhEt3I7zS60oaqa1mkIKHqmatqEAioQEWSgKEfc54FDPphQuAJ89jaP3Erd8OzYnUy_rbqzMELmQdkZ_0JrJTBg4FkcqDZkC7ei68JVPOvCVF4pTu9ItIyagghljXcm7yX4tOyBVZU0KxR2w4AmmUMu-U-uGg?purpose=inline)

[conceptviz.app](https://conceptviz.app/blog/how-to-create-scatter-plot-in-excel-guide?utm_source=chatgpt.com)

```
hours = [1, 2, 3, 4, 5, 6]marks = [30, 40, 50, 60, 75, 90]plt.scatter(hours, marks)plt.xlabel("Study Hours")plt.ylabel("Marks")plt.title("Study Hours vs Marks")plt.show()
```

5\. Box Plot

Used to identify outliers and understand data distribution.

```
sns.boxplot(x=df["Salary"])plt.title("Salary Distribution")plt.show()
```

6\. Heatmap

Used to visualize relationships and correlation between numerical variables.

[Plotting for ML & Data Science | Arman Hossen](https://images.openai.com/static-rsc-4/aK6JoswtRhqfVyFTwkZjODM5SoRPhO77d4TSIPMJw4x0AoiMLVpsC0ygn1dKpdikdwn6Y9RO4w46hnQ-CR_FXRrwnNsCIKpxCeOmK95Sg8rEmqEG1QyX1ASOeihAChvSmTXwDEHnjrOSCRX8IYAnu5KeHNpZpdllD7fqmlnDyNg?purpose=inline)

[armanruet.github.io](https://armanruet.github.io/blog/Plotting-in-machine-learning-reference/?utm_source=chatgpt.com)

```
sns.heatmap(    df.corr(numeric_only=True),    annot=True,    cmap="coolwarm")plt.title("Correlation Heatmap")plt.show()
```

7\. Pie Chart

Used to show proportions of a whole.

```
labels = ["Python", "Java", "C++"]values = [50, 30, 20]plt.pie(    values,    labels=labels,    autopct="%1.1f%%")plt.title("Programming Preferences")plt.show()
```

### Chart Selection Guide

| Your purpose            | Recommended chart |
| ----------------------- | ----------------- |
| Compare categories      | Bar chart         |
| Show time trends        | Line chart        |
| Understand distribution | Histogram         |
| Find outliers           | Box plot          |
| Find relationships      | Scatter plot      |
| Show correlation        | Heatmap           |
| Show proportions        | Pie chart         |

#

My recommendation: Don't just read these notes. Practice every Pandas function in Jupyter Notebook and use at least two real-world CSV datasets.

