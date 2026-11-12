
# PHASE 04 — MATHEMATICS & STATISTICS
# PART 01 — STATISTICS

## 1. INTRODUCTION TO STATISTICS

### 1.1 What is Statistics?

**Definition:** Statistics is the branch of mathematics that deals with collecting, organizing, analyzing, interpreting, and presenting data.

**Easy Hinglish Explanation:**

Statistics ka use data ko understand karne ke liye hota hai. Iski help se hum data ka average, patterns, variation aur relationships find kar sakte hain.

**Example:**

```python
marks = [60, 70, 80, 90, 100]
```

Statistics se hum calculate kar sakte hain:
- Average marks
- Highest and lowest marks
- Data distribution
- Students' performance

### 1.2 Importance of Statistics in AI/ML

| Application | Purpose |
|---|---|
| Data Analysis | Data ko understand karna |
| Data Cleaning | Missing values aur outliers identify karna |
| Feature Engineering | Useful features identify karna |
| Machine Learning | Patterns find karna |
| Model Evaluation | Model errors measure karna |
| Prediction | Data-based decisions lena |

### 1.3 Types of Statistics

**A. Descriptive Statistics**

Definition: Descriptive Statistics summarizes and describes the main characteristics of a dataset.

Hinglish: Available data ka summary provide karta hai.

Examples:
- Mean
- Median
- Mode
- Variance
- Standard Deviation

**B. Inferential Statistics**

Definition: Inferential Statistics uses sample data to make conclusions about a larger population.

Hinglish: Sample data ki help se poori population ke baare mein estimate ya conclusion nikalna.

Example: College ke 5,000 students mein se 100 students ka survey karke poore college ke baare mein estimate karna.

---

## 2. POPULATION AND SAMPLE

### 2.1 Population

**Definition:** Population is the complete set of individuals or observations being studied.

Example: College ke sabhi 5,000 students.

### 2.2 Sample

**Definition:** A sample is a smaller subset selected from a population.

Example: College ke randomly selected 100 students.

### 2.3 Parameter and Statistic

**Parameter:** A numerical value describing a population.

**Statistic:** A numerical value calculated from a sample.

Population Mean:

$$
\mu = \frac{\sum_{i=1}^{N}x_i}{N}
$$

Sample Mean:

$$
\bar{x} = \frac{\sum_{i=1}^{n}x_i}{n}
$$

Where:
- $\mu$ = Population mean
- $\bar{x}$ = Sample mean
- $N$ = Population size
- $n$ = Sample size

### 2.4 Difference Between Population and Sample

| Population | Sample |
|---|---|
| Complete group | Part of the group |
| Usually larger | Usually smaller |
| Parameter describes it | Statistic describes it |
| Example: 5000 students | Example: 100 students |

---

## 3. TYPES OF DATA

### 3.1 Qualitative Data

**Definition:** Qualitative data represents non-numerical characteristics or categories.

Examples:
- City
- Color
- Department
- Education level

### 3.2 Quantitative Data

**Definition:** Quantitative data represents numerical measurements or counts.

Examples:
- Age
- Salary
- Marks
- Height

Two types:

**A. Discrete Data**

Definition: Discrete data consists of countable values.

Examples:
- Number of students
- Number of cars
- Number of products

**B. Continuous Data**

Definition: Continuous data can take any value within a given range.

Examples:
- Height
- Weight
- Temperature
- Time

### 3.3 Measurement Scales

| Scale | Meaning | Example |
|---|---|---|
| Nominal | Categories without order | City |
| Ordinal | Categories with order | Education level |
| Interval | Equal intervals, no true zero | Celsius temperature |
| Ratio | Equal intervals with true zero | Height, weight |

---

## 4. MEASURES OF CENTRAL TENDENCY

Central Tendency ka matlab hai dataset ki central ya representative value find karna.

Three main types:
1. Mean
2. Median
3. Mode

### 4.1 Mean (Average)

**Definition:** Mean is the sum of all observations divided by the total number of observations.

**Formula:**

$$
\boxed{\bar{x}=\frac{\sum_{i=1}^{n}x_i}{n}}
$$

Where:
- $\bar{x}$ = Mean
- $\sum x_i$ = Sum of all values
- $n$ = Total number of values

