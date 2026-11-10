# Complete Seaborn Tutorial



Phase 02 — Python for Data

Beginner to Advanced



Complete Detailed Notes for AI/ML and Data Science

Seaborn is one of the most important Python libraries for Data Visualization. It helps you understand datasets, identify patterns, find relationships between variables, and perform Exploratory Data Analysis (EDA).

These notes cover Seaborn from basic concepts to advanced visualizations, with definitions, syntax, examples, code, and practice questions.

# 1. Introduction to Seaborn

## 1.1 What is Seaborn?

Definition: Seaborn is a Python data visualization library built on top of Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics.

Easy Explanation (Hinglish):

Seaborn ka use hum data ko graphs aur charts ke through visualize karne ke liye karte hain. Isse hum easily understand kar sakte hain ki data mein kya patterns, relationships, trends aur outliers present hain.

For example:

- Students ke marks ka distribution.
- Sales aur profit ke beech relationship.
- Age aur salary ka comparison.
- Different categories ki performance.
- Dataset mein outliers identify karna.

## 1.2 Why do we use Seaborn?

1. Attractive and professional visualizations.
2. Easy statistical visualization.
3. Works directly with Pandas DataFrames.
4. Supports categorical and numerical data.
5. Helps in Exploratory Data Analysis (EDA).
6. Helps identify correlations and relationships.
7. Provides built-in datasets.
8. Simplifies complex visualizations.

## 1.3 Seaborn vs Matplotlib

| Feature            | Matplotlib                   | Seaborn                       |
| ------------------ | ---------------------------- | ----------------------------- |
| Level              | Low-level                    | High-level                    |
| Syntax             | More code                    | Less code                     |
| Design             | Basic/customizable           | Attractive defaults           |
| DataFrame support  | Manual handling often needed | Excellent                     |
| Statistical graphs | Requires more work           | Built-in                      |
| Customization      | Very powerful                | Powerful, built on Matplotlib |

Important: Seaborn is built on Matplotlib. You can use both libraries together.

# 2. Installing and Importing Seaborn

## 2.1 Installation

Open your VS Code terminal or Command Prompt:

```
pip install seaborn
```

Install other important libraries:

```
pip install numpy pandas matplotlib
```

## 2.2 Import Libraries

```
import numpy as npimport pandas as pdimport matplotlib.pyplot as pltimport seaborn as sns
```

Explanation:

- `numpy`: Numerical operations.
- `pandas`: Data manipulation.
- `matplotlib.pyplot`: Plotting and customization.
- `seaborn`: Statistical data visualization.

## 2.3 Check Seaborn Version

```
print(sns.__version__)
```

## 2.4 Basic Seaborn Example

```
import seaborn as snsimport matplotlib.pyplot as pltdata = [10, 20, 30, 40, 50]sns.lineplot(x=range(5), y=data)plt.show()
```

Output: A line graph displaying values from 10 to 50.

# 3. Understanding Seaborn Datasets

Seaborn provides built-in datasets for learning and practice.

## 3.1 Load a Dataset

```
import seaborn as snsdf = sns.load_dataset("tips")print(df)
```

The `tips` dataset contains restaurant bill and tip information.

## 3.2 Important Built-in Datasets

| Dataset  | Description                   |
| -------- | ----------------------------- |
| tips     | Restaurant bills and tips     |
| iris     | Flower measurements           |
| titanic  | Titanic passenger information |
| penguins | Penguin measurements          |
| flights  | Monthly airline passengers    |
| diamonds | Diamond characteristics       |
| mpg      | Vehicle fuel efficiency       |
| exercise | Exercise study data           |
| planets  | Exoplanet discovery data      |

## 3.3 Explore the Dataset Using Pandas

```
df = sns.load_dataset("tips")print(df.head())print(df.tail())print(df.shape)print(df.columns)print(df.info())print(df.describe())print(df.isnull().sum())
```

Remember: Before creating visualizations, understand your dataset.

# 4. Seaborn Plot Categories

Seaborn provides different categories of visualization functions.

Seaborn Visualization Map

SEABORN

Relational Plots

Relationship between variables

- Scatter
- Line

Distribution Plots

Data distribution

- Histogram
- KDE
- ECDF

Categorical Plots

Category comparisons

- Bar
- Box
- Violin
- Strip

Matrix Plots

Matrix relationships

- Heatmap
- Cluster map

Other important plots: Regression plots, pair plots, joint plots, FacetGrid and relational figure-level plots.

# 5. Relational Plots

Relational plots show relationships between two or more numerical variables.

There are two main relational plots:

1. Scatter Plot
2. Line Plot

## 5.1 Scatter Plot

