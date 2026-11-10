# Complete Matplotlib Tutorial



Beginner to Advanced

Python + Data Science + AI/ML



Matplotlib is one of the most important Python libraries for Data Science, Data Analysis, Machine Learning and AI.

I'll teach you from zero to advanced with:

- Simple English definitions.
- Hinglish explanations.
- Python code examples.
- Expected outputs.
- Important functions and rules.
- Practice questions and projects.

# 1. What is Matplotlib?

Definition: Matplotlib is a Python library used to create graphs, charts and data visualizations.

EL10: Suppose you have marks of five students. You can print the marks, but a graph makes it easier to understand who scored more or less.

[Top 10 Matplotlib Functions Every Data Analyst Should Know](https://images.openai.com/static-rsc-4/rjI91bTzXoaVl-NKdIcru5U1I37nvQowGoYT5xqV5MBlSSaIF_YMGK8vJEM9lhf_a7hfynRVDE1V6ZoMRx-GIqmqAnQprZgFUH80tJYQFJmKUd3oq_qP49KjtUp9bKpdPKTot1fdld3HxylvMgA80pEjS627E7Mf7DO_fyQE8qo?purpose=inline)

[Master Data Visualization with Python Bar Chart: Tips, Examples, and Techniques #4 | by Mustafa Celik | Medium](https://images.openai.com/static-rsc-4/XJMbV-quFiK0Fmpw_QKKmvXkC7UZUACHtvaae78VB08CWb2QOUbQiOvPIrilQpD1VYIWgZPSBqniB3qlK2AlM7dMJgOq1PxXxf9waG8iXJ4YC6DpEAA6CYzoJcNSZptzI98XAI41N1vgTb3EL4lL2pikR4KLpycnyG4Vuh9kKl4?purpose=inline)

[Matplotlib Tutorial - Matplotlib Plot Examples](https://images.openai.com/static-rsc-4/va-fAMjaigMWmyW7DBg9SCnvSZ1vBrpq-kdocM5GMrNiLbkLsrzV8sU8ciK137jEDy9Vy0TCnnkgWyX9dxgJnT-JiROvMFVNKxgV-vKK2LBO5IvAed2PYZkDefZOQr9gzj2XGKHmeQrIlohk5ZtXvjxKg6EMO4HoV5tiUcPuUvs?purpose=inline)

8

Why do we use Matplotlib?

1. To visualize data.
2. To compare values.
3. To identify trends.
4. To find patterns.
5. To understand datasets.
6. To visualize ML model results.

# 2. Installation and Import

Step 1: Install Matplotlib

In Jupyter Notebook or terminal:

```
pip install matplotlib
```

Step 2: Import the library

```
import matplotlib.pyplot as plt
```

Explanation:

| Code         | Meaning                     |
| ------------ | --------------------------- |
| `import`     | Bring a library into Python |
| `matplotlib` | Library name                |
| `pyplot`     | Plotting module             |
| `plt`        | Short name / alias          |

`plt` is the standard alias used for Matplotlib's pyplot module.

# 3. First Graph – Line Plot

```
import matplotlib.pyplot as pltx = [1, 2, 3, 4, 5]y = [10, 20, 15, 30, 25]plt.plot(x, y)plt.show()
```

[Python:Matplotlib | pyplot | .plot() | Codecademy](https://images.openai.com/static-rsc-4/jUxLmUsJRiGMFiXDhT3FkyRe9XnNPFqyTlOAxijT5SHzRuq_4uY8FEAUYKQzMu9nL_AkJmjK2zEwNU1XaFJv5CFREbcH3LhXW2E3UFe5TnJfqkgAR5veSU4bH7u9InHQtR7M0nR-DS3CNrNoXVe-lA8a-SP7VK6wmFgPGuIcjv0?purpose=inline)

[codecademy.com](https://www.codecademy.com/resources/docs/matplotlib/pyplot/plot?utm_source=chatgpt.com)

Understand each function:

| Function       | Work               |
| -------------- | ------------------ |
| `plt.plot()`   | Creates line graph |
| `plt.show()`   | Displays graph     |
| `plt.title()`  | Adds graph title   |
| `plt.xlabel()` | Adds X-axis label  |
| `plt.ylabel()` | Adds Y-axis label  |

Add labels:

```
plt.plot(x, y)plt.title("My First Graph")plt.xlabel("Days")plt.ylabel("Sales")plt.show()
```

# 4. Types of Graphs in Matplotlib

These are the most important graph types you should learn.

## 4.1 Line Plot – `plt.plot()`

[Python Matplotlib. Matplotlib is a popular Python tool… | by Narayanan | Medium](https://images.openai.com/static-rsc-4/5iExYIe5V7Nl-XjbMB7Tqgv1FGlMOY4OrKGGhk8VIeUkAf4WRIWyu7qpIUC2sHznNwoWOtYHRlm-vtMwAas2FVAKkFRz43BGDq3oQGKnimrxUgvohob9zcruimY4aNEvoFM9FcoTfjqUdayT93pQNUPk7TWrrWFJ0QL1t2D7wyo?purpose=inline)

[medium.com](https://medium.com/%40narenss/matplotlib-basic-overview-ffe5d39e22d7?utm_source=chatgpt.com)

Used for: Trends over time, growth, temperature, stock prices.

```
import matplotlib.pyplot as pltmonths = [1, 2, 3, 4, 5]sales = [100, 150, 120, 200, 250]plt.plot(months, sales)plt.title("Monthly Sales")plt.xlabel("Month")plt.ylabel("Sales")plt.grid(True)plt.show()
```

## 4.2 Bar Chart – `plt.bar()`

[How to Add Value Labels to a Bar Plot in Matplotlib? | Baeldung on Computer Science](https://images.openai.com/static-rsc-4/sHcB9tcw67lWa0E7ctZ162YYYa7jF0fG0mHmU3wp18j1_yLhxC4NBp_CLYFK8iPkhx430aOTbu6DdzpWEToOt2eY58udIQUXPFr82cMAU_YTeJ4Yi9VsQV-pNMh3MZdMIg67i_YVS-kMhLtogpUxYdbZCN1gufHqsH3zG0UMVLw?purpose=inline)

[baeldung.com](https://www.baeldung.com/cs/matplotlib-add-value-labels-bar-plot?utm_source=chatgpt.com)

Used for: Comparing different categories.

```
students = ["A", "B", "C", "D"]marks = [80, 90, 70, 95]plt.bar(students, marks)plt.title("Student Marks")plt.xlabel("Students")plt.ylabel("Marks")plt.show()
```

Horizontal bar chart:

```
plt.barh(students, marks)plt.show()
```

## 4.3 Scatter Plot – `plt.scatter()`

[Python:Matplotlib | pyplot | .scatter() | Codecademy](https://images.openai.com/static-rsc-4/aoSvdEM4mwJ0JK2wBjSWsn6_6H0akqBn0VEeMr2Sl1ccIVl7CqJEas60p0FQeZ1Sz5xUh_fXeTq6rc67S3H4Ug9DN5U3pHBYdAeCkzMfgY4KXgLOCTaLgBhRcDW8pBdgNFpvPkVWB0kJqAPm9XMxhM8u52cmBMf76M-QeGi9f2c?purpose=inline)

[codecademy.com](https://www.codecademy.com/resources/docs/matplotlib/pyplot/scatter?utm_source=chatgpt.com)

Used for: Finding relationships between two variables.

```
height = [150, 160, 170, 180, 190]weight = [50, 55, 65, 75, 85]plt.scatter(height, weight)plt.xlabel("Height")plt.ylabel("Weight")plt.title("Height vs Weight")plt.show()
```

EL10: Har dot ek observation ko represent karta hai.

## 4.4 Pie Chart – `plt.pie()`

[Matplotlib - Pie Chart](https://images.openai.com/static-rsc-4/A6tn7uJIOFK16AlDCZy4SxjyEWK7c4WxTebcHGStmDherHSuOqLIN5qvifoK1L2Mxqrn0DfLEvp_43nO8ubbjKHuqx3S6RyaLVDlXPZjp90Bz8Ps0cZXVtDRXr7Wze9ZsVrXobbmHQGKR6Y21DD6hEHMT7mtQiChpz5OkKtw_4E?purpose=inline)

[tutorialspoint.com](https://www.tutorialspoint.com/matplotlib/matplotlib_pie_chart.htm?utm_source=chatgpt.com)

Used for: Showing proportions or percentages.

```
subjects = ["Python", "Java", "SQL", "ML"]marks = [30, 25, 20, 25]plt.pie(    marks,    labels=subjects,    autopct="%1.1f%%")plt.title("Subject Distribution")plt.show()
```

Important parameters:

- `labels`: Names of categories.
- `autopct`: Displays percentages.
- `explode`: Separates a slice.
- `startangle`: Rotates the pie chart.

```
plt.pie(    marks,    labels=subjects,    autopct="%1.1f%%",    explode=[0.1, 0, 0, 0],    startangle=90)plt.show()
```

## 4.5 Histogram – `plt.hist()`

[Visualization in Python  – PyFi](https://images.openai.com/static-rsc-4/F644Z6yoZz-kvAo3gXM4-4Lr58ZuRxE3h4h876YspHaGaYkZUSbo3yOHYGxdHBXjMWgh5ypN8ESCdNKaaWKRBJFEacBBVY0dDvLnalpi0W7BueEWR6pKv6Ls6Exd2rbc-j4YhGnnRzZkOvEVmeYsk3MqECeyShhPxKBF49AVl1c?purpose=inline)

[pyfi.com](https://pyfi.com/blogs/articles/visualization-in-python?utm_source=chatgpt.com)

Used for: Understanding data distribution and frequency.

```
marks = [45, 50, 55, 60, 60, 70, 75, 80, 85, 90]plt.hist(marks, bins=5)plt.title("Marks Distribution")plt.xlabel("Marks")plt.ylabel("Frequency")plt.show()
```

What is `bins`?

Bins means how many groups or intervals you divide the data into.

For example: 0–20, 20–40, 40–60, etc.

## 4.6 Box Plot – `plt.boxplot()`

[Principles and Techniques of Data Science - 7  Visualization I](https://images.openai.com/static-rsc-4/ccUH-pncGnPAjXG202H1xlax1EMBmlUMkfwK2KdyY84Rac_WJFuHQaPJaK-UNXhkg2h096KbkZP81r05u35R39nsW8iMHhLlv1Vkg99L3xzcheax5K8uVHx9TjcLxcGobBjfR7UroERjy6iKY40OAT43cKzM95NjW8vG38pfzbc?purpose=inline)

[ds100.org](https://ds100.org/fa23-course-notes/visualization_1/visualization_1.html?utm_source=chatgpt.com)

Used for:

- Finding outliers.
- Understanding data spread.
- Identifying median and quartiles.

```
data = [10, 20, 25, 30, 35, 40, 100]plt.boxplot(data)plt.title("Box Plot")plt.show()
```

## 4.7 Area Plot – `plt.fill_between()`

[Advanced Matplotlib: A Comprehensive Guide to Data Visualization | Towards AI](https://images.openai.com/static-rsc-4/-EvHOukorZfwIdxs8s76M_mdNDMFFVGoAx0_EtEP6_K-qTdONM4CU2B286rKsUx4G9uIvBFzIRNtBwJItumkLhIFxJ-w-dfwIshwO4R4Vm0saS0diO4ATPJRsOH2-5Q9Ow6k7JPtbQlVzRc0H7nwV_3TYP5Z-PATaKBQjQfyPVI?purpose=inline)

[towardsai.net](https://towardsai.net/p/data-science/advanced-matplotlib-a-comprehensive-guide-to-data-visualization?utm_source=chatgpt.com)

Used for showing the magnitude of values over time.

```
x = [1, 2, 3, 4, 5]y = [10, 20, 15, 30, 25]plt.fill_between(x, y, alpha=0.4)plt.plot(x, y)plt.show()
```

## 4.8 Stem Plot – `plt.stem()`

Used for discrete data points.

```
x = [1, 2, 3, 4, 5]y = [10, 20, 15, 30, 25]plt.stem(x, y)plt.show()
```

## 4.9 Step Plot – `plt.step()`

Used for data that changes in steps rather than continuously.

```
x = [1, 2, 3, 4, 5]y = [10, 10, 20, 20, 30]plt.step(x, y)plt.show()
```

## 4.10 Stack Plot – `plt.stackplot()`

Used to compare the contribution of multiple categories over time.

```
days = [1, 2, 3, 4, 5]python = [10, 20, 15, 25, 30]java = [15, 10, 20, 15, 20]plt.stackplot(days, python, java,              labels=["Python", "Java"])plt.legend()plt.show()
```

# 5. Complete Customization of Graphs

A graph is not only about displaying data. You should also know how to make it readable and professional.

## 5.1 Change Colors

```
plt.plot(x, y, color="red")plt.bar(students, marks, color="blue")plt.scatter(height, weight, color="green")
```

Some common colors:

| Color  | Code       |
| ------ | ---------- |
| Red    | `"red"`    |
| Blue   | `"blue"`   |
| Green  | `"green"`  |
| Black  | `"black"`  |
| Yellow | `"yellow"` |
| Purple | `"purple"` |
| Orange | `"orange"` |

You can also use HEX colors:

```
plt.plot(x, y, color="#3498DB")
```

## 5.2 Line Styles

```
plt.plot(x, y, linestyle="--")
```

| Style  | Meaning       |
| ------ | ------------- |
| `"-"`  | Solid line    |
| `"--"` | Dashed line   |
| `"-."` | Dash-dot line |
| `":"`  | Dotted line   |

## 5.3 Line Width

```
plt.plot(x, y, linewidth=3)
```

## 5.4 Markers

Markers display points on the graph.

```
plt.plot(x, y, marker="o")
```

| Marker | Shape    |
| ------ | -------- |
| `"o"`  | Circle   |
| `"s"`  | Square   |
| `"*"`  | Star     |
| `"+"`  | Plus     |
| `"x"`  | Cross    |
| `"^"`  | Triangle |

Combine everything:

```
plt.plot(    x, y,    color="red",    linestyle="--",    linewidth=2,    marker="o",    markersize=8)plt.show()
```

## 5.5 Grid

```
plt.grid(True)
```

Change grid appearance:

```
plt.grid(    True,    color="gray",    linestyle="--",    linewidth=0.5)
```

## 5.6 Legend

Legend explains which line represents which data.

```
x = [1, 2, 3, 4]python = [10, 20, 30, 40]java = [15, 25, 35, 45]plt.plot(x, python, label="Python")plt.plot(x, java, label="Java")plt.legend()plt.show()
```

## 5.7 Axis Limits

Set the minimum and maximum values of axes.

```
plt.xlim(0, 10)plt.ylim(0, 100)
```

## 5.8 Change Figure Size

```
plt.figure(figsize=(10, 5))plt.plot(x, y)plt.show()
```

`figsize=(10, 5)` means width 10 inches and height 5 inches.

## 5.9 Font Size and Font Weight

```
plt.title("Sales Graph", fontsize=20, fontweight="bold")plt.xlabel("Months", fontsize=14)plt.ylabel("Sales", fontsize=14)
```

## 5.10 Rotate Labels

```
plt.xticks(rotation=45)
```

Useful when category names are long.

## 5.11 Add Text and Annotations

```
plt.plot(x, y)plt.text(2, 20, "Important Point")plt.annotate(    "Maximum",    xy=(5, 25),    xytext=(3, 30),    arrowprops={"arrowstyle": "->"})plt.show()
```

- `text()` adds text at a coordinate.
- `annotate()` adds an explanation, optionally with an arrow.

# 6. Multiple Lines in One Graph

You can display multiple datasets on one graph.

```
x = [1, 2, 3, 4, 5]y1 = [10, 20, 30, 40, 50]y2 = [5, 15, 25, 35, 45]y3 = [15, 25, 35, 45, 55]plt.plot(x, y1, label="Python")plt.plot(x, y2, label="Java")plt.plot(x, y3, label="C++")plt.title("Programming Language Growth")plt.legend()plt.grid(True)plt.show()
```

# 7. Subplots – Multiple Graphs in One Figure

[Matplotlib - Introduction](https://images.openai.com/static-rsc-4/8xj1-TC-i8I1Qd395UBTApaIM8C1GXGnC1FJMJrcoxZ1Nov-fZ0HzfGbHKU8NLEWMMl3t5AdZ4NlHhVOyDe_cpHoWuWQJ7o6XkXa-wTwQoAzQOCJmXN11LMZllC8u1a9V9f8bdtbQ4Q73JBpLOVrg5TDDKJbefDQNIncr7F7rpU?purpose=inline)

[tutorialspoint.com](https://www.tutorialspoint.com/matplotlib/matplotlib_introduction.htm?utm_source=chatgpt.com)

This is very important for Data Science.

Definition: Subplots allow you to display multiple graphs inside one figure.

```
import matplotlib.pyplot as pltplt.subplot(2, 2, 1)plt.plot([1, 2, 3], [10, 20, 30])plt.title("Line")plt.subplot(2, 2, 2)plt.bar(["A", "B"], [20, 40])plt.title("Bar")plt.subplot(2, 2, 3)plt.scatter([1, 2, 3], [5, 10, 15])plt.title("Scatter")plt.subplot(2, 2, 4)plt.pie([30, 70], labels=["A", "B"])plt.title("Pie")plt.tight_layout()plt.show()
```

Understand `plt.subplot(rows, columns, position)`:

- First `2`: Two rows.
- Second `2`: Two columns.
- Third number: Graph position.

Modern alternative: `plt.subplots()`.

```
fig, ax = plt.subplots(2, 2, figsize=(10, 7))ax[0, 0].plot([1, 2, 3], [10, 20, 30])ax[0, 1].bar(["A", "B"], [20, 40])ax[1, 0].scatter([1, 2], [5, 10])ax[1, 1].hist([10, 20, 20, 30, 40])plt.tight_layout()plt.show()
```

# 8. Figure and Axes – Very Important Concept

[Introduction to Matplotlib - Zero to Mastery Data Science and Machine Learning Bootcamp](https://images.openai.com/static-rsc-4/7CKYcMIiHaji9pIpq4hUEKO9z3Htv_6WPNgIgqKSqMMd0lT832XXrofZ6iR4gIMgdOxOxHxpHEfuDKdylP8aly-rSVlfyWiiwMAdKspJqqC6Rv56EOs-D8K1-n6EIT_USntJrYjVrxigqotzy1eDDzWRMSXHjfTWR8IzJfumLwI?purpose=inline)

[dev.mrdbourke.com](https://dev.mrdbourke.com/zero-to-mastery-ml/introduction-to-matplotlib/?utm_source=chatgpt.com)

There are two important objects:

1\. Figure: The complete canvas containing the graph or graphs.

2\. Axes: The actual plotting area where data is drawn.

Example:

```
fig, ax = plt.subplots()ax.plot([1, 2, 3], [10, 20, 30])ax.set_title("My Graph")ax.set_xlabel("X Axis")ax.set_ylabel("Y Axis")plt.show()
```

Remember:

| Pyplot style   | Object-oriented style |
| -------------- | --------------------- |
| `plt.plot()`   | `ax.plot()`           |
| `plt.title()`  | `ax.set_title()`      |
| `plt.xlabel()` | `ax.set_xlabel()`     |
| `plt.ylabel()` | `ax.set_ylabel()`     |
| `plt.grid()`   | `ax.grid()`           |
| `plt.legend()` | `ax.legend()`         |

Recommendation: Learn both, but use `fig, ax = plt.subplots()` for complex projects.

# 9. Advanced Matplotlib

## 9.1 Logarithmic Scale

Useful when values have a very large range.

```
x = [1, 2, 3, 4, 5]y = [10, 100, 1000, 10000, 100000]plt.plot(x, y)plt.yscale("log")plt.show()
```

Other functions:

```
plt.xscale("log")plt.yscale("log")
```

## 9.2 Heatmap – `plt.imshow()`

[A Complete-ish Guide To Making Scientific Figures for Publication with Python and Matplotlib](https://images.openai.com/static-rsc-4/4lm4a6ffiWzk4sro8pGwAazqfTF_Vx3JRWuKVfQtUdsuBAxp0iROCs7_kBmS6JojvDWv-XMnYd319rzJb7nOVYNB5VPbH2XmlPMXrlbrAKZF-tRLscK6oKBliWJ0UNwrLp6_56PykJTQb0wD8CUH8RDuySffh6LOWxmqj4v12b8?purpose=inline)

[dendwrite.substack.com](https://dendwrite.substack.com/p/a-complete-ish-guide-to-making-scientific?utm_source=chatgpt.com)

Used for visualizing matrices and correlation data.

```
import numpy as npimport matplotlib.pyplot as pltdata = np.array([    [10, 20, 30],    [40, 50, 60],    [70, 80, 90]])plt.imshow(data, cmap="viridis")plt.colorbar()plt.title("Heatmap")plt.show()
```

## 9.3 Color Maps – `cmap`

```
plt.scatter(x, y, c=y, cmap="viridis")plt.colorbar()plt.show()
```

Popular colormaps:

- `"viridis"`
- `"plasma"`
- `"inferno"`
- `"magma"`
- `"coolwarm"`
- `"Blues"`
- `"Reds"`

## 9.4 Error Bars

Used to show uncertainty or variability.

```
x = [1, 2, 3, 4]y = [10, 20, 30, 40]error = [2, 3, 2, 4]plt.errorbar(x, y, yerr=error, fmt="o-")plt.show()
```

## 9.5 Twin Axes

Used when two datasets have different scales.

```
fig, ax1 = plt.subplots()x = [1, 2, 3, 4]temperature = [20, 25, 30, 35]sales = [100, 200, 300, 400]ax1.plot(x, temperature, color="red")ax1.set_ylabel("Temperature")ax2 = ax1.twinx()ax2.plot(x, sales, color="blue")ax2.set_ylabel("Sales")plt.show()
```

## 9.6 Horizontal and Vertical Reference Lines

```
plt.axhline(y=50, linestyle="--")plt.axvline(x=3, linestyle="--")plt.show()
```

- `axhline()` = horizontal line.
- `axvline()` = vertical line.

# 10. Matplotlib with NumPy

Matplotlib and NumPy are frequently used together in Data Science.

NumPy creates numerical data; Matplotlib visualizes it.

```
import numpy as npimport matplotlib.pyplot as pltx = np.linspace(0, 10, 100)y = np.sin(x)plt.plot(x, y)plt.title("Sine Wave")plt.xlabel("X")plt.ylabel("Sin(X)")plt.grid(True)plt.show()
```

[How to Create Professional and Readable Scientific Plots in Python | by Filipe Borges | Medium](https://images.openai.com/static-rsc-4/TFQdeq6zwYQ4jSlx0FEseUI8Jq691zJ5hzr7OELLS2frY6enunoQGGbWagdVjVW5jUiTghwRwTOQeFT4sDlp1-eafMrFqs0Aweq5QXTchFl2zIEXl2vjPs0EBDgGOXq8BARdVlarnORpj22korvmnJqCIFWP9NU1Z1PmwxG-E4M?purpose=inline)

[medium.com](https://medium.com/%40FilipeBorgesBR/how-to-create-professional-and-readable-scientific-plots-in-python-72f1defed8b3?utm_source=chatgpt.com)

Other mathematical functions:

```
y1 = np.sin(x)y2 = np.cos(x)y3 = np.tan(x)plt.plot(x, y1, label="Sin")plt.plot(x, y2, label="Cos")plt.legend()plt.grid(True)plt.show()
```

Important NumPy functions for visualization:

| Function           | Purpose                      |
| ------------------ | ---------------------------- |
| `np.array()`       | Creates an array             |
| `np.arange()`      | Creates evenly spaced steps  |
| `np.linspace()`    | Creates evenly spaced values |
| `np.random.rand()` | Random values                |
| `np.sin()`         | Sine values                  |
| `np.cos()`         | Cosine values                |
| `np.mean()`        | Average                      |
| `np.max()`         | Maximum                      |
| `np.min()`         | Minimum                      |

# 11. Matplotlib with Pandas

This is extremely important for Data Analysis and AI/ML.

Pandas stores data in DataFrames, and Matplotlib helps visualize it.

```
import pandas as pdimport matplotlib.pyplot as pltdata = {    "Month": ["Jan", "Feb", "Mar", "Apr"],    "Sales": [100, 200, 150, 300]}df = pd.DataFrame(data)plt.plot(df["Month"], df["Sales"], marker="o")plt.title("Monthly Sales")plt.xlabel("Month")plt.ylabel("Sales")plt.show()
```

## Pandas built-in plotting

You can also directly use:

```
df.plot(x="Month", y="Sales", kind="line")plt.show()
```

Important Pandas plot types:

```
df.plot(kind="line")df.plot(kind="bar")df.plot(kind="barh")df.plot(kind="hist")df.plot(kind="box")df.plot(kind="area")df.plot(kind="scatter", x="Age", y="Salary")
```

# 12. Correlation Heatmap Using Pandas + Seaborn + Matplotlib

Important for AI/ML

Correlation helps understand the relationship between numerical columns.

Seaborn is another Python visualization library built on top of Matplotlib.

Install:

```
pip install seaborn
```

Example:

```
import pandas as pdimport seaborn as snsimport matplotlib.pyplot as pltdata = {    "Age": [20, 21, 22, 23, 24],    "Study_Hours": [2, 3, 4, 5, 6],    "Marks": [40, 50, 60, 70, 80]}df = pd.DataFrame(data)correlation = df.corr(numeric_only=True)sns.heatmap(    correlation,    annot=True,    cmap="coolwarm")plt.title("Correlation Heatmap")plt.show()
```

[Unlocking Insights with Heatmaps: Correlation Analysis in Data Visualization | CodeSignal Learn](https://images.openai.com/static-rsc-4/q0mvOAQi1Hem7apER-f48ubF9xOql85hXw1ssxAY02G9ADTpaFRFhIcLqFAe6qxvU8u4YZRnibc56bWup_SL4w9we6TD4VTMVt7AAzUwdKsa_REVscaLd9HlKm7mc-PTqTnOxtmdLYOyWT9MlWYOhNaOqp-nXl8ljHWEmVPWGEw?purpose=inline)

[codesignal.com](https://codesignal.com/learn/courses/intro-to-data-visualization-with-titanic/lessons/unlocking-insights-with-heatmaps-correlation-analysis-in-data-visualization?utm_source=chatgpt.com)

Remember: Seaborn is separate from Matplotlib, but it uses Matplotlib for many plotting operations and customization.

# 13. Saving Graphs

Very useful when you need graphs for projects, reports, presentations and LinkedIn.

```
plt.plot(x, y)plt.title("My Graph")plt.savefig("my_graph.png")plt.show()
```

Important formats:

| Format  | Use               |
| ------- | ----------------- |
| `.png`  | Images            |
| `.jpg`  | Images            |
| `.pdf`  | Reports           |
| `.svg`  | Scalable graphics |
| `.jpeg` | Images            |

High-quality image:

```
plt.savefig(    "graph.png",    dpi=300,    bbox_inches="tight")
```

- `dpi=300`: High resolution.
- `bbox_inches="tight"`: Removes unnecessary surrounding whitespace.

Important: Save before `plt.show()` to avoid problems with some plotting backends.

# 14. Matplotlib Styles

You can change the appearance of your graph.

```
print(plt.style.available)
```

Choose a style:

```
plt.style.use("ggplot")plt.plot(x, y)plt.show()
```

Other popular styles include:

```
plt.style.use("classic")plt.style.use("dark_background")plt.style.use("bmh")
```

# 15. Important Functions – Complete Quick Reference

This is your Matplotlib revision table.

| Function             | Purpose                   |
| -------------------- | ------------------------- |
| `plt.figure()`       | Creates a figure          |
| `plt.subplots()`     | Creates figure and axes   |
| `plt.plot()`         | Line graph                |
| `plt.bar()`          | Vertical bar chart        |
| `plt.barh()`         | Horizontal bar chart      |
| `plt.scatter()`      | Scatter plot              |
| `plt.pie()`          | Pie chart                 |
| `plt.hist()`         | Histogram                 |
| `plt.boxplot()`      | Box plot                  |
| `plt.fill_between()` | Area shading              |
| `plt.stem()`         | Stem plot                 |
| `plt.step()`         | Step plot                 |
| `plt.stackplot()`    | Stacked area plot         |
| `plt.imshow()`       | Displays image or matrix  |
| `plt.colorbar()`     | Adds color scale          |
| `plt.errorbar()`     | Displays error bars       |
| `plt.axhline()`      | Horizontal reference line |
| `plt.axvline()`      | Vertical reference line   |
| `plt.title()`        | Graph title               |
| `plt.xlabel()`       | X-axis label              |
| `plt.ylabel()`       | Y-axis label              |
| `plt.legend()`       | Displays legend           |
| `plt.grid()`         | Displays grid             |
| `plt.xlim()`         | X-axis limits             |
| `plt.ylim()`         | Y-axis limits             |
| `plt.xticks()`       | X-axis ticks              |
| `plt.yticks()`       | Y-axis ticks              |
| `plt.text()`         | Adds text                 |
| `plt.annotate()`     | Adds annotations          |
| `plt.subplot()`      | Creates subplot           |
| `plt.tight_layout()` | Adjusts spacing           |
| `plt.savefig()`      | Saves figure              |
| `plt.show()`         | Displays figure           |
| `plt.close()`        | Closes figure             |

# 16. Common Errors and Their Solutions

| Error                                     | Reason                   | Solution                                 |
| ----------------------------------------- | ------------------------ | ---------------------------------------- |
| `ModuleNotFoundError`                     | Matplotlib not installed | `pip install matplotlib`                 |
| `NameError: plt`                          | Import missing           | `import matplotlib.pyplot as plt`        |
| `ValueError: x and y must have same size` | Different lengths        | Check both arrays                        |
| Graph not visible                         | `show()` missing         | Add `plt.show()`                         |
| Labels overlapping                        | Long category names      | Use `plt.xticks(rotation=45)`            |
| Graph too small                           | Figure size small        | Use `figsize=(10, 6)`                    |
| Old graphs appearing                      | Figure not cleared       | Use `plt.close()` or create a new figure |

Important rule: X and Y data must generally have matching lengths for ordinary line and scatter plots.

Example:

```
x = [1, 2, 3]y = [10, 20]  # Incorrectplt.plot(x, y)
```

Correct:

```
x = [1, 2, 3]y = [10, 20, 30]plt.plot(x, y)plt.show()
```

# 17. Matplotlib in AI/ML

Why should an AI/ML engineer learn Matplotlib?

Because ML models generate results that you need to visualize and understand.

[keras - How to visualize model training history using scikit learn's MLP classifier? - Stack Overflow](https://images.openai.com/static-rsc-4/VvlZ38WhKGYf5EuW4we9YZFNg8yWdKlINNU1MEmkr3yqsvFYD509lfSOBqTXuF0wk_eurd829udCVRb05SsBN9GyiHOGwHgbfHc9LQYqQdJQ3ikFUijDaS-u72GF-_iuTPNzJzpl3LSDeKN-o33iiWYar8y1lOr0J6SsQzG6UuQ?purpose=inline)

[Plotting Cross-Validated Predictions — scikit-learn 0.24.2 documentation](https://images.openai.com/static-rsc-4/lmAOztpogyN_r_pHf-c32Xi1DepZ_KVzsIp6lY_6t42SqBtiwqSQwkvfrxRkhRaH0-7ndbyPlgM2epFGLOtSZ1ZinEz5juupgYjk7LqnnTnuu_QVJTfIxp5Or98ED49eLf7tW6gqjvlvwU4oZKk89rFBycNf_e5gqZO2Vyf3e8o?purpose=inline)

[Confusion Matrix in Machine Learning: Theory, Code, and Visualization | by MD AMAN | Medium](https://images.openai.com/static-rsc-4/oHAJYy6BMFISwFIr21V4eVhp_sIbjN-2nhOppCye3jPG1K5Mp770LGx_gp7doqgn5ACJ4aNWBcc_vItHMwAtNXoYDPqDLZ19RFN1ri-0w--fAHfNeVfCSmaah-XBvmh_zayYgRDo1uKZvCdGCRMwN-ezEKaUZL6OvI34rFina8M?purpose=inline)

[Mastering ROC Curves: Plotting Classifiers with Sklearn - codepointtech.com](https://images.openai.com/static-rsc-4/mgy3-dp_oaItGjdp_SfMzw2u5VvRSdMVcJ5_5gjNcFGRc_sxBt4r3U7-L9E0f31JmSuvAcIf-JYXgNatvzl1rHPol_CzfjHLeTjHw9vDsHvEwRlXGF3XVdGrgPUC0lCP8-uxnWDhTQGAOUg51fJYc5XEm073SX1g22KUxuVdgr4?purpose=inline)

[Sensor-to-Image Based Neural Networks: A Reliable Reconstruction Method for Diffuse Optical Imaging of High-Scattering Media | MDPI](https://images.openai.com/static-rsc-4/VKzsCF56yPzk6L7ZDQpCAt52_hp9PmRoFF_KW6Tt2uP1hOSWRTTgJAoCWkf8PoCS63kct5XV5Z1eFsvDcGMAcFU85oDD3hZPBXR6pLGJMNCwqWqQXLMSF3ou7SpuNNgjmZ355Faq9byfFRYTjyWF7Sa8FT9UGmyuOoGtuHIxKHY?purpose=inline)

[Salary Dataset - Simple linear regression | Kaggle](https://images.openai.com/static-rsc-4/hmCv-BTHvQLI36BedLW6pvzsY34ruLSDeC6GAcyKzOTz514OSpeD-RS0_6QCTW21yGBSdAuV4jOWKvwIFDikX6BP_BoeH8NvF38CvXM-avlkLD0H9q2kY6P7gcpERdRiKD_jmZ6PgnG4XQnuX4D6D7-NVHafeiK-htPrxa07FDc?purpose=inline)

[Create a confusion matrix with Python](https://images.openai.com/static-rsc-4/XDWYUV1a07KYUEr3RUQRWpq3QNy9Sr0wJPSRHtY5Xmr8fF16cpXdkUmqwaXLxbRrmEfbFpVyyUFlMLKwrD1xbWFLb06-uT4i_UQYXHcavKqtoHtJx_RkD3VDEKeGYqJ2qraWLyw0U5a3h_kNhIH1NwDR6Y6JBgKJfTsMWQS7JWA?purpose=inline)

[Intro — ML with Python: Part 2 of 4 — Binary Classification | by David Liang | Medium](https://images.openai.com/static-rsc-4/zjBrhMhiXHOCxmTf03zSMsacOzfyT3kRZjOz2HOostC0UZ0CskHepZI3I54aKFklIQ-Bacge-Kl-d2DLeIqzr-1OhhgDL-qV1ogXbChrT4rkrY2byfNlZArIjMYiVPDRiERspCIOWRKWb3MpSWze0To2vmgHV-bvU3mqH2pJ93g?purpose=inline)

| AI/ML Task           | Visualization            |
| -------------------- | ------------------------ |
| Data distribution    | Histogram                |
| Feature relationship | Scatter plot             |
| Feature correlation  | Heatmap                  |
| Outlier detection    | Box plot                 |
| Model training       | Loss curve               |
| Model performance    | Accuracy graph           |
| Classification       | Confusion matrix         |
| Regression           | Actual vs predicted plot |
| Model evaluation     | ROC curve                |

## Example 1: ML Training Loss Graph

```
import matplotlib.pyplot as pltepochs = [1, 2, 3, 4, 5, 6]loss = [0.9, 0.7, 0.5, 0.35, 0.2, 0.1]plt.plot(epochs, loss, marker="o")plt.title("Model Training Loss")plt.xlabel("Epochs")plt.ylabel("Loss")plt.grid(True)plt.show()
```

EL10: Training ke saath loss decrease ho raha hai, which can indicate that the model is learning. However, validation performance is also needed to check overfitting.

## Example 2: Actual vs Predicted Values

```
actual = [10, 20, 30, 40, 50]predicted = [12, 18, 32, 38, 48]plt.scatter(actual, predicted)plt.xlabel("Actual Values")plt.ylabel("Predicted Values")plt.title("Actual vs Predicted")plt.show()
```

## Example 3: Confusion Matrix

```
import matplotlib.pyplot as pltfrom sklearn.metrics import confusion_matrix, ConfusionMatrixDisplayactual = [0, 0, 1, 1, 0, 1]predicted = [0, 1, 1, 1, 0, 0]cm = confusion_matrix(actual, predicted)display = ConfusionMatrixDisplay(confusion_matrix=cm)display.plot(cmap="Blues")plt.title("Confusion Matrix")plt.show()
```

This is useful for evaluating classification models.




# 18. Your Matplotlib Learning Roadmap

| Phase | Topics                                | Priority   |
| ----- | ------------------------------------- | ---------- |
| 1     | Installation, import, basic plots     | Must learn |
| 2     | Line, bar, scatter, pie               | Must learn |
| 3     | Histogram, boxplot, area plot         | Must learn |
| 4     | Colors, labels, legends, grid         | Must learn |
| 5     | Subplots, Figure and Axes             | Must learn |
| 6     | NumPy + Pandas integration            | Must learn |
| 7     | Heatmaps, annotations, advanced plots | Important  |
| 8     | ML visualization and projects         | Important  |


My recommendation: Don't just memorize Matplotlib functions. Practice each graph using a real CSV dataset. That's how you'll use it in actual AI/ML projects.

                             THANK YOU 