**Numerical Example:**

Dataset:

$$
X=[10,20,30,40,50]
$$

Step 1: Add all values.

$$
10+20+30+40+50=150
$$

Step 2: Count observations.

$$
n=5
$$

Step 3: Apply formula.

$$
\bar{x}=\frac{150}{5}
$$

$$
\boxed{\bar{x}=30}
$$

**Python Implementation:**

```python
data = [10, 20, 30, 40, 50]

total = sum(data)
count = len(data)

mean = total / count

print("Mean:", mean)
```

Output:

```text
Mean: 30.0
```

**Line-by-Line Explanation:**

- `data`: Stores observations.
- `sum(data)`: Adds all values.
- `len(data)`: Counts observations.
- `total / count`: Calculates average.
- `print()`: Displays the result.

**Using NumPy:**

```python
import numpy as np

data = [10, 20, 30, 40, 50]

print("Mean:", np.mean(data))
```

**AI/ML Application:** Numerical features ka average calculate karna aur suitable datasets mein missing numerical values fill karna.

### 4.2 Median

**Definition:** Median is the middle value of a dataset after arranging observations in ascending or descending order.

Hinglish: Sorted data ki beech wali value Median hoti hai.

**Case 1: Odd Number of Observations**

Formula:

$$
Median=x_{\left(\frac{n+1}{2}\right)}
$$

Example:

$$
X=[10,20,30,40,50]
$$

$$
Position=\frac{5+1}{2}=3
$$

$$
\boxed{Median=30}
$$

**Case 2: Even Number of Observations**

Formula:

$$
Median=\frac{x_{(n/2)}+x_{(n/2+1)}}{2}
$$

Example:

$$
X=[10,20,30,40]
$$

$$
Median=\frac{20+30}{2}
$$

$$
\boxed{Median=25}
$$

**Python:**

```python
import numpy as np

data = [10, 20, 30, 40, 50]

print("Median:", np.median(data))
```

**AI/ML Application:** Outliers hone par data ka central value understand karne ke liye Median useful hai.

### 4.3 Mode

**Definition:** Mode is the value that occurs most frequently in a dataset.

Example:

$$
X=[10,20,20,30,40]
$$

20 occurs most frequently.

$$
\boxed{Mode=20}
$$

**Python:**

```python
from statistics import mode

data = [10, 20, 20, 30, 40]

print("Mode:", mode(data))
```

**AI/ML Application:** Categorical columns mein missing values ko most frequent category se fill karna.

### 4.4 Mean vs Median vs Mode

| Mean | Median | Mode |
|---|---|---|
| Average | Middle value | Most frequent |
| Affected by outliers | Less affected by outliers | Frequency based |
| Numerical | Ordered data | Numerical or categorical |

---

## 5. MEASURES OF DISPERSION

Dispersion tells us how spread out the observations are in a dataset.

Main measures:
1. Range
2. Variance
3. Standard Deviation
4. Interquartile Range

### 5.1 Range

**Definition:** Range is the difference between maximum and minimum values.

Formula:

$$
\boxed{Range=X_{\max}-X_{\min}}
$$

Example:

$$
X=[10,20,30,40,50]
$$

$$
Range=50-10
$$

$$
\boxed{Range=40}
$$

**Python:**

```python
data = [10, 20, 30, 40, 50]

result = max(data) - min(data)

print("Range:", result)
```

### 5.2 Variance

**Definition:** Variance measures the average squared deviation of observations from their mean.

Hinglish: Variance batata hai ki values mean se kitni spread hain.

**Population Variance:**

$$
\boxed{\sigma^2=\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}}
$$

**Sample Variance:**

$$
\boxed{s^2=\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}
$$

Where:
- $\sigma^2$ = Population variance
- $s^2$ = Sample variance
- $\mu$ = Population mean
- $\bar{x}$ = Sample mean

**Numerical Example:**

$$
X=[2,4,6]
$$

Step 1: Mean.

$$
\mu=\frac{2+4+6}{3}=4
$$

Step 2: Squared deviations.

$$
(2-4)^2=4
$$

$$
(4-4)^2=0
$$

$$
(6-4)^2=4
$$

Step 3: Add them.

$$
4+0+4=8
$$

