#  Complete Pandas Tutorial
### From Beginner to Advanced | Python for AI/ML Engineers

Pandas is one of the most important Python libraries for **Data Analysis, Data Science, Machine Learning, and AI Engineering**.

Since you already know the basics of Python, NumPy, and Pandas, we'll focus on **quick revision of fundamentals, detailed explanations of important concepts, advanced techniques, and practical question-solving**.

By the end of this tutorial, you'll be able to:
- Create and manipulate datasets.
- Read CSV, Excel, and JSON files.
- Clean missing, duplicate, and incorrect data.
- Filter, sort, and modify data.
- Use `groupby()`, `merge()`, `join()`, and `concat()`.
- Perform statistical analysis.
- Handle dates, strings, and categorical data.
- Use advanced Pandas techniques for real-world datasets.
- Prepare datasets for Machine Learning projects.

---

# PHASE 1: Understanding Pandas

## 1. What is Pandas?

**Definition in English:** Pandas is an open-source Python library used for data manipulation, data cleaning, and data analysis.

**EL10 explanation:** Imagine you have the marks of 1,000 students. You want to find the topper, calculate the average marks, identify students who failed, and sort the results.

Doing this manually would take a long time.

Pandas lets you perform these tasks with Python code.

### Example

Suppose you have this dataset:

| Name | Age | Marks |
|---|---:|---:|
| Amir | 20 | 85 |
| Rahul | 21 | 72 |
| Priya | 19 | 95 |
| Neha | 20 | 60 |

You can use Pandas to:
- Find the student with the highest marks.
- Calculate average marks.
- Filter students scoring above 80.
- Sort students by marks.
- Export the results to a CSV file.

### Where is Pandas used?

| Field | Application |
|---|---|
| Data Analysis | Analyze business and student data |
| Machine Learning | Prepare datasets for training |
| AI Engineering | Process structured data |
| Finance | Analyze transactions and financial records |
| Healthcare | Analyze medical datasets |
| Data Science | Discover patterns and trends |

---

## 2. Install and Import Pandas

### Install Pandas

In your terminal, run:

```bash
pip install pandas
```

If you're using Jupyter Notebook, run:

```python
%pip install pandas
```

If Pandas is already installed, you don't need to reinstall it.

### Import Pandas

```python
import pandas as pd
```

Here:
- `import` loads a library.
- `pandas` is the library name.
- `as pd` creates a short alias.

Instead of writing `pandas.DataFrame()`, we can write `pd.DataFrame()`.

**Important:** `pd` is a conventional alias, not a special Python keyword.

---

# PHASE 2: The Two Main Pandas Data Structures

## 3. Series

**Definition:** A Series is a one-dimensional labeled array that can store data of different types.

**EL10 explanation:** Think of a Series as one column in an Excel sheet.

### Example

```python
import pandas as pd

marks = pd.Series([85, 72, 95, 60])

print(marks)
```

Output:

```text
0    85
1    72
2    95
3    60
dtype: int64
```

What do the numbers mean?

- `0, 1, 2, 3` are index labels.
- `85, 72, 95, 60` are the values.
- `int64` indicates an integer data type.

### Create a Series with custom indexes

```python
marks = pd.Series(
    [85, 72, 95],
    index=["Amir", "Rahul", "Priya"]
)

print(marks)
```

Output:

```text
Amir     85
Rahul    72
Priya    95
dtype: int64
```

### Access values

```python
print(marks["Amir"])
print(marks.iloc[0])
```

Both return:

```text
85
```

The difference:

- `marks["Amir"]` accesses a value using its index label.
- `marks.iloc[0]` accesses the first value by position.

### Useful Series operations

```python
marks.sum()
marks.mean()
marks.max()
marks.min()
marks.count()
marks.sort_values()
```

These calculate the sum, average, maximum, minimum, number of non-missing values, and sorted values.

**Remember:** A Series is like a single labeled column.

---

## 4. DataFrame

**Definition:** A DataFrame is a two-dimensional labeled data structure with rows and columns.

**EL10 explanation:** A DataFrame is like an Excel spreadsheet or a database table.

### Create your first DataFrame

```python
import pandas as pd

data = {
    "Name": ["Amir", "Rahul", "Priya", "Neha"],
    "Age": [20, 21, 19, 20],
    "Marks": [85, 72, 95, 60]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Age  Marks
0   Amir   20     85
1  Rahul   21     72
2  Priya   19     95
3   Neha   20     60
```

### Understand the structure

- **Rows:** Individual records.
- **Columns:** Different attributes.
- **Index:** Labels used to identify rows.
- **Values:** The actual data stored in the table.

In this example, each row represents one student.

### Select a column

```python
df["Name"]
```

### Select multiple columns

```python
df[["Name", "Marks"]]
```

### Select a row by position

```python
df.iloc[0]
```

### Select a row by label

```python
df.loc[0]
```

Both return the first row in this example because the index labels are `0, 1, 2, 3`.

**Key difference:**

| Method | Purpose |
|---|---|
| `df["Marks"]` | Select a column |
| `df.loc[0]` | Select a row using its label |
| `df.iloc[0]` | Select a row using its position |

---

# PHASE 3: Exploring a Dataset

## 5. Important DataFrame Attributes and Methods

Before analyzing a dataset, you should understand its structure.