[Introduction to Seaborn for dataviz with Python](https://images.openai.com/static-rsc-4/h7BYGHQNqF1X0hsu5IfhjSKpzjdrMZiW23qwe4HzaNNi-VOSM6lO2mSVD-D8uG6j5ACUTEGzsBU-uLLlCalBX-xXOIxAfOWHlHkMhzKi_Tyk60qezGzHiSAyj40_MpsR4x1kOWfnFEk4MJ9iyTtw5utu_qLJykNNChyF8abeT-g?purpose=inline)

[python-graph-gallery.com](https://python-graph-gallery.com/seaborn/?utm_source=chatgpt.com)

Definition: A scatter plot is a graph that displays the relationship between two numerical variables using individual data points.

Use cases:

- Study hours vs marks.
- Experience vs salary.
- Height vs weight.
- Advertising cost vs sales.

Syntax:

```
sns.scatterplot(    data=df,    x="total_bill",    y="tip")plt.show()
```

### Important Parameters

| Parameter | Purpose                      |
| --------- | ---------------------------- |
| `data`    | Dataset                      |
| `x`       | X-axis variable              |
| `y`       | Y-axis variable              |
| `hue`     | Different colors by category |
| `style`   | Different marker styles      |
| `size`    | Different marker sizes       |
| `alpha`   | Transparency                 |

### Example: Scatter Plot with Hue

```
df = sns.load_dataset("tips")sns.scatterplot(    data=df,    x="total_bill",    y="tip",    hue="sex")plt.title("Bill vs Tip")plt.show()
```

Explanation: The `hue` parameter gives different colors to different categories.

### Example: Multiple Features

```
sns.scatterplot(    data=df,    x="total_bill",    y="tip",    hue="day",    style="sex",    size="size")plt.show()
```

## 5.2 Line Plot

[seaborn.lineplot — seaborn 0.11.2 documentation](https://images.openai.com/static-rsc-4/QE9nepFWfnanj-dyGpmRf41cAu_GG91_Aq4Pj0ut9ynoSNUsO9SwRn99I6pUoNtEqnpESWVnoLR2OxgxTWEnRmn7EqJ7pcMdwWSNPr-TwOM1yuwJotTJz2iAjSMD_GTa9v7CYxBlNeF5jHSuShw8U8YMyR0LIqr2MkxkGCj_VJI?purpose=inline)

[seaborn.pydata.org](https://seaborn.pydata.org/archive/0.11/generated/seaborn.lineplot.html?highlight=lineplot\&utm_source=chatgpt.com)

Definition: A line plot displays data points connected by lines. It is useful for understanding trends and changes over continuous variables.

Use cases:

- Monthly sales.
- Temperature changes.
- Stock prices.
- Student performance over time.

Syntax:

```
sns.lineplot(    data=df,    x="day",    y="total_bill")plt.show()
```

Example:

```
flights = sns.load_dataset("flights")sns.lineplot(    data=flights,    x="year",    y="passengers")plt.title("Yearly Passengers")plt.show()
```

### Important Parameters

- `hue`: Different colored lines.
- `style`: Different line styles.
- `markers`: Show markers.
- `errorbar`: Show uncertainty intervals.
- `estimator`: Aggregation function, default is mean for repeated observations.

```
sns.lineplot(    data=flights,    x="year",    y="passengers",    marker="o")plt.show()
```

Difference:

- Scatter plot: Shows individual observations.
- Line plot: Shows trends and connected observations; repeated x-values may be aggregated.

# 6. Distribution Plots

Distribution plots help us understand how numerical data is distributed.

They answer questions like:

- What is the average range?
- Is the data normally distributed?
- Are there outliers?
- Is the data skewed?
- Where are most values concentrated?

Important distribution plots:

1. Histogram
2. KDE Plot
3. ECDF Plot
4. Rug Plot

## 6.1 Histogram

[seaborn.histplot — seaborn 0.13.2 documentation](https://images.openai.com/static-rsc-4/GoWj_ElyipkidKf47npJUva9Dxaj0bwZNnBqOk0ZaAPTGwe08t6FrnHQbOWobFAzfYLkkLufjcIEQwG-i326Ct5gcLuN_c5zxPImq32CWaUEFVPyP2f_nrAr0eCHsTnrhq9RZbmPKu5vej1orfbG91zMznLPSZeqpnGsDSjboNM?purpose=inline)

[seaborn.pydata.org](https://seaborn.pydata.org/generated/seaborn.histplot.html?utm_source=chatgpt.com)

Definition: A histogram represents numerical data using bars, where each bar shows the frequency of observations within a particular interval (bin).

Syntax:

```
sns.histplot(    data=df,    x="total_bill")plt.show()
```

### Important Parameters

| Parameter | Meaning                                |
| --------- | -------------------------------------- |
| `bins`    | Number of intervals                    |
| `kde`     | Adds density curve                     |
| `color`   | Bar color                              |
| `stat`    | Count, frequency, density, probability |
| `element` | Bar, step, poly                        |
| `hue`     | Separate distributions by category     |

Example:

```
sns.histplot(    data=df,    x="total_bill",    bins=20,    kde=True,    color="skyblue")plt.title("Distribution of Total Bill")plt.show()
```

What is bins?

Bins divide numerical data into intervals.

For example, marks from 0–100 can be divided into:

- 0–20
- 20–40
- 40–60
- 60–80
- 80–100

## 6.2 KDE Plot

[seaborn.kdeplot — seaborn 0.13.2 documentation](https://images.openai.com/static-rsc-4/HUqdo4kyFZYI4YuC71_5oALW1vOs9XoQ-G275YLXIujV_KLPijm8c_9lMWVwTPR18G3c5BiBX8zfS3Si4Jwmi_ohcsTtVYGwEoXznaXmZpNTLErn-p0RZlqWBB34IkvJ7CY53AZrFsBshg5c8fSMYujfc0CeqPBNXhJuN7GxlFA?purpose=inline)

[seaborn.pydata.org](https://seaborn.pydata.org/generated/seaborn.kdeplot.html?utm_source=chatgpt.com)

Definition: KDE (Kernel Density Estimation) is a statistical technique used to estimate the probability density distribution of continuous numerical data.

Easy explanation: Histogram bars ki jagah KDE ek smooth curve show karta hai jo data ka distribution batata hai.

Syntax:

```
sns.kdeplot(    data=df,    x="total_bill")plt.show()
```

Example:

```
sns.kdeplot(    data=df,    x="total_bill",    fill=True,    color="blue")plt.show()
```

Important parameters:

- `fill=True`: Fill area below curve.
- `hue`: Compare categories.
- `bw_adjust`: Adjust smoothness.
- `cumulative=True`: Cumulative density.

## 6.3 ECDF Plot

[seaborn.ecdfplot — seaborn 0.13.2 documentation](https://images.openai.com/static-rsc-4/My9dsFTGKX6wnM6VGlfskLehoWSnkMMEZrW-NJ5M2SFWtc2voWQjIOZbSOtKawgOGiDCrUqJ2AKc1dif7ReI-hGfQxyhj0ewmH19q6UKxjqhyv5m6fzdXVyyG6rfsRcel365f8zEuF2ggL3GaW821GBGpdOkETl6aObk9pIu3KA?purpose=inline)

[seaborn.pydata.org](https://seaborn.pydata.org/generated/seaborn.ecdfplot.html?utm_source=chatgpt.com)

Definition: ECDF (Empirical Cumulative Distribution Function) shows the proportion of observations less than or equal to each value.

```
sns.ecdfplot(    data=df,    x="total_bill")plt.show()
```

Use: Understand what percentage of observations falls below a particular value.

## 6.4 Rug Plot

[Visualizing Data in Python With Seaborn – Real Python](https://images.openai.com/static-rsc-4/PFhLa5QSbpgQ1w5qdG0bsuXGwL6Ngjua5EitQtDuJIwzNHEahONIH--6isUEGLtPAHY5aD5P3cGHIO-AP7Nz2c91pxqi99wKHDp8j7vh6p34uQhdNYygSCLSKjFq2ufZQfTU-ghqmvELnIQOu5aKBbzntzw-Hvs1ZsL_0FKQ6s4?purpose=inline)

[realpython.com](https://realpython.com/python-seaborn/?utm_source=chatgpt.com)

Definition: A rug plot displays individual data observations as small marks along an axis.

```
sns.rugplot(    data=df,    x="total_bill")plt.show()
```

## 6.5 Distribution Plot Comparison

| Plot      | Main Purpose                |
| --------- | --------------------------- |
| Histogram | Frequency distribution      |
| KDE       | Smooth density distribution |
| ECDF      | Cumulative proportion       |
| Rug       | Individual observations     |

# 7. Categorical Plots

Categorical plots are used to compare values across different categories or groups.

Example:

- Male vs Female salary.
- Sales by product category.
- Marks by department.
- Tips by restaurant day.

Important categorical plots:

1. Bar Plot
2. Count Plot
3. Box Plot
4. Violin Plot
5. Strip Plot
6. Swarm Plot
7. Boxen Plot
8. Point Plot

## 7.1 Bar Plot

[seaborn.barplot — seaborn 0.12.2 documentation](https://images.openai.com/static-rsc-4/k67WNzWCKpKXp5nTZ5gzyG5Q3SMbmbpEDbWiwBAnup0QjZIA52U9GZE4mBkBm5RYcgRpa3g37kKUMBNG9_2XlE5BhKG4_szQG0f1PKedNbrX0qYyBH6oX6k9tKs_Nxa0b3D9P7ADwZeVTR62vb-gZAuGKvRnDnSPR1kjaEW8n6g?purpose=inline)

[seaborn.pydata.org](https://seaborn.pydata.org/archive/0.12/generated/seaborn.barplot.html?utm_source=chatgpt.com)

Definition: A bar plot represents an aggregate value of a numerical variable for each category.

For example, average tips for each day.

Syntax:

```
sns.barplot(    data=df,    x="day",    y="tip")plt.show()
```

Important: `barplot()` generally calculates the mean of the numerical variable for each category by default.

Example:

```
sns.barplot(    data=df,    x="day",    y="total_bill",    hue="sex",    errorbar=None)plt.title("Average Bill by Day and Gender")plt.show()
```

Important parameters:

| Parameter   | Purpose              |
| ----------- | -------------------- |
| `x`         | Categories           |
| `y`         | Numerical values     |
| `hue`       | Additional category  |
| `estimator` | Aggregation function |
| `errorbar`  | Uncertainty interval |
| `order`     | Category order       |
| `palette`   | Color palette        |

Change estimator:

```
import numpy as npsns.barplot(    data=df,    x="day",    y="tip",    estimator=np.median)plt.show()
```

Here, the bar height represents the median instead of the mean.

## 7.2 Count Plot

[seaborn.countplot — seaborn 0.13.2 documentation](https://images.openai.com/static-rsc-4/SUcjPqErdbzu24uPSYP0_yu0srRmX5kF781mdvbkEU8uSPdoR0l39KxPCp6davQhyKCTJy58yUoH7ORHlTaeBE3tsBK1l0SXNOWxSvk8NiVDcNO3Mlc8pWJYXUkPzA109AZmgqvhY45SJf4A0pKnm80po0nblhDDzl2NLT9NPFo?purpose=inline)

[seaborn.pydata.org](https://seaborn.pydata.org/generated/seaborn.countplot.html?utm_source=chatgpt.com)

Definition: A count plot displays the number of observations in each category.

Syntax:

```
sns.countplot(    data=df,    x="day")plt.show()
```

Example:

```
sns.countplot(    data=df,    x="sex",    hue="smoker")plt.title("Customer Count by Gender and Smoking Status")plt.show()
```

Difference between Bar Plot and Count Plot

| Bar Plot                         | Count Plot                    |
| -------------------------------- | ----------------------------- |
| Shows aggregated numerical value | Shows frequency               |
| Requires numerical variable      | Requires categorical variable |
| Default estimator is mean        | Counts observations           |

## 7.3 Box Plot

[Seaborn Boxplot - How to Create Box and Whisker Plots • datagy](https://images.openai.com/static-rsc-4/Go2wzLw56SJI2eauNLGY-Bo2VjOTG6dfn5YzmJJFVAnC2r_Opmhyaco6YjiqR3RJR6bXMCogwRc5xzfzSAtTyQcsI21-qjcuJq2ZqNn9pIWONdzIlNvTICdd6L-6ljJWBY0_VuXUPipJsVkZ0LsrdIRSeHicG5QPgOgb7K9zqVU?purpose=inline)

[datagy.io](https://datagy.io/seaborn-boxplot/?utm_source=chatgpt.com)

Definition: A box plot displays the distribution of numerical data using quartiles, median, whiskers and potential outliers.

It is especially useful for identifying outliers.

### Five-Number Summary

1. Minimum
2. First Quartile (Q1)
3. Median (Q2)
4. Third Quartile (Q3)
5. Maximum

[Chapter 2: The Middle and the Mess — A Little Bit of Everything in Biostatistics for Health Science Students](https://images.openai.com/static-rsc-4/OUce9PnoLYaB4sJ8wuK0QkiKKkxwq41Hu_rmehZdZoEMsiwz4XmlTrRBSQ_8_8EZZkNLY2RKXF2JZAY_7aSvVtTt0RGgXbDCo3f4XNzVGlu6pc-ARWZr6zdQOnshg5obqFP3aTQ8aaG2h8XPeQ_K1L-c7Avhrmwxy8Mk09lkbNU?purpose=inline)

[paytonyau.github.io](https://paytonyau.github.io/biostats-book/chapters/02_middle.html?utm_source=chatgpt.com)

### Important Concepts

- Q1: 25th percentile.
- Q2: 50th percentile (Median).
- Q3: 75th percentile.
- IQR: Interquartile Range.

Formula:

\\[ IQR = Q3-Q1 \\]

Common box-plot outlier rule:

\\[ Lower = Q1-1.5(IQR) \\]

\\[ Upper = Q3+1.5(IQR) \\]

Values outside these limits are plotted as potential outliers.

### Syntax

```
sns.boxplot(    data=df,    x="day",    y="total_bill")plt.show()
```

Example:

```
sns.boxplot(    data=df,    x="day",    y="tip",    hue="sex")plt.title("Tip Distribution by Day")plt.show()
```

Real-world use: Finding unusual salary values, transaction amounts, exam marks, etc.

## 7.4 Violin Plot

[Is it possible to draw a split violinplot? - HoloViews - HoloViz Discourse](https://images.openai.com/static-rsc-4/muL4_jqtb0UzvnoQsmr84IEsfucLsH4KMdKdD2vahZW06Q6n_SZxmBmQOlyY3kxopLzFfyREAVyCw4VQlB1wW1Ay7lnS3pHSWt1nHHrM7oPOkgB6wgAT1Q-sHxV52rYpp7V_Vkl9brG2C5IqMTnYP0WU1NQjmfP8p9p0Zc50ukg?purpose=inline)

[discourse.holoviz.org](https://discourse.holoviz.org/t/is-it-possible-to-draw-a-split-violinplot/54?utm_source=chatgpt.com)

Definition: A violin plot combines a box plot with a KDE-style density representation to show the distribution and concentration of data.

Syntax:

```
sns.violinplot(    data=df,    x="day",    y="total_bill")plt.show()
```

Example:

```
sns.violinplot(    data=df,    x="day",    y="tip",    hue="sex",    inner="quart")plt.show()
```

Important parameters:

- `inner`: Show quartiles, box, points or nothing.
- `split`: Split two hue categories into halves when supported by the category structure.
- `density_norm`: Controls width normalization.
- `cut`: Controls how far density extends beyond observed values.

## 7.5 Strip Plot

[Seaborn stripplot: Jitter Plots for Distributions of Categorical Data • datagy](https://images.openai.com/static-rsc-4/NadkQjYDS2mi7yrR72PA9OGMGuA7W_xBycpo3W5B0lukFx2mNkCAIiXXzmqakphvxRCpuibsgrG6I_lAd9zA017g4P5a4SSLMEVIJDNH67472mgtlMPr6yqc3rxutRfQtBSBvuVaJCy69F1shySXuYk77tX8jAORrHs2fJdSFFQ?purpose=inline)

[datagy.io](https://datagy.io/seaborn-stripplot/?utm_source=chatgpt.com)

Definition: A strip plot displays individual observations as points along categorical groups.

```
sns.stripplot(    data=df,    x="day",    y="total_bill")plt.show()
```

Important parameter:

`jitter=True` adds small random horizontal displacement to help prevent overlapping points.

```
sns.stripplot(    data=df,    x="day",    y="tip",    jitter=True,    hue="sex")plt.show()
```

## 7.6 Swarm Plot

[seaborn.swarmplot — seaborn 0.11.2 documentation](https://images.openai.com/static-rsc-4/bLq55kinALDfighdeQ7w_wh_reSs-slH7OCjNaPPZ2eiBfQVrEMSNee-5-94On7IlnMYJaE_N81MrasAD2_DLha-CZMPR7Pw2rzsdhGd1TvGwdPFoEOJKeJODgm-QNNSEjPBB4MBApytWW9yzopOfOFLXXAiFXsUGPOinXV8rk0?purpose=inline)

[seaborn.pydata.org](https://seaborn.pydata.org/archive/0.11/generated/seaborn.swarmplot.html?utm_source=chatgpt.com)

Definition: A swarm plot displays individual observations without overlapping points, arranging them within categorical groups.

```
sns.swarmplot(    data=df,    x="day",    y="total_bill")plt.show()
```

Difference: Strip Plot vs Swarm Plot

- Strip plot: Points may overlap.
- Swarm plot: Attempts to prevent point overlap.
- Swarm plot may become slow with large datasets.

## 7.7 Boxen Plot

[seaborn.boxenplot — seaborn 0.13.2 documentation](https://images.openai.com/static-rsc-4/VPRZeJwxdjxdVCYfdBp-U8fDV5BXqSc8VXcHVVRY-mU_dutf6JhXgcd-nIKSxBjkJp4BrR3wAvKYT06Vab0RQajcVXSIAHIPyL1mfcA_ioTOJJ6FBoj8YQC1M2AI9DR0rrFHwt5IeFx2218aNl--6HJAZqbWx8qJiAIcgiShj4E?purpose=inline)

[seaborn.pydata.org](https://seaborn.pydata.org/generated/seaborn.boxenplot.html?utm_source=chatgpt.com)

Definition: A boxen plot (letter-value plot) displays distribution information through multiple quantiles and is particularly useful for larger datasets.

```
sns.boxenplot(    data=df,    x="day",    y="total_bill")plt.show()
```

## 7.8 Point Plot

Definition: A point plot represents an estimated statistical value for each category, using points and often connecting lines to highlight differences.

```
sns.pointplot(    data=df,    x="day",    y="tip",    hue="sex")plt.show()
```

## 7.9 Categorical Plots Comparison

| Plot   | What it shows                    |
| ------ | -------------------------------- |
| Bar    | Average or another aggregate     |
| Count  | Number of observations           |
| Box    | Median, quartiles and outliers   |
| Violin | Distribution and density         |
| Strip  | Individual points                |
| Swarm  | Non-overlapping points           |
| Boxen  | Detailed quantile distribution   |
| Point  | Estimated values and differences |

# 8. Regression Plots

Regression plots help us understand the relationship between variables and visualize trends using statistical models.

They are useful in machine learning and statistical analysis.

## 8.1 Regplot

[Estimating regression fits — seaborn 0.13.2 documentation](https://images.openai.com/static-rsc-4/uHe63035_CqAWGADIrHG03kZInoaB2_qpz58qBjyMc-9aNwDOXBxK-N_ZvGx_raCEVQk17cObw3hOoRMDPQh5elsPYNN1KGuFxbfxr0Q7d5O7oppg_XKTYb4QlvIg0Sr_Uz9mANIoHhTcpFfrKyh9UX9PaeNBXjPyUJad4iSOnY?purpose=inline)

[seaborn.pydata.org](https://seaborn.pydata.org/tutorial/regression.html?utm_source=chatgpt.com)

Definition: A regression plot displays a scatter plot with a fitted regression line and, by default, a confidence interval.

Syntax:

```
sns.regplot(    data=df,    x="total_bill",    y="tip")plt.show()
```

Example:

```
sns.regplot(    data=df,    x="total_bill",    y="tip",    color="blue",    ci=95)plt.title("Bill vs Tip Regression")plt.show()
```

Important parameters:

- `order`: Polynomial regression order.
- `ci`: Confidence interval.
- `scatter`: Display scatter points.
- `fit_reg`: Not a current regplot argument; use `scatter=False` or `sns.lmplot` options as appropriate.
- `logistic`: Fit logistic regression.

## 8.2 Lmplot

Definition: `lmplot()` combines regression plotting with FacetGrid functionality to show relationships across categories or subsets.

```
sns.lmplot(    data=df,    x="total_bill",    y="tip",    hue="sex")plt.show()
```

## 8.3 Residplot

Definition: A residual plot displays the difference between actual values and predicted values against a predictor variable.

Residual:

\\[ Residual = Actual - Predicted \\]

```
sns.residplot(    data=df,    x="total_bill",    y="tip")plt.show()
```

Why use residual plots?

- Check regression model assumptions.
- Identify non-linear patterns.
- Detect unusual observations.
- Evaluate model fit.

# 9. Matrix Plots

Matrix plots are used to visualize data arranged in rows and columns, especially correlations and relationships between multiple numerical features.

Important matrix plots:

1. Heatmap
2. Cluster Map

## 9.1 Heatmap

[Unlocking Insights with Heatmaps: Correlation Analysis in Data Visualization | CodeSignal Learn](https://images.openai.com/static-rsc-4/q0mvOAQi1Hem7apER-f48ubF9xOql85hXw1ssxAY02G9ADTpaFRFhIcLqFAe6qxvU8u4YZRnibc56bWup_SL4w9we6TD4VTMVt7AAzUwdKsa_REVscaLd9HlKm7mc-PTqTnOxtmdLYOyWT9MlWYOhNaOqp-nXl8ljHWEmVPWGEw?purpose=inline)

[codesignal.com](https://codesignal.com/learn/courses/intro-to-data-visualization-with-titanic/lessons/unlocking-insights-with-heatmaps-correlation-analysis-in-data-visualization?utm_source=chatgpt.com)

Definition: A heatmap represents numerical values using different colors in a matrix format.

One of the most important plots for Data Science and Machine Learning.

### What is Correlation?

Correlation measures the strength and direction of a relationship between two numerical variables.

Correlation coefficient ranges from -1 to +1.

| Value | Meaning                      |
| ----- | ---------------------------- |
| +1    | Perfect positive correlation |
| 0     | No linear correlation        |
| -1    | Perfect negative correlation |

### Create a Correlation Matrix

First, select numerical columns:

```
numeric_df = df.select_dtypes(include="number")
```

Calculate correlation:

```
corr = numeric_df.corr()print(corr)
```

Create heatmap:

```
sns.heatmap(    corr,    annot=True,    cmap="coolwarm")plt.title("Correlation Heatmap")plt.show()
```

Important parameters:

| Parameter    | Purpose             |
| ------------ | ------------------- |
| `data`       | Matrix data         |
| `annot=True` | Display values      |
| `cmap`       | Color scheme        |
| `linewidths` | Space between cells |
| `fmt`        | Number formatting   |
| `vmin`       | Minimum color value |
| `vmax`       | Maximum color value |
| `cbar`       | Display color bar   |
| `mask`       | Hide selected cells |

### Advanced Heatmap

```
corr = numeric_df.corr()mask = np.triu(    np.ones_like(corr, dtype=bool))sns.heatmap(    corr,    annot=True,    cmap="coolwarm",    fmt=".2f",    linewidths=0.5,    mask=mask,    vmin=-1,    vmax=1)plt.title("Advanced Correlation Heatmap")plt.show()
```

Why mask?

`np.triu()` creates an upper-triangle mask, so you can display only one half of the symmetric correlation matrix.

### Important ML Application

Heatmaps help identify:

- Highly correlated features.
- Possible multicollinearity.
- Relationships among numerical variables.
- Features that may need further investigation.

Remember: Correlation does not imply causation.

## 9.2 Cluster Map

[Seaborn all Graphs with explanation | by Rudra Prasad Bhuyan | Medium](https://images.openai.com/static-rsc-4/l21YZVJpReKq6gfIQOxu8HKzPoE05Tpvcxoliyi19LhyqVoucGuNb6GRaGSodLflTwc5GYl0QQyxFCEGv4k_Jy5z67gr3AqtM-OPy4BOXHW_6_gR-4ILPE5-xbJhxEgv-cfLmDlLw7BCp9hB01HK7SCQY43xSI7oAv7EtBL_82I?purpose=inline)

[medium.com](https://medium.com/%40rudraprasadbhuyan999/seaborn-all-graphs-with-explanation-dad59632111b?utm_source=chatgpt.com)

Definition: A cluster map performs hierarchical clustering on rows and columns and visualizes the reordered data as a heatmap.

```
sns.clustermap(    numeric_df.corr(),    cmap="coolwarm",    annot=True)plt.show()
```

Difference:

- Heatmap: Displays values in the given order.
- Cluster map: Groups similar rows and columns based on hierarchical clustering.

# 10. Multi-Variable Visualization

These plots help visualize relationships between multiple variables simultaneously.

## 10.1 Pair Plot

[Bài 7: Trực quan hoá dữ liệu với Matplotlib và Seaborn](https://images.openai.com/static-rsc-4/XB1s5Yz-emJKaOyEJCEJkJEcT0sMDDAE1UKxubnm4d7w1_jNjWH5yJc4VGfbZf-rANO1wgMMRKBc9-DgX6nz6R_FBEx5tX43XvRJoaROxLCAETjAxKX79uwySAaoy_Xpyr4tlbDrVuHSSwJfxlgUlXcQ3_MbnKNZNpnaZDcP-0E?purpose=inline)

[zootopi.dev](https://www.zootopi.dev/docs/tutorial/python/09.visualization?utm_source=chatgpt.com)

Definition: A pair plot creates a grid of plots to visualize pairwise relationships among numerical variables in a dataset.

Syntax:

```
iris = sns.load_dataset("iris")sns.pairplot(iris)plt.show()
```

Example with hue:

```
sns.pairplot(    iris,    hue="species")plt.show()
```

Important parameters:

- `hue`: Separate categories by color.
- `vars`: Select specific numerical variables.
- `kind`: Scatter or KDE.
- `diag_kind`: Histogram or KDE on diagonal.
- `corner=True`: Display only one triangle.

Example:

```
sns.pairplot(    iris,    hue="species",    corner=True,    diag_kind="hist")plt.show()
```

Use in ML: Pair plots are helpful during EDA to understand feature relationships and possible class separation.

## 10.2 Joint Plot

[Scatter plot with marginal histograms in seaborn | PYTHON CHARTS](https://images.openai.com/static-rsc-4/7DxKR9QuFNe_fbfcHYzNy33cD6KuCjsH7qaXBomKVJWAocOJKeG0SylVvv8pFqoQQTwG2j4nIRr7XJXrRS5XJV1COAjQ6-EhL-qkj-SzpfzMVVHzb7Ab1DEGCjekJmEQVxNzF02ZwRdu5yAWIRufg7dg8bRniMt-E7XS0QvJDCo?purpose=inline)

[python-charts.com](https://python-charts.com/correlation/scatter-plot-marginal-histograms-seaborn/?utm_source=chatgpt.com)

Definition: A joint plot displays the relationship between two numerical variables along with their individual distributions.

```
sns.jointplot(    data=df,    x="total_bill",    y="tip")plt.show()
```

Different kinds:

```
sns.jointplot(    data=df,    x="total_bill",    y="tip",    kind="reg")plt.show()
```

Available kinds include:

- `scatter`
- `kde`
- `hist`
- `hex`
- `reg`
- `resid`

## 10.3 FacetGrid

Definition: FacetGrid creates a grid of subplots based on categorical variables, allowing the same visualization to be compared across groups.

```
g = sns.FacetGrid(    df,    col="sex",    row="smoker")g.map_dataframe(    sns.scatterplot,    x="total_bill",    y="tip")plt.show()
```

## 10.4 Relplot

Definition: `relplot()` is a figure-level interface for creating relational plots across multiple subsets.

```
sns.relplot(    data=df,    x="total_bill",    y="tip",    hue="sex",    col="time",    kind="scatter")plt.show()
```

It supports scatter and line plots.

# 11. Seaborn Styling and Customization

Visualization is not only about creating graphs. A professional data scientist should also know how to customize them.

## 11.1 Set Plot Style

Seaborn provides different styles:

```
sns.set_style("whitegrid")
```

Available styles:

- `darkgrid`
- `whitegrid`
- `dark`
- `white`
- `ticks`

Example:

```
sns.set_style("whitegrid")sns.histplot(data=df, x="total_bill")plt.show()
```

## 11.2 Set Theme

```
sns.set_theme(    style="whitegrid",    palette="deep",    font_scale=1.2)
```

## 11.3 Color Palettes

Colors improve the readability of visualizations.

```
sns.set_palette("pastel")
```

Some popular palettes:

| Palette    | Description                  |
| ---------- | ---------------------------- |
| deep       | Standard Seaborn colors      |
| muted      | Soft colors                  |
| pastel     | Light colors                 |
| bright     | Bright colors                |
| dark       | Dark colors                  |
| colorblind | Color-vision-friendly colors |
| viridis    | Sequential color palette     |
| coolwarm   | Diverging color palette      |

Example:

```
sns.barplot(    data=df,    x="day",    y="tip",    palette="viridis",    hue="day",    legend=False)plt.show()
```

## 11.4 Add Title and Labels

```
sns.scatterplot(    data=df,    x="total_bill",    y="tip")plt.title("Total Bill vs Tip")plt.xlabel("Total Bill")plt.ylabel("Tip Amount")plt.show()
```

## 11.5 Change Figure Size

```
plt.figure(figsize=(10, 6))sns.histplot(    data=df,    x="total_bill")plt.show()
```

## 11.6 Rotate X-Axis Labels

```
plt.xticks(rotation=45)
```

## 11.7 Add Grid

```
plt.grid(True)
```

## 11.8 Remove Spines

```
sns.despine()
```

Removes unnecessary borders from the plot.

## 11.9 Save a Graph

```
plt.figure(figsize=(10, 6))sns.histplot(data=df, x="total_bill")plt.savefig(    "seaborn_graph.png",    dpi=300,    bbox_inches="tight")plt.show()
```

Important:

- `dpi=300`: High-resolution image.
- `bbox_inches="tight"`: Reduces unnecessary margins.

# 12. Seaborn Figure-Level vs Axes-Level Functions

This is an important advanced concept.

Seaborn functions are divided into two types.

## 12.1 Axes-Level Functions

These functions draw plots on a Matplotlib Axes object.

Examples:

- `sns.scatterplot()`
- `sns.lineplot()`
- `sns.histplot()`
- `sns.boxplot()`
- `sns.violinplot()`
- `sns.heatmap()`
- `sns.regplot()`

Example:

```
fig, ax = plt.subplots(figsize=(8, 5))sns.scatterplot(    data=df,    x="total_bill",    y="tip",    ax=ax)ax.set_title("Bill vs Tip")plt.show()
```

## 12.2 Figure-Level Functions

These functions manage the complete figure and can create multiple subplots automatically.

Examples:

- `sns.relplot()`
- `sns.displot()`
- `sns.catplot()`
- `sns.lmplot()`
- `sns.jointplot()`
- `sns.pairplot()`
- `sns.clustermap()`

Example:

```
sns.displot(    data=df,    x="total_bill",    col="sex",    kind="hist")plt.show()
```

## Difference

| Axes-Level                               | Figure-Level                   |
| ---------------------------------------- | ------------------------------ |
| Works with individual Axes               | Manages complete Figure        |
| Can be combined with Matplotlib subplots | Can create multiple facets     |
| Accepts `ax=`                            | Generally doesn't accept `ax=` |
| More manual layout control               | Easier multi-plot layouts      |

# 13. Handling Missing Values Before Visualization

Real-world datasets often contain missing values.

Seaborn generally skips missing observations for the variables being plotted, but you should inspect and handle missing values appropriately.

## 13.1 Find Missing Values

```
print(df.isnull().sum())
```

## 13.2 Visualize Missing Values

```
sns.heatmap(    df.isnull(),    cbar=False,    cmap="viridis")plt.title("Missing Values")plt.show()
```

## 13.3 Remove Missing Values

```
clean_df = df.dropna()
```

## 13.4 Fill Missing Values

```
df["total_bill"] = df["total_bill"].fillna(    df["total_bill"].mean())
```

Important: Do not blindly remove or fill missing values. First understand why values are missing and choose an appropriate strategy.

# 14. Complete EDA Using Seaborn

Very Important for AI/ML

EDA stands for Exploratory Data Analysis.

Definition: Exploratory Data Analysis is the process of examining and visualizing a dataset to understand its structure, distributions, relationships, patterns, and unusual observations before applying machine learning algorithms.

## 14.1 EDA Workflow

1\. Load Dataset

Pandas / CSV / Database

2\. Understand Data

head, shape, info, describe

3\. Data Cleaning

Missing values, duplicates, outliers

4\. Univariate Analysis

Histogram, KDE, Count Plot, Box Plot

5\. Bivariate Analysis

Scatter, Line, Box, Regression

6\. Multivariate Analysis

Pair Plot, Heatmap, Pairwise Relationships

7\. Insights and Conclusions

Find patterns and prepare for ML

## 14.2 Types of EDA

A. Univariate Analysis

Analysis of a single variable.

Example:

```
sns.histplot(data=df, x="total_bill", kde=True)plt.show()
```

B. Bivariate Analysis

Analysis of two variables.

Example:

```
sns.scatterplot(    data=df,    x="total_bill",    y="tip")plt.show()
```

C. Multivariate Analysis

Analysis of more than two variables.

Example:

```
sns.pairplot(    df,    hue="sex")plt.show()
```

## 14.3 Complete EDA Code

This example uses the built-in `tips` dataset.

```
import pandas as pdimport numpy as npimport seaborn as snsimport matplotlib.pyplot as plt# Load datasetdf = sns.load_dataset("tips")# Understand datasetprint(df.head())print(df.shape)print(df.info())print(df.describe())# Check missing valuesprint(df.isnull().sum())# Check duplicatesprint(df.duplicated().sum())# 1. Distributionsns.histplot(    data=df,    x="total_bill",    kde=True)plt.title("Total Bill Distribution")plt.show()# 2. Category countsns.countplot(    data=df,    x="day",    hue="day",    legend=False)
```

# 15. Important Seaborn Functions Cheat Sheet

Keep this table for revision.

| Function            | Purpose                                  |
| ------------------- | ---------------------------------------- |
| `sns.scatterplot()` | Relationship between numerical variables |
| `sns.lineplot()`    | Trends                                   |
| `sns.histplot()`    | Frequency distribution                   |
| `sns.kdeplot()`     | Density distribution                     |
| `sns.ecdfplot()`    | Cumulative distribution                  |
| `sns.rugplot()`     | Individual observations                  |
| `sns.barplot()`     | Statistical category comparison          |
| `sns.countplot()`   | Category frequency                       |
| `sns.boxplot()`     | Quartiles and outliers                   |
| `sns.violinplot()`  | Density and distribution                 |
| `sns.stripplot()`   | Individual category observations         |
| `sns.swarmplot()`   | Non-overlapping category observations    |
| `sns.boxenplot()`   | Detailed quantile distribution           |
| `sns.pointplot()`   | Category estimates                       |
| `sns.regplot()`     | Regression visualization                 |
| `sns.lmplot()`      | Regression with facets                   |
| `sns.residplot()`   | Regression residuals                     |
| `sns.heatmap()`     | Matrix visualization                     |
| `sns.clustermap()`  | Hierarchical clustering                  |
| `sns.pairplot()`    | Pairwise relationships                   |
| `sns.jointplot()`   | Joint and marginal distributions         |
| `sns.relplot()`     | Relational figure-level plots            |
| `sns.displot()`     | Distribution figure-level plots          |
| `sns.catplot()`     | Categorical figure-level plots           |
| `sns.FacetGrid()`   | Multi-panel visualization                |

# 16. Seaborn with Pandas and NumPy

Seaborn is most useful when combined with NumPy and Pandas.

### Example: Create Your Own Dataset

```
import numpy as npimport pandas as pdimport seaborn as snsimport matplotlib.pyplot as pltnp.random.seed(42)data = {    "Student": ["A", "B", "C", "D", "E",                "F", "G", "H", "I", "J"],    "Study_Hours": np.random.randint(1, 10, 10),    "Marks": np.random.randint(40, 100, 10),    "Department": [        "AI", "CS", "AI", "ML", "CS",        "ML", "AI", "CS", "ML", "AI"    ]}df = pd.DataFrame(data)print(df)
```

### Visualization 1: Study Hours vs Marks

```
sns.scatterplot(    data=df,    x="Study_Hours",    y="Marks",    hue="Department")plt.title("Study Hours vs Marks")plt.show()
```

### Visualization 2: Department-wise Marks

```
sns.barplot(    data=df,    x="Department",    y="Marks")plt.title("Average Marks by Department")plt.show()
```

### Visualization 3: Marks Distribution

```
sns.histplot(    data=df,    x="Marks",    bins=5,    kde=True)plt.show()
```

### Visualization 4: Correlation

```
sns.heatmap(    df.select_dtypes(include="number").corr(),    annot=True,    cmap="coolwarm")plt.show()
```

# 17. Real-World Applications of Seaborn

| Industry   | Application                         |
| ---------- | ----------------------------------- |
| Finance    | Stock trends and financial analysis |
| Healthcare | Patient data analysis               |
| Education  | Student performance analysis        |
| E-commerce | Sales and customer behaviour        |
| Marketing  | Advertising and customer insights   |
| Banking    | Transaction pattern analysis        |
| AI/ML      | Feature analysis and EDA            |
| Business   | Revenue and profit analysis         |

## Seaborn in Machine Learning

Before building an ML model, Seaborn helps you:

1. Understand the dataset.
2. Identify feature distributions.
3. Find outliers.
4. Analyze relationships.
5. Visualize correlations.
6. Compare different classes.
7. Understand patterns in target variables.

Example: In a house-price prediction project:

- Histogram: House price distribution.
- Scatter plot: Area vs Price.
- Box plot: Price distribution by location.
- Heatmap: Correlation among numerical features.
- Pair plot: Relationships between multiple features.

Important: Seaborn is primarily an analysis and visualization library, not a machine learning algorithm library. Use Scikit-learn for model training.

# 18. Common Mistakes in Seaborn

| Mistake                              | Correct Approach                   |
| ------------------------------------ | ---------------------------------- |
| Forgetting `plt.show()`              | Call `plt.show()`                  |
| Using incorrect column names         | Check `df.columns`                 |
| Using strings in correlation         | Select numerical columns           |
| Plotting too many points             | Sample or aggregate large datasets |
| Ignoring missing values              | Inspect missingness first          |
| Confusing countplot and barplot      | Understand their purposes          |
| Using too many colors                | Keep colors consistent             |
| Not adding axis labels               | Add meaningful labels              |
| Ignoring outliers                    | Inspect using box plots            |
| Assuming correlation means causation | Investigate further                |



# 19. Mini Projects Using Seaborn

| Project                      | Dataset          | Main Visualizations      |
| ---------------------------- | ---------------- | ------------------------ |
| Student Performance Analysis | Student marks    | Histogram, Box, Scatter  |
| Titanic Survival Analysis    | Titanic          | Count, Bar, Heatmap      |
| Sales Data Analysis          | Sales CSV        | Line, Bar, Histogram     |
| Customer Behaviour Analysis  | Customer dataset | Scatter, Pairplot        |
| Iris Flower Analysis         | Iris             | Pairplot, Violin         |
| House Price Analysis         | Housing dataset  | Heatmap, Regression, Box |

## My recommendation: Complete these three projects first:

1. Student Performance Analysis.
2. Titanic Data Analysis.
3. Sales Data Visualization Dashboard.

They will help you practice Seaborn in real-world Data Science workflows.



# 20. Where Seaborn Fits in Your AI/ML Roadmap

Your Python for Data phase should follow this learning order:

1. API Handling

   Foundation

   Fetch and handle external data.
2. NumPy

   Foundation

   Numerical computing and arrays.
3. Pandas

   Foundation

   Data cleaning and manipulation.
4. Matplotlib

   Visualization

   Basic and customized graphs.
5. Seaborn

   Visualization

   Statistical visualization and EDA.
6. SQL

   Database

   Data querying and database management.
7. Data Analysis and EDA

   Practical application

   Apply all these tools to real-world datasets.

## Final Recommendation

For your B.Tech CS-AI-ML journey, don't just memorize Seaborn functions. Focus on understanding which graph to use, why to use it, and how to interpret its output.

Your target should be:

- Understand all major Seaborn plots.
- Write plotting code independently.
- Perform complete EDA.
- Interpret correlations, distributions and outliers.
- Complete at least 3 practical projects.