Step 4: Divide by population size.

$$
\sigma^2=\frac{8}{3}
$$

$$
\boxed{\sigma^2\approx2.67}
$$

**Python:**

```python
import numpy as np

data = [2, 4, 6]

population_variance = np.var(data)
sample_variance = np.var(data, ddof=1)

print("Population Variance:", population_variance)
print("Sample Variance:", sample_variance)
```

Important:
- `np.var(data)` calculates population variance by default.
- `ddof=1` calculates sample variance.

### 5.3 Standard Deviation

**Definition:** Standard Deviation measures the amount of variation or dispersion in a dataset.

**Population SD:**

$$
\boxed{\sigma=\sqrt{\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}}}
$$

**Sample SD:**

$$
\boxed{s=\sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}}
$$

Standard Deviation is the square root of Variance.

Example:

$$
Variance=2.67
$$

$$
SD=\sqrt{2.67}
$$

$$
\boxed{SD\approx1.63}
$$

**Python:**

```python
import numpy as np

data = [2, 4, 6]

print("Population SD:", np.std(data))
print("Sample SD:", np.std(data, ddof=1))
```

Interpretation:
- Low SD: Values mean ke close hain.
- High SD: Values zyada spread hain.
- SD = 0: All values identical hain.

### 5.4 Range vs Variance vs Standard Deviation

| Measure | Meaning |
|---|---|
| Range | Maximum - Minimum |
| Variance | Average squared deviation |
| Standard Deviation | Spread in original units |

---

## 6. PERCENTILES AND QUARTILES

### 6.1 Percentile

**Definition:** A percentile indicates the value below which a specified percentage of observations falls.

Example: 90th percentile means approximately 90% of observations are at or below that value.

**Python:**

```python
import numpy as np

data = [10, 20, 30, 40, 50, 60, 70]

print("90th Percentile:", np.percentile(data, 90))
```

### 6.2 Quartiles

**Definition:** Quartiles divide ordered data into four parts.

- Q1 = 25th percentile
- Q2 = 50th percentile
- Q3 = 75th percentile

$$
Q_1=P_{25}
$$

$$
Q_2=P_{50}
$$

$$
Q_3=P_{75}
$$

### 6.3 Interquartile Range (IQR)

**Definition:** IQR measures the spread of the middle 50% of observations.

Formula:

$$
\boxed{IQR=Q_3-Q_1}
$$

Example:

$$
Q_1=20,\quad Q_3=60
$$

$$
IQR=60-20
$$

$$
\boxed{IQR=40}
$$

### 6.4 Outlier Detection Using IQR

An outlier is an observation that is unusually far from the other observations.

Lower Bound:

$$
LB=Q_1-1.5(IQR)
$$

Upper Bound:

$$
UB=Q_3+1.5(IQR)
$$

Values outside these bounds are potential outliers.

**Example:**

$$
Q_1=20,\quad Q_3=60
$$

$$
IQR=60-20=40
$$

$$
LB=20-1.5(40)=-40
$$

$$
UB=60+1.5(40)=120
$$

Values below -40 or above 120 are potential outliers.

**Python:**

```python
import numpy as np

data = [10, 20, 30, 40, 50, 60, 200]

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = [
    x for x in data
    if x < lower or x > upper
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Outliers:", outliers)
```

**AI/ML Application:** Outlier detection, data cleaning and exploratory data analysis.

Important: Har outlier ko remove nahi karna chahiye. Pehle verify karo ki wo genuine observation hai ya data error.

---

## 7. COVARIANCE AND CORRELATION

### 7.1 Covariance

**Definition:** Covariance measures how two variables change together.

**Population Covariance:**

$$
\boxed{Cov(X,Y)=\frac{\sum_{i=1}^{N}(x_i-\mu_x)(y_i-\mu_y)}{N}}
$$

**Sample Covariance:**

$$
\boxed{Cov(X,Y)=\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{n-1}}
$$

Interpretation:
- Positive covariance: Variables generally same direction mein change karte hain.
- Negative covariance: Variables generally opposite directions mein change karte hain.
- Zero covariance: No linear co-movement indicated.

**Python:**