We'll use the following example:

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Amir", "Rahul", "Priya", "Neha", "Aman"],
    "Age": [20, 21, 19, 20, 22],
    "Marks": [85, 72, 95, 60, 88],
    "City": ["Delhi", "Meerut", "Delhi", "Noida", "Meerut"]
})
```

### 5.1 `head()`

Displays the first five rows by default.

```python
df.head()
```

Display the first two rows:

```python
df.head(2)
```

### 5.2 `tail()`

Displays the last five rows by default.

```python
df.tail()
```

### 5.3 `shape`

Returns the number of rows and columns.

```python
df.shape
```

Output:

```text
(5, 4)
```

This means five rows and four columns.

Notice that `shape` is an attribute, so you write `df.shape`, not `df.shape()`.

### 5.4 `columns`

Displays column names.

```python
df.columns
```

### 5.5 `index`

Displays row index labels.

```python
df.index
```

### 5.6 `dtypes`

Displays the data type of each column.

```python
df.dtypes
```

Typical output:

```text
Name     object
Age       int64
Marks     int64
City     object
```

String columns may use `object` or Pandas' dedicated `string` dtype, depending on how they were created.

### 5.7 `info()`

Shows a concise summary of the DataFrame.

```python
df.info()
```

It provides information about:
- Column names.
- Number of non-null values.
- Data types.
- Memory usage.

### 5.8 `describe()`

Provides descriptive statistics for numeric columns.

```python
df.describe()
```

You can obtain statistics such as:
- Count.
- Mean.
- Standard deviation.
- Minimum.
- 25th percentile.
- Median (50th percentile).
- 75th percentile.
- Maximum.

For a general overview that includes non-numeric columns:

```python
df.describe(include="all")
```

### 5.9 `value_counts()`

Counts how frequently each value occurs in a Series.

```python
df["City"].value_counts()
```

Expected counts:

```text
Delhi     2
Meerut    2
Noida     1
```

### 5.10 `nunique()`

Counts the number of distinct, non-missing values.

```python
df["City"].nunique()
```

Output:

```text
3
```

### Quick revision

| Attribute or method | Purpose |
|---|---|
| `head()` | First rows |
| `tail()` | Last rows |
| `shape` | Number of rows and columns |
| `columns` | Column names |
| `index` | Index labels |
| `dtypes` | Column data types |
| `info()` | Structural summary |
| `describe()` | Descriptive statistics |
| `value_counts()` | Frequency of values |
| `nunique()` | Number of unique non-missing values |

---

# PHASE 4: Selecting and Filtering Data

## 6. Selecting Rows and Columns with `loc` and `iloc`

These are among the most important Pandas concepts for interviews and practical work.

### 6.1 `loc[]` — Label-based selection

```python
df.loc[0]
```

Select a particular column from a row:

```python
df.loc[0, "Name"]
```

Output:

```text
Amir
```

Select multiple rows:

```python
df.loc[0:2]
```

**Important:** With ordinary label-based slicing, both endpoints are included when the labels exist.

Select specific rows and columns:

```python
df.loc[0:2, ["Name", "Marks"]]
```

### 6.2 `iloc[]` — Position-based selection

```python
df.iloc[0]
```

Select the first row:

```python
df.iloc[0]
```

Select the first three rows:

```python
df.iloc[0:3]
```

Here, the ending position `3` is excluded.

Select the first two rows and first two columns:

```python
df.iloc[0:2, 0:2]
```

### Difference between `loc` and `iloc`

| Feature | `loc` | `iloc` |
|---|---|---|
| Selection | Index labels | Integer positions |
| Row example | `df.loc[2]` | `df.iloc[2]` |
| Column example | `df.loc[:, "Marks"]` | `df.iloc[:, 2]` |
| Slice endpoint | Usually included | Excluded |

**Interview tip:** If the index contains labels such as `101, 105, 110`, `loc[105]` selects label `105`, while `iloc[1]` selects the second row.

---

## 7. Filtering Data

Filtering means selecting rows that satisfy a condition.

Suppose we have:

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Amir", "Rahul", "Priya", "Neha", "Aman"],
    "Age": [20, 21, 19, 20, 22],
    "Marks": [85, 72, 95, 60, 88],
    "City": ["Delhi", "Meerut", "Delhi", "Noida", "Meerut"]
})
```

### 7.1 Students scoring above 80

```python
df[df["Marks"] > 80]
```

This returns Amir, Priya, and Aman.

### 7.2 Students scoring below 70

```python
df[df["Marks"] < 70]
```

This returns Neha.

### 7.3 Multiple conditions using AND

Find students scoring above 80 who are at least 20 years old.

```python
df[(df["Marks"] > 80) & (df["Age"] >= 20)]
```

### 7.4 Multiple conditions using OR

Find students who live in Delhi or Meerut.

```python
df[(df["City"] == "Delhi") | (df["City"] == "Meerut")]
```

### 7.5 Using `isin()`

Select students from Delhi and Meerut.

```python
df[df["City"].isin(["Delhi", "Meerut"])]
```

### 7.6 Using `between()`

Find students scoring between 70 and 90, inclusive.

```python
df[df["Marks"].between(70, 90)]
```

### 7.7 Using `query()`

```python
df.query("Marks > 80 and Age >= 20")
```

This is another readable way to filter data.

### Important rules

In compound Boolean filters:

- Use `&` for AND.
- Use `|` for OR.
- Use `~` for NOT.
- Put each condition in parentheses.

For example:

```python
df[(df["Marks"] > 70) & (df["Age"] < 22)]
```

Do not use Python's ordinary `and` or `or` directly between Pandas Series conditions.

---

# PHASE 5: Adding, Updating, and Removing Data

## 8. Adding a New Column

Suppose we want to calculate each student's result.

```python
df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)
```

This adds a `Result` column.

However, for simple conditions, `numpy.where()` or Pandas' vectorized operations can be more convenient than `apply()`.

### Example using NumPy

```python
import numpy as np

df["Result"] = np.where(df["Marks"] >= 40, "Pass", "Fail")
```

### Create a column using calculations

Suppose each student receives five bonus marks.

```python
df["Updated_Marks"] = df["Marks"] + 5
```

### Create a percentage column

If the maximum marks are 100:

```python
df["Percentage"] = df["Marks"] / 100 * 100
```

This example produces the same numbers as the `Marks` column because the maximum is 100.

For a maximum of 500:

```python
df["Percentage"] = df["Marks"] / 500 * 100
```

---

## 9. Updating Existing Values

### Update one cell

```python
df.loc[0, "Marks"] = 90
```

This changes Amir's marks from 85 to 90.

### Update multiple rows conditionally

Give five bonus marks to students scoring below 70.

```python
df.loc[df["Marks"] < 70, "Marks"] += 5
```

### Rename columns

```python
df.rename(
    columns={"Marks": "Score"},
    inplace=True
)
```

Now the column previously named `Marks` is called `Score`.

### Rename the index

```python
df.rename(index={0: "Student_1"}, inplace=True)
```

### Delete a column

```python
df.drop(columns=["Age"], inplace=True)
```

### Delete a row by label

```python
df.drop(index=0, inplace=True)
```

**Important:** `inplace=True` modifies the existing DataFrame. Without it, many Pandas operations return a new DataFrame, so you must assign the result if you want to keep it.

