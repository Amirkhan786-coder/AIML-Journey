# PHASE 02 — PYTHON FOR DATA



Complete Detailed Notes

B.Tech CS – AI & ML

Beginner to Advanced



This phase is one of the most important phases in your AI/ML journey. You will learn how to collect, process, clean, analyze, and visualize data using Python.

Main objective: By completing Phase 02, you should be able to take raw data, process it, analyze it, visualize it, and prepare it for Machine Learning.

## 1. Complete Phase 02 syllabus

| No. | Topic        | Required level        |
| --- | ------------ | --------------------- |
| 1   | API Handling | Intermediate–Advanced |
| 2   | NumPy        | Strong                |
| 3   | Pandas       | Strong                |
| 4   | Matplotlib   | Strong                |
| 5   | Seaborn      | Strong                |

## 2. API HANDLING — Working with APIs

[Čo je REST API a ako funguje? Sprievodca pre začiatočníkov | Skillmea](https://images.openai.com/static-rsc-4/3lXYpnAUtN1VF_Gnm845RsBz84cpMH9zTvHXGsm7Ib51nUrtkgf9xNJWrystcYgSM6uyOSpq5wqyG5oIxrwRIbprorzDIPVK8k9eV8K5ejmGtGlS8tkvpcXqN-j085CPTZhsHTLk6LXd_FR1rRWCB7YfNiV2_atOBAUT9X8g4J4?purpose=inline)

[skillmea.sk](https://skillmea.sk/blog/co-je-rest-api?utm_source=chatgpt.com)

### 2.1 What is an API?

Definition: API (Application Programming Interface) is a mechanism that allows two different software applications to communicate and exchange data.

EL10 Explanation: Imagine you are ordering food in a restaurant.

1. You give your order to the waiter.
2. The waiter sends your order to the kitchen.
3. The kitchen prepares the food.
4. The waiter brings your food.

Here:

- You = Client
- Waiter = API
- Kitchen = Server
- Food = Response/Data

Real-world examples:

- Weather applications fetch weather data through APIs.
- Payment applications use payment gateway APIs.
- AI applications use APIs to access AI models.
- Google Maps uses APIs to provide location data.

### 2.2 Important API terminology

| Term           | Meaning                     |
| -------------- | --------------------------- |
| Client         | Application requesting data |
| Server         | System providing data       |
| Endpoint       | Specific API URL            |
| Request        | Message sent to server      |
| Response       | Data returned by server     |
| JSON           | Common data exchange format |
| HTTP           | Communication protocol      |
| Authentication | Verifying access            |
| API Key        | Secret access credential    |

### 2.3 Types of APIs

1. REST API – Uses HTTP methods to communicate.
2. SOAP API – Uses structured XML messages.
3. GraphQL API – Allows clients to request specific data.
4. WebSocket API – Supports two-way real-time communication.

For AI/ML development, REST APIs are especially important.

### 2.4 HTTP methods

| Method | Purpose                |
| ------ | ---------------------- |
| GET    | Retrieve data          |
| POST   | Create/send data       |
| PUT    | Replace existing data  |
| PATCH  | Update specific fields |
| DELETE | Delete data            |

### 2.5 HTTP status codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 204  | No Content            |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 429  | Too Many Requests     |
| 500  | Internal Server Error |
| 503  | Service Unavailable   |

### 2.6 Install Requests library

```
pip install requests
```

```
import requests
```

The `requests` library helps Python communicate with web APIs.

### 2.7 GET request

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts/1"response = requests.get(url)print(response.status_code)print(response.text)print(response.json())
```

Explanation:

- `requests.get()` sends a GET request.
- `status_code` returns the HTTP status.
- `text` returns response content as text.
- `json()` converts JSON response into Python objects.

### 2.8 Working with JSON

JSON stands for JavaScript Object Notation.

Example:

```
{
    "name": "Amir",
    "age": 20,
    "course": "B.Tech AI ML"
}
```

Python dictionary:

```
student = {    "name": "Amir",    "age": 20,    "course": "B.Tech AI ML"}print(student["name"])
```

JSON conversion:

```
import jsondata = '{"name": "Amir", "age": 20}'python_data = json.loads(data)print(python_data["name"])
```

Important functions:

| Function       | Purpose                     |
| -------------- | --------------------------- |
| `json.loads()` | JSON string → Python object |
| `json.dumps()` | Python object → JSON string |
| `json.load()`  | Read JSON from file         |
| `json.dump()`  | Write JSON into file        |

### 2.9 POST request

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts"data = {    "title": "AI ML",    "body": "Learning API handling",    "userId": 1}response = requests.post(url, json=data)print(response.status_code)print(response.json())
```

### 2.10 API error handling

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts/1"try:    response = requests.get(url, timeout=10)    response.raise_for_status()    data = response.json()    print(data)except requests.exceptions.Timeout:    print("Request timed out")except requests.exceptions.HTTPError as e:    print("HTTP Error:", e)except requests.exceptions.RequestException as e:    print("API Error:", e)
```

### 2.11 API parameters

Parameters allow you to filter or customize API requests.

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts"params = {    "userId": 1}response = requests.get(url, params=params)print(response.json())
```

### 2.12 API authentication

Some APIs require authentication.

Common methods:

- API Key
- Bearer Token
- Basic Authentication
- OAuth 2.0

Example:

```
import requestsurl = "https://api.example.com/data"headers = {    "Authorization": "Bearer YOUR_TOKEN"}response = requests.get(url, headers=headers)print(response.status_code)
```

Never expose actual API keys in GitHub repositories. Use environment variables.

```
pip install python-dotenv
```

```
import osfrom dotenv import load_dotenvload_dotenv()api_key = os.getenv("API_KEY")
```

### 2.13 Advanced API concepts

Learn these after the fundamentals:

- Pagination — retrieving large datasets in pages.
- Rate limiting — restricting the number of requests.
- Timeouts — preventing requests from hanging.
- Retries — trying failed requests again.
- Headers — sending additional request information.
- Query parameters — filtering API data.
- Async API handling — making multiple requests efficiently.
- API documentation — understanding endpoints and parameters.
- Data extraction — collecting API data into Pandas DataFrames.

Mini project: Weather Data Fetcher using a public weather API.

# 3. NUMPY — Numerical Computing

[\[\]](https://images.openai.com/static-rsc-4/rGKtXuOSXdSHTUadf9WMxK-zdSuf1gszTL3lwSap7-xOeEFiJJOCDhHPLBM4Rcxv3RGOiflDKprugyyMmTxuJoB0hF7qGCHac9FanP7o2ktwXxWOxEf4tjyYX1GTjDjc2sBVBb1caO4RfYoiKfSmFa66bu-7JXowdobFCrzRjf8?purpose=inline)

[damianavila.github.io](https://damianavila.github.io/Python-Cientifico-HCC/3_NumPy.html?utm_source=chatgpt.com)

### 3.1 What is NumPy?

Definition: NumPy (Numerical Python) is a Python library used for numerical calculations, multidimensional arrays, mathematical operations, and scientific computing.

EL10 Explanation: Suppose you have 10,000 student marks. You want to calculate their average, maximum, minimum, and standard deviation.

Using ordinary Python loops can be cumbersome. NumPy makes these numerical operations easier and efficient.

### 3.2 Why use NumPy?

- Fast numerical calculations.
- Multidimensional arrays.
- Mathematical operations.
- Statistical calculations.
- Matrix operations.
- Linear algebra.
- Foundation for Machine Learning.

### 3.3 Installation

```
pip install numpy
```

```
import numpy as np
```

`np` is the standard alias for NumPy.

### 3.4 Creating NumPy arrays

1\. One-dimensional array

```
import numpy as nparr = np.array([10, 20, 30, 40])print(arr)
```

2\. Two-dimensional array

```
arr = np.array([    [1, 2, 3],    [4, 5, 6]])print(arr)
```

3\. Three-dimensional array

```
arr = np.array([    [[1, 2], [3, 4]],    [[5, 6], [7, 8]]])print(arr)
```

### 3.5 Important array creation functions

| Function              | Purpose                         |
| --------------------- | ------------------------------- |
| `np.array()`          | Create an array                 |
| `np.zeros()`          | Array filled with zeros         |
| `np.ones()`           | Array filled with ones          |
| `np.empty()`          | Allocate an uninitialized array |
| `np.arange()`         | Create a range of values        |
| `np.linspace()`       | Create evenly spaced values     |
| `np.eye()`            | Identity matrix                 |
| `np.full()`           | Fill array with a value         |
| `np.random.rand()`    | Random values between 0 and 1   |
| `np.random.randint()` | Random integers                 |

Examples:

```
np.zeros((2, 3))np.ones((3, 3))np.arange(1, 11, 2)np.linspace(0, 10, 5)np.eye(3)np.full((2, 2), 7)
```

### 3.6 Array attributes

These are extremely important.

```
arr = np.array([    [1, 2, 3],    [4, 5, 6]])print(arr.ndim)print(arr.shape)print(arr.size)print(arr.dtype)print(arr.itemsize)
```

| Attribute  | Meaning              |
| ---------- | -------------------- |
| `ndim`     | Number of dimensions |
| `shape`    | Rows and columns     |
| `size`     | Total elements       |
| `dtype`    | Data type            |
| `itemsize` | Bytes per element    |

### 3.7 Array indexing

Indexing means accessing a particular element.

```
arr = np.array([10, 20, 30, 40])print(arr[0]) print(arr[2])print(arr[-1])
```

2D indexing:

```
arr = np.array([    [10, 20, 30],    [40, 50, 60]])print(arr[0, 1])print(arr[1, 2])
```

### 3.8 Array slicing

Syntax:

```
array[start:stop:step]
```

Example:

```
arr = np.array([10, 20, 30, 40, 50])print(arr[1:4])print(arr[:3])print(arr[::2])print(arr[::-1])
```

### 3.9 Reshaping arrays

Reshaping changes the structure without changing the total number of elements.

```
arr = np.arange(1, 13)new_arr = arr.reshape(3, 4)print(new_arr)
```

Other useful operations:

```
arr.flatten()arr.ravel()arr.reshape(-1, 1)arr.reshape(1, -1)
```

Difference:

- `flatten()` returns a copy.
- `ravel()` returns a flattened view when possible.
- `reshape()` changes the dimensions.

### 3.10 Mathematical operations

```
a = np.array([10, 20, 30])b = np.array([1, 2, 3])print(a + b)print(a - b)print(a * b)print(a / b)print(a ** 2)
```

### 3.11 Universal functions (ufuncs)

```
arr = np.array([1, 4, 9, 16])print(np.sqrt(arr))print(np.square(arr))print(np.exp(arr))print(np.log(arr))print(np.abs(arr))
```

### 3.12 Statistical operations

```
marks = np.array([70, 80, 90, 60, 100])print(np.mean(marks))print(np.median(marks))print(np.std(marks))print(np.var(marks))print(np.min(marks))print(np.max(marks))print(np.sum(marks))
```

### 3.13 Axis in NumPy

For a 2D array:

```
arr = np.array([    [10, 20, 30],    [40, 50, 60]])print(np.sum(arr, axis=0))print(np.sum(arr, axis=1))
```

- `axis=0`: operation down the rows, producing column-wise results.
- `axis=1`: operation across columns, producing row-wise results.

### 3.14 Broadcasting

Broadcasting allows NumPy to perform operations on arrays with compatible shapes.

```
arr = np.array([10, 20, 30])print(arr + 5)
```

Output:

```
[15 25 35]
```

### 3.15 Boolean indexing and filtering

```
marks = np.array([45, 67, 89, 32, 95])print(marks[marks > 60])
```

Output:

```
[67 89 95]
```

### 3.16 Joining and splitting

```
a = np.array([1, 2, 3])b = np.array([4, 5, 6])print(np.concatenate((a, b)))print(np.vstack((a, b)))print(np.hstack((a, b)))print(np.split(np.array([1, 2, 3, 4]), 2))
```

### 3.17 Matrix operations

```
a = np.array([[1, 2], [3, 4]])b = np.array([[5, 6], [7, 8]])print(a.T)print(np.dot(a, b))print(a @ b)print(np.linalg.det(a))print(np.linalg.inv(a))
```

### 3.18 Random module

```
np.random.seed(42)print(np.random.randint(1, 100, 5))print(np.random.rand(3, 3))print(np.random.randn(3, 3))print(np.random.choice([10, 20, 30]))
```

### 3.19 NumPy topics for AI/ML

You must understand:

- Arrays and dimensions.
- Indexing and slicing.
- Reshaping.
- Broadcasting.
- Vectorization.
- Statistical operations.
- Matrix multiplication.
- Linear algebra.
- Random number generation.
- Boolean masking.

Mini project: Student Marks Analysis using NumPy.

# 4. PANDAS — Data Manipulation and Analysis

[Data Analysis with Python Pandas | PPTX](https://images.openai.com/static-rsc-4/8g_jWFVA2_No-oqrt9Fi5Duu7C-KQE2yXq3HQQnFCeYXMpPdBGEO3EDS4NUQ_qsS7nEFLL5yJneP92VpDoyZ7haQKVVY0YXJQ7RT4CP4m02j3oOq0McyXN3j6SK64s23xwtXFtDVhFO1wMuPoTeDExAPj_0ym1eSTWh53D7z2xI?purpose=inline)

[slideshare.net](https://www.slideshare.net/slideshow/data-analysis-with-python-pandas/234423451?utm_source=chatgpt.com)

### 4.1 What is Pandas?

Definition: Pandas is a Python library used for data manipulation, data cleaning, data analysis, and working with structured datasets.

EL10 Explanation: Imagine an Excel sheet containing 10,000 students. You want to find students who scored above 80, remove empty values, calculate averages, and sort marks.

Pandas allows you to do all this using Python.

### 4.2 Why use Pandas?

- Data cleaning.
- Data manipulation.
- Handling missing values.
- Filtering and sorting.
- Grouping and aggregation.
- Reading CSV and Excel files.
- Exploratory Data Analysis (EDA).
- Preparing datasets for ML models.

### 4.3 Installation

```
pip install pandas
```

```
import pandas as pd
```

### 4.4 Main Pandas data structures

1\. Series

A one-dimensional labeled data structure.

```
import pandas as pdmarks = pd.Series([80, 90, 75, 85])print(marks)
```

2\. DataFrame

A two-dimensional table containing rows and columns.

```
data = {    "Name": ["Amir", "Rahul", "Aman"],    "Age": [20, 21, 19],    "Marks": [90, 85, 95]}df = pd.DataFrame(data)print(df)
```

### 4.5 Reading different files

```
df = pd.read_csv("students.csv")df = pd.read_excel("students.xlsx")df = pd.read_json("students.json")df = pd.read_sql("SELECT * FROM students", connection)
```

For Excel support:

```
pip install openpyxl
```

### 4.6 Understanding a dataset

These functions are essential:

```
print(df.head())print(df.tail())print(df.shape)print(df.columns)print(df.index)print(df.dtypes)print(df.info())print(df.describe())print(df.isnull().sum())
```

| Function     | Purpose               |
| ------------ | --------------------- |
| `head()`     | First five rows       |
| `tail()`     | Last five rows        |
| `shape`      | Rows and columns      |
| `columns`    | Column names          |
| `info()`     | Dataset information   |
| `describe()` | Statistical summary   |
| `dtypes`     | Column data types     |
| `isnull()`   | Detect missing values |

### 4.7 Selecting columns

```
print(df["Name"])print(df[["Name", "Marks"]])
```

### 4.8 Selecting rows using loc and iloc

loc — label-based selection

```
print(df.loc[0])print(df.loc[0:2, ["Name", "Marks"]])
```

iloc — integer-position-based selection

```
print(df.iloc[0])print(df.iloc[0:3, 0:2])
```

### 4.9 Filtering data

```
print(df[df["Marks"] > 80])print(df[df["Age"] >= 20])
```

Multiple conditions:

```
result = df[    (df["Marks"] > 80) &    (df["Age"] >= 20)]print(result)
```

Use:

- `&` for AND.
- `|` for OR.
- `~` for NOT.

### 4.10 Adding and deleting columns

```
df["Grade"] = ["A", "B", "A"]df["Bonus"] = df["Marks"] + 5df.drop(columns=["Bonus"], inplace=True)
```

### 4.11 Handling missing values

Missing values are common in real-world datasets.

Detect missing values:

```
print(df.isnull().sum())
```

Remove missing rows:

```
df.dropna(inplace=True)
```

Fill missing values:

```
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```

Other methods:

- `fillna(0)`
- `fillna(method=...)` — note that current Pandas versions prefer explicit forward/backward fill methods.
- `dropna()`
- `interpolate()`

### 4.12 Removing duplicates

```
print(df.duplicated().sum())df.drop_duplicates(inplace=True)
```

### 4.13 Sorting data

```
df.sort_values("Marks")df.sort_values("Marks", ascending=False)
```

### 4.14 GroupBy

GroupBy is used to group data and calculate statistics.

```
data = {    "Department": ["CS", "IT", "CS", "IT"],    "Marks": [90, 80, 85, 75]}df = pd.DataFrame(data)print(df.groupby("Department")["Marks"].mean())
```

Important aggregation functions:

```
df.groupby("Department").agg({    "Marks": ["mean", "max", "min", "sum"]})
```

### 4.15 Merging and joining

Merge:

```
df1 = pd.DataFrame({    "ID": [1, 2],    "Name": ["Amir", "Rahul"]})df2 = pd.DataFrame({    "ID": [1, 2],    "Marks": [90, 85]})result = pd.merge(df1, df2, on="ID")print(result)
```

Important merge types:

- Inner Join
- Left Join
- Right Join
- Outer Join

Concatenation:

```
pd.concat([df1, df2], axis=0)
```

### 4.16 Apply and Lambda

```
df["Marks"] = df["Marks"].apply(lambda x: x + 5)
```

### 4.17 Value counts and unique values

```
print(df["Department"].unique())print(df["Department"].nunique())print(df["Department"].value_counts())
```

### 4.18 Date and time handling

```
df["Date"] = pd.to_datetime(df["Date"])df["Year"] = df["Date"].dt.yeardf["Month"] = df["Date"].dt.monthdf["Day"] = df["Date"].dt.day
```

### 4.19 Exporting datasets

```
df.to_csv("cleaned_data.csv", index=False)df.to_excel("cleaned_data.xlsx", index=False)df.to_json("cleaned_data.json")
```

### 4.20 Advanced Pandas concepts

- Pivot tables.
- Crosstab.
- MultiIndex.
- Resampling.
- Window functions.
- String operations.
- Categorical data.
- Memory optimization.
- Efficient handling of large datasets.

Mini project: Complete Student Performance Data Analysis using Pandas.

# 5. MATPLOTLIB — Data Visualization

[Matplotlib vs. Plotly: Choosing the Right Data Visualization Tool](https://images.openai.com/static-rsc-4/-85Qggfc-04J9v_h8YLF303SajUOu6QACjEOCF0YWVeik_XRoH4vRRQpDPrFoMdNtjswwX6POqNJ3d38oTDcSk0PjKUzskGzKj3JcuCb-7XcKlBmq2JM-Wq9-8TUqGYK8zj2Qtfh0Y3HKFydOLyNmGqpjH-N-0btmbm9NyXLLJI?purpose=inline)

[randomwalk.ai](https://randomwalk.ai/blog/matplotlib-vs-plotly-choosing-the-right-data-visualization-tool/?utm_source=chatgpt.com)

### 5.1 What is Matplotlib?

Definition: Matplotlib is a Python library used to create static, animated, and interactive data visualizations.

EL10 Explanation: Suppose you have marks of 100 students. Instead of reading 100 numbers, you can create a graph that shows:

- Highest and lowest marks.
- Average marks.
- Comparison between students.
- Distribution of marks.

Matplotlib converts numerical data into meaningful visual representations.

### 5.2 Why use Matplotlib?

- Visualize datasets.
- Understand data patterns.
- Identify trends.
- Compare different values.
- Detect unusual observations.
- Create charts for reports and presentations.
- Perform Exploratory Data Analysis (EDA).

### 5.3 Installation

```
pip install matplotlib
```

Import:

```
import matplotlib.pyplot as plt
```

`plt` is the standard alias.

### 5.4 Basic plotting structure

```
import matplotlib.pyplot as pltx = [1, 2, 3, 4, 5]y = [10, 20, 30, 40, 50]plt.plot(x, y)plt.show()
```

Important functions:

| Function        | Purpose           |
| --------------- | ----------------- |
| `plt.plot()`    | Create line graph |
| `plt.show()`    | Display graph     |
| `plt.title()`   | Add title         |
| `plt.xlabel()`  | X-axis label      |
| `plt.ylabel()`  | Y-axis label      |
| `plt.legend()`  | Display legend    |
| `plt.grid()`    | Add grid          |
| `plt.figure()`  | Create figure     |
| `plt.savefig()` | Save graph        |
| `plt.xlim()`    | Set X-axis limits |
| `plt.ylim()`    | Set Y-axis limits |

### 5.5 Line plot

Used to show trends and changes over time.

```
import matplotlib.pyplot as pltmonths = ["Jan", "Feb", "Mar", "Apr"]sales = [100, 150, 120, 200]plt.plot(months, sales)plt.title("Monthly Sales")plt.xlabel("Months")plt.ylabel("Sales")plt.grid()plt.show()
```

Customization:

```
plt.plot(    months,    sales,    color="blue",    marker="o",    linestyle="--",    linewidth=2,    label="Sales")plt.legend()plt.show()
```

### 5.6 Bar chart

Used to compare categories.

```
students = ["Amir", "Rahul", "Aman", "Ravi"]marks = [90, 75, 85, 95]plt.bar(students, marks)plt.title("Student Marks")plt.xlabel("Students")plt.ylabel("Marks")plt.show()
```

Horizontal bar chart:

```
plt.barh(students, marks)plt.show()
```

### 5.7 Scatter plot

Used to identify relationships between two numerical variables.

```
hours = [1, 2, 3, 4, 5, 6]marks = [30, 40, 50, 65, 75, 90]plt.scatter(hours, marks)plt.xlabel("Study Hours")plt.ylabel("Marks")plt.title("Study Hours vs Marks")plt.show()
```

AI/ML use: Understanding relationships between features.

### 5.8 Histogram

Used to understand the frequency distribution of numerical data.

```
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]plt.hist(marks, bins=5, edgecolor="black")plt.title("Marks Distribution")plt.xlabel("Marks")plt.ylabel("Frequency")plt.show()
```

Remember:

- Bar chart compares categories.
- Histogram shows the distribution of numerical values.

### 5.9 Pie chart

Used to show proportions or percentages.

```
labels = ["Python", "Java", "C++", "SQL"]values = [40, 25, 20, 15]plt.pie(    values,    labels=labels,    autopct="%1.1f%%",    startangle=90)plt.title("Programming Language Preference")plt.show()
```

### 5.10 Box plot

Used to understand data distribution, quartiles, and potential outliers.

```
marks = [45, 50, 55, 60, 65, 70, 75, 80, 95, 150]plt.boxplot(marks)plt.title("Marks Distribution")plt.show()
```

Important concepts:

- Minimum.
- First quartile (Q1).
- Median (Q2).
- Third quartile (Q3).
- Maximum within whisker limits.
- Potential outliers.

### 5.11 Subplots

Subplots allow multiple graphs in one figure.

```
import matplotlib.pyplot as pltx = [1, 2, 3, 4]y = [10, 20, 30, 40]fig, axes = plt.subplots(1, 2)axes[0].plot(x, y)axes[0].set_title("Line Plot")axes[1].bar(x, y)axes[1].set_title("Bar Chart")plt.tight_layout()plt.show()
```

### 5.12 Figure and Axes

Understand these two important concepts:

- Figure: The complete canvas.
- Axes: The individual plotting area inside the figure.

```
fig, ax = plt.subplots(figsize=(8, 5))ax.plot([1, 2, 3], [10, 20, 30])ax.set_title("My Graph")ax.set_xlabel("X")ax.set_ylabel("Y")plt.show()
```

### 5.13 Customization

Learn these properties:

| Property     | Meaning           |
| ------------ | ----------------- |
| `color`      | Graph color       |
| `marker`     | Data point symbol |
| `linestyle`  | Line style        |
| `linewidth`  | Line thickness    |
| `markersize` | Marker size       |
| `alpha`      | Transparency      |
| `figsize`    | Figure dimensions |
| `fontsize`   | Text size         |
| `rotation`   | Rotate labels     |
| `edgecolor`  | Border color      |

### 5.14 Saving visualizations

```
plt.plot([1, 2, 3], [10, 20, 30])plt.savefig(    "graph.png",    dpi=300,    bbox_inches="tight")plt.show()
```

### 5.15 Advanced Matplotlib topics

- Multiple lines in one plot.
- Multiple axes.
- Subplots and GridSpec.
- Annotations.
- Error bars.
- Logarithmic scales.
- Date and time plots.
- Interactive plotting.
- 3D plots.
- Animation.
- Styling and themes.

### 5.16 Important graph selection

| Chart     | Best use                       |
| --------- | ------------------------------ |
| Line      | Trends over time               |
| Bar       | Category comparison            |
| Scatter   | Relationship between variables |
| Histogram | Frequency distribution         |
| Pie       | Proportions                    |
| Box       | Outliers and distribution      |
| Area      | Cumulative trends              |
| Error bar | Uncertainty                    |
| Heatmap   | Values across two dimensions   |

Mini project: Student Marks Visualization Dashboard using Matplotlib.

# 6. SEABORN — Statistical Data Visualization

[Ten Must-Know Seaborn Plots. For anyone who wants to ace… | by Sneha Bajaj | Medium](https://images.openai.com/static-rsc-4/i3aN9E425ymZlh3-U664cNWhTw8osGedkaTrLM8UXETBf9-vo-wCN-_ok65QAUBdHojK-N7Ur824h9Q_eS62YndZAxTPPG_KRgFTYRTXikdakXDvC0SsRIGor1wOx-fj6u2ksIc0hcExUjd5AIZ1hIFq6txEyXz3tUa59_z8s30?purpose=inline)

[medium.com](https://medium.com/%40snehabajaj108/ten-must-know-seaborn-plots-1f3a82dc99c5?utm_source=chatgpt.com)

### 6.1 What is Seaborn?

Definition: Seaborn is a Python statistical data visualization library built on top of Matplotlib.

EL10 Explanation: Matplotlib gives you tools to create graphs. Seaborn makes it easier to create attractive statistical graphs and understand relationships in datasets.

Seaborn is particularly useful for Exploratory Data Analysis.

### 6.2 Why use Seaborn?

- Beautiful statistical graphs.
- Better data visualization.
- Correlation analysis.
- Distribution analysis.
- Relationship analysis.
- Categorical data visualization.
- Understanding Machine Learning datasets.

### 6.3 Installation

```
pip install seaborn
```

Import:

```
import seaborn as snsimport matplotlib.pyplot as plt
```

### 6.4 Load an inbuilt dataset

Seaborn provides example datasets.

```
import seaborn as snsimport matplotlib.pyplot as pltdf = sns.load_dataset("tips")print(df.head())
```

Other example datasets include:

- `iris`
- `titanic`
- `penguins`
- `flights`
- `tips`

### 6.5 Scatter plot

Used to understand the relationship between two numerical variables.

```
sns.scatterplot(    data=df,    x="total_bill",    y="tip")plt.show()
```

### 6.6 Line plot

Used to show trends.

```
sns.lineplot(    data=df,    x="size",    y="total_bill")plt.show()
```

### 6.7 Bar plot

Used to compare statistical values across categories. By default, Seaborn estimates the mean.

```
sns.barplot(    data=df,    x="day",    y="total_bill")plt.show()
```

### 6.8 Count plot

Used to count observations in different categories.

```
sns.countplot(    data=df,    x="day")plt.show()
```

### 6.9 Histogram

Used to understand the distribution of numerical data.

```
sns.histplot(    data=df,    x="total_bill",    bins=20,    kde=True)plt.show()
```

`kde=True` adds a smooth estimated density curve.

### 6.10 Box plot

Used to identify distribution, quartiles, and potential outliers.

```
sns.boxplot(    data=df,    x="day",    y="total_bill")plt.show()
```

### 6.11 Violin plot

Combines distribution density information with box-plot-like summaries.

```
sns.violinplot(    data=df,    x="day",    y="total_bill")plt.show()
```

### 6.12 Heatmap

One of the most important Seaborn visualizations for AI/ML.

A heatmap uses colors to represent numerical values.

Example: Correlation matrix.

```
import seaborn as snsimport matplotlib.pyplot as pltdf = sns.load_dataset("iris")corr = df.select_dtypes(include="number").corr()sns.heatmap(    corr,    annot=True,    cmap="coolwarm")plt.title("Correlation Heatmap")plt.show()
```

Why important in ML?

It helps identify relationships between numerical features and possible multicollinearity.

### 6.13 Pairplot

Pairplot shows relationships between multiple numerical variables.

```
df = sns.load_dataset("iris")sns.pairplot(    df,    hue="species")plt.show()
```

This is especially useful for exploring datasets before model training.

### 6.14 Regression plot

Shows the relationship between two numerical variables with a fitted regression line.

```
sns.regplot(    data=df,    x="sepal_length",    y="petal_length")plt.show()
```

### 6.15 Joint plot

Combines a relationship plot with marginal distributions.

```
sns.jointplot(    data=df,    x="sepal_length",    y="petal_length",    kind="scatter")
```

### 6.16 Styling and themes

```
sns.set_theme(style="whitegrid")sns.set_palette("Set2")sns.set_context("notebook")
```

Common styles:

- `whitegrid`
- `darkgrid`
- `white`
- `dark`
- `ticks`

### 6.17 FacetGrid

FacetGrid creates multiple plots based on categories.

```
df = sns.load_dataset("tips")g = sns.FacetGrid(    df,    col="time")g.map_dataframe(    sns.histplot,    x="total_bill")plt.show()
```

### 6.18 Advanced Seaborn topics

- PairGrid.
- FacetGrid.
- JointGrid.
- Categorical plots.
- Distribution plots.
- Regression visualization.
- Custom palettes.
- Statistical estimation.
- Confidence intervals.
- Complex multi-variable visualization.

### 6.19 Matplotlib vs Seaborn

| Matplotlib                    | Seaborn                           |
| ----------------------------- | --------------------------------- |
| General visualization library | Statistical visualization library |
| More manual customization     | Convenient default styling        |
| Fine-grained control          | High-level plotting functions     |
| Supports many plot types      | Strong statistical plots          |
| Works independently           | Built on Matplotlib               |

Mini project: Iris Dataset Exploratory Data Analysis using Seaborn.

# 7. HOW ALL FIVE TOPICS WORK TOGETHER

This is the most important practical concept in Phase 02.

[Core Concepts | Python for Analytics | QuickLearnPro](https://images.openai.com/static-rsc-4/U3gerciD8apmTxHszOhrfYy0abqE_P_DSp5iYKpyNh0u4pc4IC3X8nWZT6VRAGGTxnZwvIkUFcjddmtMaAOeNm5I17EGMyrqgnMk0Ewk3Pswzs9GyP7k_fTIaaiYAZMkqSf6Pg56ysqDlYstrbqnESZ7qBE9coQ6ZC2Db7dQnYQ?purpose=inline)

[quicklearnpro.com](https://quicklearnpro.com/domains/data-analytics/python-for-analytics/core-concepts?utm_source=chatgpt.com)

Imagine you are building an AI-powered student performance prediction system.

| Step | Technology   | Work                              |
| ---- | ------------ | --------------------------------- |
| 1    | API Handling | Collect student data              |
| 2    | NumPy        | Perform numerical calculations    |
| 3    | Pandas       | Clean and organize data           |
| 4    | Matplotlib   | Create basic graphs               |
| 5    | Seaborn      | Perform statistical visualization |
| 6    | ML libraries | Train prediction models           |

Complete workflow:

```
          DATA SOURCE
               |
               v
          API HANDLING
               |
               v
           RAW DATA
               |
               v
             NUMPY
      Numerical Operations
               |
               v
            PANDAS
       Cleaning and Analysis
               |
               v
          MATPLOTLIB
        Basic Visualization
               |
               v
            SEABORN
      Statistical Visualization
               |
               v
          CLEAN DATASET
               |
               v
        MACHINE LEARNING
               |
               v
        MODEL PREDICTION
```


# 8. PRACTICE QUESTIONS

These questions will help you check whether you actually understand the topics.

Phase 02 knowledge test

8 MCQs

1\. Which Python library is used for multidimensional numerical arrays?

Pandas

NumPy

Seaborn

Requests

2\. Which HTTP method is normally used to retrieve API data?

POST

DELETE

GET

PATCH

3\. Which Pandas function displays the first five rows?

tail()

head()

info()

describe()

4\. Which function creates a histogram in Matplotlib?

plt.bar()

plt.plot()

plt.hist()

plt.pie()

5\. Which Seaborn function creates a correlation heatmap?

sns.pairplot()

sns.heatmap()

sns.countplot()

sns.regplot()

6\. What does df.dropna() do?

Fills missing values

Removes missing-value rows by default

Sorts data

Removes duplicates

7\. What is broadcasting in NumPy?

Sending API requests

Compatible array operations

Creating graphs

Reading CSV files

8\. Which Seaborn function is useful for pairwise numerical relationships?

sns.pairplot()

sns.countplot()

sns.barplot()

sns.boxplot()

Submit answersAnswer all 8 questions to see your result and explanations.

# 9. FINAL PHASE 02 CHECKLIST

Use this checklist to track your progress.

Your learning progress

# 0%

0 of 59 topics completed

1\. API Handling

0/10 completed

Understand API and REST architecture

GET, POST, PUT, PATCH, DELETE

HTTP status codes

JSON handling

Requests library

Headers and parameters

Authentication and API keys

Exception handling and timeouts

Pagination, retries and rate limits

Fetch API data into Pandas

2\. NumPy

0/11 completed

Array creation and dimensions

Array attributes

Indexing and slicing

Reshaping and flattening

Mathematical operations

Broadcasting and vectorization

Statistical operations

Axis and Boolean indexing

Joining and splitting

Matrix and linear algebra

Random number generation

3\. Pandas

0/13 completed

Series and DataFrame

Read CSV, Excel and JSON

head, tail, info and describe

loc and iloc

Filtering and sorting

Adding and deleting columns

Missing value handling

Duplicate removal

GroupBy and aggregation

Merge, join and concat

Apply and Lambda

Pivot tables and date handling

Export datasets

4\. Matplotlib

0/9 completed

Line and bar charts

Scatter plots and histograms

Pie and box plots

Figure and Axes

Subplots

Graph customization

Annotations and legends

Save figures

Advanced plotting

5\. Seaborn

0/10 completed

Scatter and line plots

Bar and count plots

Histogram and KDE

Box and violin plots

Heatmaps and correlation

Pairplot

Regression plot

Jointplot

FacetGrid and PairGrid

Themes and customization

6\. Projects

0/6 completed

Weather Data Fetcher

Student Marks Analyzer

Student Data Cleaning

Visualization Dashboard

Iris Dataset EDA

Combined Student Performance Analysis

Reset checklist