```python
import numpy as np

study_hours = [1, 2, 3, 4, 5]
marks = [20, 30, 40, 50, 60]

covariance_matrix = np.cov(
    study_hours,
    marks,
    ddof=1
)

print(covariance_matrix)
print("Covariance:", covariance_matrix[0, 1])
```

### 7.2 Correlation

**Definition:** Correlation measures the strength and direction of a relationship between two variables.

**Pearson Correlation Formula:**

$$
\boxed{r=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}}
$$

Range:

$$
\boxed{-1\leq r\leq+1}
$$

Interpretation:

| Correlation | Meaning |
|---|---|
| +1 | Perfect positive linear correlation |
| +0.8 | Strong positive |
| 0 | No linear correlation |
| -0.8 | Strong negative |
| -1 | Perfect negative linear correlation |

**Python:**

```python
import numpy as np

study_hours = [1, 2, 3, 4, 5]
marks = [20, 30, 40, 50, 60]

correlation = np.corrcoef(
    study_hours,
    marks
)[0, 1]

print("Correlation:", correlation)
```

### 7.3 Covariance vs Correlation

| Covariance | Correlation |
|---|---|
| Measures joint variation | Measures strength and direction |
| Depends on units | Unit-free |
| No fixed range | -1 to +1 |
| Difficult to compare | Easier to compare |

**Important:** Correlation does not imply causation.

Do variables related ho sakte hain, lekin iska matlab ye nahi ki ek doosre ka cause hai.

---

## 8. SKEWNESS

**Definition:** Skewness measures the asymmetry of a data distribution.

### 8.1 Types of Skewness

**A. Positive Skewness**
- Right-side tail longer.
- Often mean > median.

**B. Negative Skewness**
- Left-side tail longer.
- Often mean < median.

**C. Zero Skewness**
- Distribution approximately symmetrical.
- Mean and median often close.

**Python:**

```python
from scipy.stats import skew

data = [10, 20, 20, 30, 40, 50, 100]

print("Skewness:", skew(data))
```

**AI/ML Application:** Feature transformations and distribution analysis.

---

## 9. KURTOSIS

**Definition:** Kurtosis describes the tail heaviness of a distribution relative to a normal distribution.

### 9.1 Types of Kurtosis

1. Mesokurtic: Similar tail heaviness to normal distribution.
2. Leptokurtic: Heavier tails.
3. Platykurtic: Lighter tails.

### 9.2 Excess Kurtosis

$$
\boxed{Excess\ Kurtosis=Kurtosis-3}
$$

Normal distribution has zero excess kurtosis.

**Python:**

```python
from scipy.stats import kurtosis

data = [10, 20, 20, 30, 40, 50, 100]

print("Excess Kurtosis:", kurtosis(data))
```

**AI/ML Application:** Financial analysis, anomaly detection and extreme-value analysis.

---

## 10. STATISTICAL DISTRIBUTIONS

**Definition:** A statistical distribution describes how possible values of a variable are distributed and how frequently or likely different values occur.

### 10.1 Normal Distribution

**Definition:** Normal distribution is a continuous, symmetric, bell-shaped probability distribution.

Probability Density Function:

$$
\boxed{
f(x)=\frac{1}{\sigma\sqrt{2\pi}}
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
}
$$

Where:
- $\mu$ = Mean
- $\sigma$ = Standard deviation
- $\sigma^2$ = Variance
- $x$ = Observation

### 10.2 Empirical Rule

For a normal distribution:

- Approximately 68% observations lie within 1 SD.
- Approximately 95% observations lie within 2 SD.
- Approximately 99.7% observations lie within 3 SD.

$$
P(\mu-\sigma\leq X\leq\mu+\sigma)\approx68\%
$$

$$
P(\mu-2\sigma\leq X\leq\mu+2\sigma)\approx95\%
$$

$$
P(\mu-3\sigma\leq X\leq\mu+3\sigma)\approx99.7\%
$$

### 10.3 Standard Normal Distribution

A normal distribution with mean 0 and standard deviation 1 is called a Standard Normal Distribution.

$$
\boxed{\mu=0,\quad\sigma=1}
$$

### 10.4 Z-Score

**Definition:** Z-score tells us how many standard deviations an observation is away from the mean.

Formula:

$$
\boxed{Z=\frac{X-\mu}{\sigma}}
$$