For example:

```python
df = df.drop(columns=["Age"])
```

---

# PHASE 6: Sorting and Ranking

## 10. Sorting Data

### Sort by marks in ascending order

```python
df.sort_values(by="Marks")
```

Ascending order means smallest to largest.

### Sort by marks in descending order

```python
df.sort_values(by="Marks", ascending=False)
```

### Sort by multiple columns

First sort by city, then by marks in descending order.

```python
df.sort_values(
    by=["City", "Marks"],
    ascending=[True, False]
)
```

### Sort by index

```python
df.sort_index()
```

### Rank students by marks

```python
df["Rank"] = df["Marks"].rank(
    ascending=False,
    method="dense"
)
```

Higher marks receive better ranks. The `dense` method gives tied values the same rank without leaving gaps afterward.

For example, marks of `95, 90, 90, 80` produce ranks `1, 2, 2, 3`.

---

# PHASE 7: Missing Data Handling

## 11. What Is Missing Data?

Imagine you have the following dataset:

| Name | Age | Marks |
|---|---:|---:|
| Amir | 20 | 85 |
| Rahul | 21 | NaN |
| Priya | NaN | 95 |
| Neha | 20 | 60 |

`NaN` represents a missing numerical value in this example.

Missing values can cause problems during analysis and machine learning. Pandas provides tools to identify and handle them.

### 11.1 Detect missing values

```python
df.isna()
```

Returns `True` wherever a value is missing.

### 11.2 Count missing values per column

```python
df.isna().sum()
```

### 11.3 Check whether any value is missing

```python
df.isna().any()
```

### 11.4 Remove rows containing missing values

```python
df.dropna()
```

By default, this removes rows containing at least one missing value.

### 11.5 Remove columns containing missing values

```python
df.dropna(axis=1)
```

### 11.6 Fill missing values with a fixed number

```python
df["Marks"] = df["Marks"].fillna(0)
```

### 11.7 Fill missing values with the mean

```python
df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)
```

### 11.8 Fill missing values with the median

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

### 11.9 Forward fill

```python
df.ffill()
```

Fills missing values using the previous valid value along the selected direction.

### 11.10 Backward fill

```python
df.bfill()
```

Fills missing values using the next valid value.

### Which method should you use?

| Situation | Possible approach |
|---|---|
| Very few incomplete rows | Consider `dropna()` |
| Numerical data with roughly symmetric distribution | Mean imputation may work |
| Numerical data with strong outliers | Median imputation may be preferable |
| Sequential data | Forward/backward fill may be appropriate |
| Missing values represent an unknown category | Consider an explicit `"Unknown"` category |

**AI/ML warning:** Do not automatically replace all missing values with zero. Zero may be a real measurement, not a missing value.

When preparing training and test datasets, fit imputation rules on the training data only, then apply those rules to validation/test data to avoid data leakage.

For the full guide, see the official [Pandas User Guide: Missing Data](https://pandas.pydata.org/docs/user_guide/missing_data.html?utm_source=chatgpt.com).

---

# PHASE 8: Duplicate Data and Data Cleaning

## 12. Detect and Remove Duplicates

Suppose your dataset contains the same student twice.

```python
df = pd.DataFrame({
    "Name": ["Amir", "Rahul", "Amir", "Priya"],
    "Marks": [85, 72, 85, 95]
})
```

### Check duplicate rows

```python
df.duplicated()
```

This returns a Boolean Series indicating which rows duplicate an earlier row.

### Count duplicate rows

```python
df.duplicated().sum()
```

### Remove duplicate rows

```python
df.drop_duplicates()
```

### Remove duplicates based on a specific column

```python
df.drop_duplicates(subset=["Name"])
```

This keeps the first occurrence of each name by default.

### Keep the last occurrence

```python
df.drop_duplicates(
    subset=["Name"],
    keep="last"
)
```

### Remove every occurrence of duplicated names

```python
df.drop_duplicates(
    subset=["Name"],
    keep=False
)
```

**Real-world example:** In a sales dataset, you might identify duplicate transactions using a transaction ID rather than comparing every column.

**Important:** Before deleting duplicates, determine what makes a record genuinely duplicate. Two transactions with the same customer and amount may still be different transactions.

---

## 13. Cleaning Text Data

Real-world data is often messy.

For example:

```python
df = pd.DataFrame({
    "Name": [" Amir ", "RAHUL", " priya", "Neha "],
    "City": ["Delhi", "delhi", "MEERUT", "Meerut"]
})
```

Notice the extra spaces and inconsistent capitalization.

### Remove leading and trailing spaces

```python
df["Name"] = df["Name"].str.strip()
```

### Convert text to lowercase

```python
df["Name"] = df["Name"].str.lower()
```

### Convert text to uppercase

```python
df["Name"] = df["Name"].str.upper()
```

### Convert text to title case

```python
df["Name"] = df["Name"].str.title()
```

### Replace text

```python
df["City"] = df["City"].str.replace(
    "delhi",
    "Delhi",
    case=False,
    regex=False
)
```

### Check whether text contains a word

```python
df["City"].str.contains(
    "delhi",
    case=False,
    na=False
)
```

### Check whether a string starts with a particular letter

```python
df["Name"].str.startswith("A", na=False)
```

### Check whether a string ends with a particular letter

```python
df["Name"].str.endswith("a", na=False)
```

### Extract part of a string

```python
df["Name"].str[:3]
```

This extracts the first three characters of each name.

### Replace multiple spaces

```python
df["Name"] = df["Name"].str.replace(
    r"\s+",
    " ",
    regex=True
).str.strip()
```

Here, `\s+` matches one or more whitespace characters.

**Remember:** The `.str` accessor lets you apply string operations to an entire Series without manually looping over every row.

---

# PHASE 9: Data Type Conversion

## 14. Understanding Data Types

Pandas commonly works with:

| Data type | Example |
|---|---|
| Integer | `20` |
| Float | `85.5` |
| String | `"Amir"` |
| Boolean | `True` |
| Datetime | `2026-10-31` |
| Category | `"Delhi"` |

### Convert a column to integer

```python
df["Age"] = df["Age"].astype("int64")
```

Only do this when the values can safely be represented as integers.

### Convert a column to string

```python
df["Name"] = df["Name"].astype("string")
```

### Convert text containing numbers to numeric data

```python
df = pd.DataFrame({
    "Marks": ["85", "72", "95", "Unknown"]
})

df["Marks"] = pd.to_numeric(
    df["Marks"],
    errors="coerce"
)
```

Result:

```text
85.0
72.0
95.0
NaN
```

`errors="coerce"` converts values that cannot be parsed into missing values.

### Convert a column to datetime

```python
df = pd.DataFrame({
    "Date": ["2026-01-10", "2026-02-15"]
})

df["Date"] = pd.to_datetime(df["Date"])
```

### Why data types matter

Suppose marks are stored as strings:

```python
["10", "20", "100"]
```

Sorting these as text can produce an order different from numeric sorting.

Correct numeric conversion ensures calculations and comparisons work as intended.

---

# PHASE 10: Mathematical and Statistical Operations

## 15. Basic Statistics

Let's create a dataset:

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Amir", "Rahul", "Priya", "Neha"],
    "Marks": [85, 72, 95, 60],
    "Age": [20, 21, 19, 20]
})
```

### Sum

```python
df["Marks"].sum()
```

Output:

```text
312
```

### Mean

```python
df["Marks"].mean()
```

Output:

```text
78.0
```

### Median

```python
df["Marks"].median()
```

Output:

```text
78.5
```

### Maximum and minimum

```python
df["Marks"].max()
df["Marks"].min()
```

### Standard deviation

```python
df["Marks"].std()
```

Measures how spread out the values are. By default, Pandas uses the sample standard deviation (`ddof=1`).

### Variance

```python
df["Marks"].var()
```

Variance measures squared deviations from the mean.

### Count non-missing values

```python
df["Marks"].count()
```

### Correlation

```python
df[["Marks", "Age"]].corr()
```

Correlation measures the strength and direction of a linear relationship between numerical variables.

Its values range from -1 to +1.

- Close to +1: strong positive linear relationship.
- Close to -1: strong negative linear relationship.
- Close to 0: little or no linear relationship.

**Important:** Correlation does not prove causation.

### Cumulative sum

```python
df["Cumulative_Marks"] = df["Marks"].cumsum()
```

### Difference between consecutive values

```python
df["Marks_Difference"] = df["Marks"].diff()
```

### Percentage change

```python
df["Marks_Change"] = df["Marks"].pct_change() * 100
```

This calculates percentage change relative to the previous row. It is useful for ordered time-series data, but you should sort the data correctly first.

---

# PHASE 11: Grouping and Aggregation

## 16. Master `groupby()`

**Definition:** `groupby()` splits data into groups, applies calculations to each group, and combines the results.

Think of it as dividing students by city and calculating the average marks of each city.

### Create the dataset

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Amir", "Rahul", "Priya", "Neha", "Aman"],
    "City": ["Delhi", "Meerut", "Delhi", "Noida", "Meerut"],
    "Marks": [85, 72, 95, 60, 88],
    "Age": [20, 21, 19, 20, 22]
})
```

### Average marks by city

```python
df.groupby("City")["Marks"].mean()
```

Expected results:

| City | Average marks |
|---|---:|
| Delhi | 90 |
| Meerut | 80 |
| Noida | 60 |

### Sum by group

```python
df.groupby("City")["Marks"].sum()
```

### Count records per group

```python
df.groupby("City").size()
```

### Calculate multiple statistics

```python
df.groupby("City")["Marks"].agg(
    ["mean", "max", "min", "count"]
)
```

### Group by multiple columns

```python
df.groupby(["City", "Age"])["Marks"].mean()
```

This creates groups using both city and age.

### Aggregate multiple columns

```python
df.groupby("City").agg({
    "Marks": ["mean", "max"],
    "Age": "mean"
})
```

### Keep group names as ordinary columns

```python
df.groupby(
    "City",
    as_index=False
)["Marks"].mean()
```

### Filter groups

Suppose you want only cities whose average marks exceed 75.

```python
df.groupby("City").filter(
    lambda group: group["Marks"].mean() > 75
)
```

This returns the original student rows belonging to qualifying cities.

### `agg()` vs. `transform()` vs. `filter()`

| Method | What it does |
|---|---|
| `agg()` | Calculates summary statistics for each group |
| `transform()` | Returns results aligned with the original rows |
| `filter()` | Keeps or removes entire groups based on a condition |

Example of `transform()`:

```python
df["City_Average"] = (
    df.groupby("City")["Marks"].transform("mean")
)
```

Each student receives the average marks of their city.

This is particularly useful when creating features for data analysis or machine learning.

---

# PHASE 12: Combining Multiple DataFrames

## 17. `concat()`, `merge()`, and `join()`

These three operations are essential when working with real-world datasets.

### 17.1 `concat()` — Combine tables along an axis

Imagine you have January and February sales in separate tables.

```python
jan = pd.DataFrame({
    "Name": ["Amir", "Rahul"],
    "Marks": [85, 72]
})

feb = pd.DataFrame({
    "Name": ["Priya", "Neha"],
    "Marks": [95, 60]
})
```

Combine them vertically:

```python
result = pd.concat(
    [jan, feb],
    ignore_index=True
)
```

`ignore_index=True` creates a fresh sequential index.

Combine tables horizontally:

```python
result = pd.concat(
    [jan, feb],
    axis=1
)
```

Horizontal concatenation aligns rows by index, so it does not necessarily match records by name.

### 17.2 `merge()` — Combine using a common key

Imagine two database tables.

**Students:**

| ID | Name |
|---:|---|
| 1 | Amir |
| 2 | Mohit |
| 3 | Pushpa |

**Marks:**

| ID | Marks |
|---:|---:|
| 1 | 97 |
| 2 | 89 |
| 3 | 95 |

Code:

```python
students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amir", "Rahul", "Priya"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [97, 89, 95]
})

result = pd.merge(
    students,
    marks,
    on="ID",
    how="inner"
)
```

Output:

| ID | Name | Marks |
|---:|---|---:|
| 1 | Amir | 97 |
| 2 | Mohit | 89 |
| 3 | Pushpa | 95 |

### Types of merge