Example:

$$
X=70,\quad\mu=50,\quad\sigma=10
$$

$$
Z=\frac{70-50}{10}
$$

$$
\boxed{Z=2}
$$

Interpretation: Observation mean se 2 standard deviations above hai.

**Python:**

```python
from scipy.stats import zscore

data = [10, 20, 30, 40, 50]

print("Z-Scores:", zscore(data))
```

### 10.5 Other Important Distributions

| Distribution | Type | Application |
|---|---|---|
| Bernoulli | Discrete | Binary outcomes |
| Binomial | Discrete | Number of successes |
| Poisson | Discrete | Event counts |
| Uniform | Discrete or continuous | Equal likelihood over a specified range |
| Normal | Continuous | Measurement data |
| Exponential | Continuous | Waiting-time models |

---

## 11. REGRESSION ERROR METRICS

Regression models numerical values predict karte hain.

Examples:
- House prices
- Salary
- Temperature
- Sales

Where:
- $y_i$ = Actual value
- $\hat{y}_i$ = Predicted value
- $n$ = Number of observations

### 11.1 Mean Absolute Error (MAE)

**Definition:** MAE measures the average absolute difference between actual and predicted values.

Formula:

$$
\boxed{MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|}
$$

Example:

Actual:

$$
Y=[10,20,30]
$$

Predicted:

$$
\hat{Y}=[12,18,35]
$$

Calculation:

$$
MAE=\frac{|10-12|+|20-18|+|30-35|}{3}
$$

$$
MAE=\frac{2+2+5}{3}
$$

$$
\boxed{MAE=3}
$$

### 11.2 Mean Squared Error (MSE)

**Definition:** MSE measures the average squared difference between actual and predicted values.

Formula:

$$
\boxed{MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
$$

Example:

$$
MSE=\frac{(10-12)^2+(20-18)^2+(30-35)^2}{3}
$$

$$
MSE=\frac{4+4+25}{3}
$$

$$
\boxed{MSE=11}
$$

### 11.3 Root Mean Squared Error (RMSE)

**Definition:** RMSE is the square root of Mean Squared Error.

Formula:

$$
\boxed{RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}}
$$

Example:

$$
RMSE=\sqrt{11}
$$

$$
\boxed{RMSE\approx3.32}
$$

### 11.4 R-Squared Score (R²)

**Definition:** R² measures how much of the variation in the target variable is explained by a regression model relative to a mean baseline.

Formula:

$$
\boxed{R^2=1-\frac{SS_{res}}{SS_{tot}}}
$$

Where:

$$
SS_{res}=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

$$
SS_{tot}=\sum_{i=1}^{n}(y_i-\bar{y})^2
$$

Interpretation:
- R² = 1: Perfect predictions.
- R² = 0: Same performance as predicting the target mean.
- R² < 0: Worse than the mean baseline.

### 11.5 Python Implementation of Error Metrics

```python
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import numpy as np

actual = [10, 20, 30]
predicted = [12, 18, 35]

mae = mean_absolute_error(actual, predicted)

mse = mean_squared_error(actual, predicted)

rmse = np.sqrt(mse)

r2 = r2_score(actual, predicted)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)
```

### 11.6 Error Metrics Comparison

| Metric | Purpose |
|---|---|
| MAE | Average absolute error |
| MSE | Average squared error |
| RMSE | Square root of MSE |
| R² | Explained variation relative to mean baseline |

---

## 12. COMPLETE PYTHON STATISTICS PRACTICE

Install required libraries if needed:

```bash
python -m pip install numpy pandas scipy matplotlib seaborn scikit-learn
```

Complete code:

```python
import numpy as np
import pandas as pd

from scipy import stats

# Dataset
data = [10, 20, 20, 30, 40, 50, 60]

# Central Tendency
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data, keepdims=False).mode)

# Dispersion
print("Range:", np.max(data) - np.min(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))

# Quartiles
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)

print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)

# IQR
IQR = Q3 - Q1

print("IQR:", IQR)

# Skewness
print("Skewness:", stats.skew(data))

# Kurtosis
print("Kurtosis:", stats.kurtosis(data))

# Correlation
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

print("Correlation:", np.corrcoef(x, y)[0, 1])
```

---