| Type | Meaning |
|---|---|
| `inner` | Keep matching keys from both tables |
| `left` | Keep every key from the left table |
| `right` | Keep every key from the right table |
| `outer` | Keep keys from both tables |
| `cross` | Produce all combinations of rows |

Example:

```python
pd.merge(
    students,
    marks,
    on="ID",
    how="left"
)
```

A left merge retains every student, even if that student has no matching marks record.

### Merge using different column names

```python
pd.merge(
    students,
    marks,
    left_on="ID",
    right_on="ID"
)
```

Use `left_on` and `right_on` when the matching key columns have different names.

### Validate relationships

If each student should have exactly one record in the marks table:

```python
pd.merge(
    students,
    marks,
    on="ID",
    validate="one_to_one"
)
```

This raises an error if the keys violate the expected one-to-one relationship.

Validation is particularly useful for catching unexpected duplicate keys.

### 17.3 `join()` — Commonly join using indexes

```python
left = pd.DataFrame(
    {"Name": ["Amir", "Mohit"]},
    index=[1, 2]
)

right = pd.DataFrame(
    {"Marks": [97, 89]},
    index=[1, 2]
)

result = left.join(right)
```

This combines the tables using their index labels by default.

**Easy memory trick:**
- `concat()` → Stack or align tables.
- `merge()` → Match records using key columns.
- `join()` → Commonly combine tables using indexes.

For more detail, see the official [Pandas guide to combining tables](https://pandas.pydata.org/docs/user_guide/merging.html?utm_source=chatgpt.com).

---

# PHASE 13: Reading and Writing Files

## 18. Importing CSV Files

CSV stands for **Comma-Separated Values**. It is a common format for storing tabular data.

Suppose your file is named `students.csv`.

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
```

### Important CSV options

**Read only specific columns:**

```python
df = pd.read_csv(
    "students.csv",
    usecols=["Name", "Marks"]
)
```

**Read only the first 100 rows:**

```python
df = pd.read_csv("students.csv", nrows=100)
```

**Treat a particular value as missing:**

```python
df = pd.read_csv(
    "students.csv",
    na_values=["NA", "Unknown", "-"]
)
```

**Read a CSV file with a different separator:**

```python
df = pd.read_csv(
    "students.csv",
    sep=";"
)
```

**Specify a column's data type:**

```python
df = pd.read_csv(
    "students.csv",
    dtype={"Name": "string"}
)
```

## 19. Read and Write Excel Files

Read an Excel file:

```python
df = pd.read_excel("students.xlsx")
```

Read a specific sheet:

```python
df = pd.read_excel(
    "students.xlsx",
    sheet_name="Sheet1"
)
```

Write to Excel:

```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

You may need an Excel engine such as `openpyxl`:

```python
%pip install openpyxl
```

## 20. Read and Write JSON Files

Read JSON:

```python
df = pd.read_json("students.json")
```

Write JSON:

```python
df.to_json(
    "output.json",
    orient="records",
    indent=2
)
```

## 21. Read and Write SQL Data

Pandas can read SQL query results using a database connection.

For example, with a SQLite database:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("college.db")

df = pd.read_sql_query(
    "SELECT * FROM students",
    conn
)

conn.close()
```

**Security tip:** When SQL queries include user-supplied values, use parameterized queries rather than building SQL strings through concatenation.

## 22. Export to CSV

```python
df.to_csv(
    "cleaned_data.csv",
    index=False
)
```

`index=False` prevents Pandas from writing the DataFrame's index as an additional column.

### File handling cheat sheet

| Task | Function |
|---|---|
| Read CSV | `pd.read_csv()` |
| Write CSV | `df.to_csv()` |
| Read Excel | `pd.read_excel()` |
| Write Excel | `df.to_excel()` |
| Read JSON | `pd.read_json()` |
| Write JSON | `df.to_json()` |
| Read SQL | `pd.read_sql_query()` |
| Inspect file | `df.head()` |

The official documentation covers supported formats, import options, and export options: [Pandas Input/Output Guide](https://pandas.pydata.org/docs/user_guide/io.html?utm_source=chatgpt.com).

---

# PHASE 14: Reshaping Data

## 23. What Is Reshaping?

Sometimes the same information can be represented in different table structures.

Pandas provides functions such as `pivot()`, `pivot_table()`, `melt()`, and `crosstab()` to reshape or summarize data. [Pandas](https://pandas.pydata.org/docs/user_guide/?utm_source=chatgpt.com)

### 23.1 `pivot()`

Imagine this dataset:

```python
df = pd.DataFrame({
    "Name": ["Amir", "Amir", "Mohit", "Mohit"],
    "Subject": ["Math", "Science", "Math", "Science"],
    "Marks": [97, 90, 89, 80]
})
```

Convert subjects into columns:

```python
wide = df.pivot(
    index="Name",
    columns="Subject",
    values="Marks"
)
```

Result:

| Name | Math | Science |
|---|---:|---:|
| Amir | 97 | 90 |
| Rahul | 89| 80 |

**Important:** `pivot()` requires the combination of the selected index and column values to identify a unique value. If duplicates exist, use `pivot_table()` or aggregate the data first.

### 23.2 `pivot_table()`

Calculate average marks for each student and subject:

```python
table = df.pivot_table(
    index="Name",
    columns="Subject",
    values="Marks",
    aggfunc="mean"
)
```

Unlike `pivot()`, `pivot_table()` can aggregate duplicate combinations.

### 23.3 `melt()`

Convert a wide table into a long table.

```python
wide = pd.DataFrame({
    "Name": ["Amir", "Mohit"],
    "Math": [97, 89],
    "Science": [90, 80]
})

long = wide.melt(
    id_vars="Name",
    var_name="Subject",
    value_name="Marks"
)
```

Result:

| Name | Subject | Marks |
|---|---|---:|
| Amir | Math | 97 |
| Rahul | Math | 89 |
| Amir | Science | 90 |
| Rahul | Science | 80 |

### 23.4 `crosstab()`

Count how frequently categories occur together.

```python
pd.crosstab(
    df["Name"],
    df["Subject"]
)
```

### When should you use each?

| Function | Purpose |
|---|---|
| `pivot()` | Restructure unique combinations |
| `pivot_table()` | Restructure and aggregate data |
| `melt()` | Convert wide data into long data |
| `crosstab()` | Create frequency tables |

---

# PHASE 15: Date and Time Operations

## 24. Working with Dates

Date operations are useful in sales analysis, stock data, attendance systems, and time-series forecasting.

### Create a DataFrame

```python
df = pd.DataFrame({
    "Date": [
        "2026-01-10",
        "2026-02-15",
        "2026-03-20"
    ],
    "Sales": [1000, 1500, 2000]
})
```

### Convert strings to datetime

```python
df["Date"] = pd.to_datetime(df["Date"])
```

### Extract year

```python
df["Year"] = df["Date"].dt.year
```

### Extract month

```python
df["Month"] = df["Date"].dt.month
```

### Extract day

```python
df["Day"] = df["Date"].dt.day
```

### Extract weekday

```python
df["Weekday"] = df["Date"].dt.day_name()
```

### Filter records after a particular date

```python
df[df["Date"] >= "2026-02-01"]
```

### Group sales by month

```python
monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Sales"]
    .sum()
)
```

### Generate a date range

```python
dates = pd.date_range(
    start="2026-01-01",
    periods=7,
    freq="D"
)
```

This creates seven consecutive daily dates.

### Resample time-series data

If a DataFrame has a datetime index:

```python
df = df.set_index("Date")

monthly_sales = df["Sales"].resample("MS").sum()
```

`MS` means month start. Each monthly group is labeled at the start of its month.

**Important:** Before resampling, ensure your data is properly converted to datetime and has an appropriate datetime index.

---

# PHASE 16: Categorical Data and Conditional Logic

## 25. Categorical Data

Suppose a dataset contains a column with values such as:

```text
Low, Medium, High
```

These are categories rather than continuous measurements.

### Convert a column to category

```python
df["Priority"] = df["Priority"].astype("category")
```

### Create an ordered category

```python
df["Priority"] = pd.Categorical(
    df["Priority"],
    categories=["Low", "Medium", "High"],
    ordered=True
)
```

Now Pandas knows the intended order of the categories.

This can help when sorting priority levels.

### Conditional values with `where()`

```python
df["Result"] = df["Marks"].where(
    df["Marks"] >= 40,
    "Fail"
)
```

This retains marks for qualifying rows and substitutes `"Fail"` otherwise. Depending on the column's dtype, mixed numeric and string values may require an appropriate common dtype.

For straightforward pass/fail classification, `np.where()` is often clearer.

### Multiple conditions with `np.select()`

```python
import numpy as np

conditions = [
    df["Marks"] >= 90,
    df["Marks"] >= 75,
    df["Marks"] >= 40
]

choices = ["Excellent", "Good", "Pass"]

df["Grade"] = np.select(
    conditions,
    choices,
    default="Fail"
)
```

The conditions are evaluated in order, so the first matching condition determines the result.

---

# PHASE 17: Advanced Pandas

## 26. The `apply()` Method

`apply()` applies a function to a Series or along a DataFrame axis.

### Apply a function to a column

```python
df["Marks_Doubled"] = df["Marks"].apply(
    lambda x: x * 2
)
```

### Apply a function row by row

```python
df["Total"] = df.apply(
    lambda row: row["Math"] + row["Science"],
    axis=1
)
```

Here, `axis=1` means that the function operates on each row.

For simple arithmetic, vectorized operations are usually preferable:

```python
df["Total"] = df["Math"] + df["Science"]
```

### When should you use `apply()`?

Use it when a transformation is difficult to express with built-in operations or vectorized calculations.

Avoid using it automatically for every calculation. Built-in Pandas and NumPy operations are often faster and easier to read.

---

## 27. `map()` vs. `apply()` vs. `replace()`

Suppose:

```python
df = pd.DataFrame({
    "City_Code": [1, 2, 3, 1]
})
```

### `map()` — Map values in a Series

```python
city_map = {
    1: "Delhi",
    2: "Meerut",
    3: "Noida"
}

df["City"] = df["City_Code"].map(city_map)
```

### `apply()` — Apply a function

```python
df["City_Code_Doubled"] = (
    df["City_Code"].apply(lambda x: x * 2)
)
```

### `replace()` — Replace specified values

```python
df["City_Code"] = df["City_Code"].replace({
    1: 100,
    2: 200
})
```

### Difference

| Method | Typical use |
|---|---|
| `map()` | Mapping or transforming Series values |
| `apply()` | Applying a function to Series or DataFrame axes |
| `replace()` | Replacing specified values or patterns |

---

## 28. MultiIndex

A MultiIndex is a hierarchical index with multiple levels.

For example:

```python
df = pd.DataFrame({
    "City": ["Delhi", "Delhi", "Meerut", "Meerut"],
    "Year": [2025, 2026, 2025, 2026],
    "Sales": [100, 150, 80, 120]
})
```

Create a MultiIndex:

```python
indexed = df.set_index(["City", "Year"])
```

The index now has two levels: `City` and `Year`.

Select data for Delhi:

```python
indexed.loc["Delhi"]
```

Restore the index to ordinary columns:

```python
indexed.reset_index()
```

**When is it useful?** MultiIndex is helpful for hierarchical summaries, grouped time-series data, and tables with multiple levels of identification.

---

## 29. Rolling and Expanding Calculations

These operations are useful in financial analysis, forecasting, and time-series data.

### Rolling average

```python
df["Rolling_Average"] = (
    df["Sales"].rolling(window=3).mean()
)
```

This calculates the average over each three-row window.

The first two rows will be missing by default because a complete three-row window is not yet available.

### Expanding average

```python
df["Expanding_Average"] = (
    df["Sales"].expanding().mean()
)
```

This calculates the average using all observations from the beginning through the current row.

### Exponentially weighted average

```python
df["EWMA"] = (
    df["Sales"].ewm(span=3, adjust=False).mean()
)
```

Recent observations receive greater weight than older ones.

**Important:** If these operations represent time, sort the dataset chronologically before calculating them.

---

## 30. Memory and Performance Optimization

This is an important topic for an AI/ML engineer.

### 30.1 Avoid unnecessary row loops

Less efficient for large datasets:

```python
for i in range(len(df)):
    df.loc[i, "Double"] = df.loc[i, "Marks"] * 2
```

Better:

```python
df["Double"] = df["Marks"] * 2
```

### 30.2 Use appropriate data types

```python
df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce",
    downcast="integer"
)
```

Downcasting may reduce memory use when the values fit within a smaller numeric type.

### 30.3 Use categorical types for repeated labels

```python
df["City"] = df["City"].astype("category")
```

This can reduce memory usage when a column contains a small number of repeated categories.

### 30.4 Read large CSV files in chunks

```python
for chunk in pd.read_csv(
    "large_dataset.csv",
    chunksize=10000
):
    print(chunk.shape)
```

This processes the file in chunks of up to 10,000 rows rather than loading the entire file into one DataFrame.

### 30.5 Check memory usage

```python
df.memory_usage(deep=True)
```

For total DataFrame memory usage:

```python
df.memory_usage(deep=True).sum()
```

These techniques help you write more efficient data-processing code.

---

# PHASE 18: Pandas for AI/ML Engineers 

This phase is especially important for your goal of becoming an AI/ML engineer.

In Machine Learning, you generally don't give raw, messy data directly to a model. You first inspect, clean, transform, and prepare the dataset.

## 31. Complete Data Preprocessing Example

Let's create a realistic student dataset.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Amir", "Rahul", "Priya", "Neha", "Aman", "Rahul"],
    "Age": [20, 21, 19, np.nan, 22, 21],
    "Study_Hours": [4, 2, 6, 3, np.nan, 2],
    "Attendance": [90, 65, 95, 70, 85, 65],
    "Marks": [85, 55, 98, 60, 88, 55]
})

print(df)
```

### Step 1: Understand the dataset

```python
df.head()
df.shape
df.info()
df.describe()
```

### Step 2: Check missing values

```python
df.isna().sum()
```

### Step 3: Remove duplicate records

```python
df = df.drop_duplicates()
```

This removes exact duplicate rows. In a real dataset, first determine which columns define a duplicate record.

### Step 4: Handle missing numerical values

```python
df["Age"] = df["Age"].fillna(df["Age"].median())

df["Study_Hours"] = df["Study_Hours"].fillna(
    df["Study_Hours"].median()
)
```

For a real ML workflow, calculate these medians using the training dataset only.

### Step 5: Create a new feature

```python
df["Study_Efficiency"] = (
    df["Marks"] / df["Study_Hours"]
)
```

This creates a new feature representing marks per study hour.

Note that this is a simple illustrative feature, not necessarily a reliable measure of learning efficiency.

### Step 6: Create a target variable

```python
df["Result"] = np.where(
    df["Marks"] >= 40,
    "Pass",
    "Fail"
)
```

The target is what a supervised ML model might try to predict.

### Step 7: Separate features and target

```python
X = df[[
    "Age",
    "Study_Hours",
    "Attendance"
]]

y = df["Marks"]
```

Here:
- `X` contains the input features.
- `y` contains the target variable.

### Step 8: Split the data

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

This creates training and testing subsets.

**Important:** For a proper ML pipeline, split the data before learning imputation statistics or other transformations from it. Use a Scikit-learn `Pipeline` with suitable preprocessing to help prevent data leakage.

Also, if you are predicting marks, do not include `Marks` itself—or a feature calculated directly from it—in `X`. That would leak the answer into the model.

Official resources: [Scikit-learn Preprocessing Guide](https://scikit-learn.org/stable/modules/preprocessing.html?utm_source=chatgpt.com).

---

# PHASE 19: Pandas Visualization

## 32. Create Charts Using Pandas

Pandas supports plotting through Matplotlib.

First, import the library:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

### Bar chart

Compare marks among students.

```python
df.plot(
    x="Name",
    y="Marks",
    kind="bar"
)

plt.tight_layout()
plt.show()
```

### Line chart

Show how sales change over time.

```python
sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [100, 150, 120, 200]
})

sales.plot(
    x="Month",
    y="Sales",
    kind="line",
    marker="o"
)

plt.tight_layout()
plt.show()
```

### Histogram

Understand the distribution of marks.

```python
df["Marks"].plot(kind="hist", bins=10)

plt.show()
```

### Scatter plot

Examine the relationship between study hours and marks.

```python
df.plot(
    x="Study_Hours",
    y="Marks",
    kind="scatter"
)

plt.show()
```

### Common plot types

| Chart | Purpose |
|---|---|
| `bar` | Compare categories |
| `line` | Show trends |
| `hist` | Examine distributions |
| `scatter` | Examine relationships between two numerical variables |
| `box` | Examine distributions and potential outliers |
| `area` | Show cumulative or changing quantities |

---

# PHASE 20: Complete Pandas Revision Cheat Sheet

## 33. Most Important Commands

Save this section for quick revision.

| Task | Pandas command |
|---|---|
| Import library | `import pandas as pd` |
| Create DataFrame | `pd.DataFrame(data)` |
| Create Series | `pd.Series(data)` |
| Read CSV | `pd.read_csv("file.csv")` |
| Read Excel | `pd.read_excel("file.xlsx")` |
| Export CSV | `df.to_csv("file.csv", index=False)` |
| First rows | `df.head()` |
| Last rows | `df.tail()` |
| Dimensions | `df.shape` |
| Column names | `df.columns` |
| Data types | `df.dtypes` |
| Dataset summary | `df.info()` |
| Statistical summary | `df.describe()` |
| Select column | `df["Name"]` |
| Select columns | `df[["Name", "Marks"]]` |
| Select by label | `df.loc[0]` |
| Select by position | `df.iloc[0]` |
| Filter rows | `df[df["Marks"] > 80]` |
| Count missing values | `df.isna().sum()` |
| Remove missing rows | `df.dropna()` |
| Fill missing values | `df.fillna(0)` |
| Check duplicates | `df.duplicated()` |
| Remove duplicates | `df.drop_duplicates()` |
| Sort data | `df.sort_values("Marks")` |
| Count unique values | `df["City"].nunique()` |
| Count category frequency | `df["City"].value_counts()` |
| Group data | `df.groupby("City")` |
| Calculate average | `df["Marks"].mean()` |
| Calculate median | `df["Marks"].median()` |
| Combine tables | `pd.concat([df1, df2])` |
| Merge tables | `pd.merge(df1, df2, on="ID")` |
| Join tables | `df1.join(df2)` |
| Reshape data | `df.melt()` |
| Create pivot table | `df.pivot_table(...)` |
| Convert to datetime | `pd.to_datetime(df["Date"])` |
| Rename columns | `df.rename(columns={"Old": "New"})` |
| Delete column | `df.drop(columns=["Age"])` |
| Map values | `df["City"].map(mapping)` |
| Apply a function | `df["Marks"].apply(function)` |
| Check memory | `df.memory_usage(deep=True)` |

---

# PHASE 21: Common Pandas Mistakes

## 34. Mistakes You Should Avoid

### Mistake 1: Using `and` instead of `&`

Incorrect:

```python
df[(df["Age"] > 18) and (df["Marks"] > 80)]
```

Correct:

```python
df[(df["Age"] > 18) & (df["Marks"] > 80)]
```

### Mistake 2: Forgetting to save the result

```python
df.dropna()
```

This returns a cleaned DataFrame but does not, by itself, replace `df`.

Use:

```python
df = df.dropna()
```

Alternatively, assign the result to another variable.

### Mistake 3: Confusing `loc` and `iloc`

- `loc` uses labels.
- `iloc` uses integer positions.

### Mistake 4: Treating missing values as ordinary values

Incorrect:

```python
df[df["Marks"] == np.nan]
```

Correct:

```python
df[df["Marks"].isna()]
```

### Mistake 5: Using loops for every calculation

Instead of:

```python
for i in range(len(df)):
    df.loc[i, "Double"] = df.loc[i, "Marks"] * 2
```

Prefer:

```python
df["Double"] = df["Marks"] * 2
```

### Mistake 6: Ignoring duplicate keys when merging

Duplicate keys can multiply rows in a merge and unexpectedly change your totals.

Check the relevant key columns and use `validate=` when you know the expected relationship.

### Mistake 7: Data leakage in Machine Learning

Do not calculate preprocessing statistics from the complete dataset before splitting it into training and testing data.

Fit transformations on training data and apply them to the test data.

---

# PHASE 22: Practical Exercises — Beginner to Advanced

Since your Pandas fundamentals are already familiar, use these exercises to test whether you can apply them without looking at the answers.

Create this dataset first:

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": [
        "Amir", "Rahul", "Priya", "Neha",
        "Aman", "Sara", "Vikram", "Rahul"
    ],
    "Age": [20, 21, 19, np.nan, 22, 20, 23, 21],
    "City": [
        "Delhi", "Meerut", "Delhi", "Noida",
        "Meerut", "Delhi", "Noida", "Meerut"
    ],
    "Marks": [85, 72, 95, 60, 88, 91, 67, 72],
    "Study_Hours": [4, 3, 6, 2, 5, 5, 2, 3]
})
```


---

# PHASE 23: Mini Project — Student Performance Analysis

## 35. Build Your First Pandas Project

**Project name:** Student Performance Data Analyzer

### Objective

Build a Python program that reads student records, cleans the dataset, analyzes performance, and exports the results.

### Required features

1. Read student records from a CSV file.
2. Display dataset information and statistical summaries.
3. Identify missing values and duplicate records.
4. Clean missing and inconsistent data.
5. Calculate average marks.
6. Identify the highest-scoring student.
7. Calculate city-wise average marks.
8. Create a pass/fail column.
9. Rank students by marks.
10. Generate a chart comparing student marks.
11. Export the cleaned data to a new CSV file.

### Suggested project structure

```text
Student_Performance_Analyzer/
│
├── data/
│   └── students.csv
│
├── output/
│   └── cleaned_students.csv
│
├── main.py
└── README.md
```

### What should you learn from this project?

By completing it, you practise:

- File handling.
- Data exploration.
- Data cleaning.
- Boolean filtering.
- Grouping and aggregation.
- Data visualization.
- Exporting results.

**Completion target:** The project should run from beginning to end on a real CSV file, handle missing data appropriately, generate correct results, and include a README explaining how to run it.

Do not stop at writing the code. Test it with incomplete data, duplicate rows, and unexpected text values.

---

# PHASE 24: Your Pandas Learning Roadmap

Because you already know the basics of Pandas, you should focus on revision and practical implementation rather than starting from zero.

| Phase | Topics | Suggested time |
|---|---|---:|
| 1 | Series, DataFrames, indexing | 1 hour |
| 2 | Filtering, sorting, conditional logic | 1–2 hours |
| 3 | Missing values, duplicates, data types | 1–2 hours |
| 4 | Statistics, `groupby()`, aggregation | 1–2 hours |
| 5 | `merge()`, `join()`, `concat()` | 1–2 hours |
| 6 | CSV, Excel, JSON, SQL | 1 hour |
| 7 | Reshaping, dates, string operations | 1–2 hours |
| 8 | Advanced operations and optimization | 2 hours |
| 9 | Practical questions and mini project | 3–5 hours |

These are approximate study times for revision and practice, not guaranteed completion times. Adjust them according to how easily you solve the exercises.

## Your final checklist

Before moving on to the next AI/ML topic, make sure you can do the following without copying code:

- [ ] Create and inspect a DataFrame.
- [ ] Select rows and columns using `loc` and `iloc`.
- [ ] Filter data using multiple conditions.
- [ ] Handle missing values and duplicates.
- [ ] Clean text and convert data types.
- [ ] Calculate descriptive statistics.
- [ ] Use `groupby()` and `agg()`.
- [ ] Combine tables using `merge()`, `join()`, and `concat()`.
- [ ] Read and export CSV files.
- [ ] Reshape data with `pivot_table()` and `melt()`.
- [ ] Process date and time columns.
- [ ] Prepare a dataset for Machine Learning without data leakage.
- [ ] Complete the Student Performance Analyzer project.

### Best official resources

1. [Pandas Getting Started](https://pandas.pydata.org/docs/getting_started/?utm_source=chatgpt.com) — Tutorials and introductory concepts.
2. [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html?utm_source=chatgpt.com) — Quick revision.
3. [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/?utm_source=chatgpt.com) — Detailed reference for advanced topics.

---

## My recommendation for you

Since you have already studied Python, NumPy, and Pandas, **don't spend days repeatedly reading basic definitions**. Revise each topic, practise coding questions, and build the mini project. Pay particular attention to data cleaning, grouping, merging, and ML preprocessing because these skills are used extensively in data analysis and model development.




