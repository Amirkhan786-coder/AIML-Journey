# NUMPY — COMPLETE DETAILED NOTES



Zero to Advanced

B.Tech CS–AI/ML

Data Science & Machine Learning



Subject: Python for Data Science\
Library: NumPy (Numerical Python)\
Level: Beginner → Intermediate → Advanced\
Notes format: English definitions + Hinglish explanations + syntax + code + outputs + practical applications.

# UNIT 1 — INTRODUCTION TO NUMPY

## 1. What is NumPy?

Definition: NumPy (Numerical Python) is an open-source Python library used for numerical computing, scientific calculations, and multidimensional array operations.

Explanation (Hinglish):

NumPy Python ki ek powerful library hai jo large numerical data ko efficiently handle karne mein help karti hai.

Suppose tumhare paas 10,000 students ke marks hain. Tumhe:

- Average calculate karna hai.
- Maximum aur minimum marks find karne hain.
- Data ko filter karna hai.
- Mathematical calculations perform karni hain.

NumPy ye operations easily perform kar sakta hai.

### Main features of NumPy

1. Fast numerical computations.
2. Multidimensional array support.
3. Mathematical and statistical functions.
4. Matrix and linear algebra operations.
5. Broadcasting.
6. Memory-efficient numerical processing.
7. Integration with Pandas, Matplotlib, Scikit-learn and other scientific Python libraries.

## 2. Why do we use NumPy?

| Python List                                       | NumPy Array                                   |
| ------------------------------------------------- | --------------------------------------------- |
| General-purpose collection                        | Numerical computing                           |
| Can contain different data types                  | Usually homogeneous elements                  |
| No built-in vectorized arithmetic                 | Supports vectorized operations                |
| Multidimensional operations need more manual work | Native multidimensional arrays                |
| Less convenient for large numerical calculations  | Designed for efficient numerical calculations |

Example:

```
# Python listnumbers = [10, 20, 30, 40]# NumPy arrayimport numpy as nparr = np.array([10, 20, 30, 40])print(arr * 2)
```

Output:

```
[20 40 60 80]
```

In a normal Python list, `numbers * 2` repeats the list rather than multiplying each element.

## 3. Installation and Import

Install NumPy:

```
pip install numpy
```

Import NumPy:

```
import numpy as np
```

`np` is the standard alias used for NumPy.

Check version:

```
print(np.__version__)
```

Check installation:

```
arr = np.array([1, 2, 3])print(arr)
```

# UNIT 2 — NUMPY ARRAYS

## 4. What is an Array?

Definition: An array is a collection of elements stored in an organized structure across one or more dimensions.

NumPy ka main object `ndarray` hai.

`ndarray` stands for N-dimensional array.

### Types of arrays

1D Array — One Dimension

## 10

## 20

## 30

## 40

## 50

Example: [10, 20, 30, 40, 50]

2D Array — Rows and Columns

## 10

## 20

## 30

## 40

## 50

## 60

Example: [[10, 20, 30], [40, 50, 60]]

3D Array — Collection of 2D Arrays

Block 1

1

2

3

4

Block 2

5

6

7

8

Example shape: (2, 2, 2)

### A. Creating a 1D array

```
import numpy as nparr = np.array([10, 20, 30, 40])print(arr)print(type(arr))
```

Output:

```
[10 20 30 40]
<class 'numpy.ndarray'>
```

### B. Creating a 2D array

```
arr = np.array([    [10, 20, 30],    [40, 50, 60]])print(arr)
```

Output:

```
[[10 20 30]
 [40 50 60]]
```

### C. Creating a 3D array

```
arr = np.array([    [[1, 2], [3, 4]],    [[5, 6], [7, 8]]])print(arr)
```

Output:

```
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

### Applications of multidimensional arrays

- 1D: Student marks, prices, measurements.
- 2D: Tables, datasets and grayscale images.
- 3D: Color images, collections of matrices and batches of data.
- Higher dimensions: Video data, batches of images and deep-learning tensors.

# UNIT 3 — ARRAY CREATION METHODS

## 5. Important NumPy Array Creation Functions

### 5.1 `np.array()`

Creates an array from a Python list or another array-like object.

```
arr = np.array([1, 2, 3, 4])print(arr)
```

### 5.2 `np.zeros()`

Creates an array filled with zeros.

Syntax:

```
np.zeros(shape)
```

Example:

```
arr = np.zeros(5)print(arr)
```

Output:

```
[0. 0. 0. 0. 0.]
```

2D example:

```
arr = np.zeros((2, 3))print(arr)
```

### 5.3 `np.ones()`

Creates an array filled with ones.

```
arr = np.ones((2, 3))print(arr)
```

Output:

```
[[1. 1. 1.]
 [1. 1. 1.]]
```

### 5.4 `np.full()`

Creates an array filled with a specified value.

```
arr = np.full((2, 3), 7)print(arr)
```

Output:

```
[[7 7 7]
 [7 7 7]]
```

### 5.5 `np.arange()`

Creates evenly spaced values using a specified step size.

Syntax:

```
np.arange(start, stop, step)
```

Example:

```
arr = np.arange(1, 11, 2)print(arr)
```

Output:

```
[1 3 5 7 9]
```

Important: Stop value is excluded.

### 5.6 `np.linspace()`

Creates a specified number of evenly spaced values between two endpoints.

Syntax:

```
np.linspace(start, stop, num)
```

Example:

```
arr = np.linspace(0, 10, 5)print(arr)
```

Output:

```
[ 0.   2.5  5.   7.5 10. ]
```

Important: Endpoint is included by default.

Difference between `arange()` and `linspace()`:

| `arange()`                 | `linspace()`                             |
| -------------------------- | ---------------------------------------- |
| Uses step size             | Uses number of values                    |
| Stop excluded              | Endpoint included by default             |
| Good for integer sequences | Good for evenly spaced numerical samples |

### 5.7 `np.eye()`

Creates an identity matrix.

```
arr = np.eye(3)print(arr)
```

Output:

```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

### 5.8 `np.empty()`

Creates an array without initializing its elements.

```
arr = np.empty((2, 3))print(arr)
```

Values are unpredictable. They should not be assumed to be zeros.

### 5.9 `np.diag()`

Creates a diagonal matrix from a 1D array or extracts the diagonal of a 2D array.

```
arr = np.diag([1, 2, 3])print(arr)
```

Output:

```
[[1 0 0]
 [0 2 0]
 [0 0 3]]
```

# UNIT 4 — ARRAY ATTRIBUTES AND DATA TYPES

## 6. Array Attributes

Array attributes provide information about the structure and memory characteristics of an array.

```
arr = np.array([    [10, 20, 30],    [40, 50, 60]])print(arr.shape)print(arr.ndim)print(arr.size)print(arr.dtype)print(arr.itemsize)print(arr.nbytes)
```

| Attribute  | Definition                  | Example  |
| ---------- | --------------------------- | -------- |
| `shape`    | Size of each dimension      | `(2, 3)` |
| `ndim`     | Number of dimensions        | `2`      |
| `size`     | Total number of elements    | `6`      |
| `dtype`    | Data type of elements       | `int64`  |
| `itemsize` | Bytes per element           | `8`      |
| `nbytes`   | Total array element storage | `48`     |

Example:

```
arr = np.array([10, 20, 30])print("Shape:", arr.shape)print("Dimension:", arr.ndim)print("Size:", arr.size)
```

Output:

```
Shape: (3,)
Dimension: 1
Size: 3
```

## 7. NumPy Data Types

Definition: Data types specify what kind of values an array stores.

Important data types:

| Data type   | Description           |
| ----------- | --------------------- |
| `int8`      | 8-bit integer         |
| `int16`     | 16-bit integer        |
| `int32`     | 32-bit integer        |
| `int64`     | 64-bit integer        |
| `float32`   | 32-bit floating point |
| `float64`   | 64-bit floating point |
| `bool_`     | Boolean               |
| `complex64` | Complex number        |

### Specify dtype

```
arr = np.array([1, 2, 3], dtype=np.float32)print(arr)print(arr.dtype)
```

Output:

```
[1. 2. 3.]
float32
```

### Convert data types using `astype()`

```
arr = np.array([1.5, 2.5, 3.5])new_arr = arr.astype(int)print(new_arr)
```

Output:

```
[1 2 3]
```

Note: Converting floats to integers truncates decimal portions rather than rounding them.

# UNIT 5 — INDEXING AND SLICING

## 8. What is Indexing?

Definition: Indexing is the process of accessing individual elements of an array using their positions.

Python aur NumPy mein indexing zero se start hoti hai.

### 8.1 Positive Indexing

```
arr = np.array([10, 20, 30, 40, 50])print(arr[0])print(arr[2])print(arr[4])
```

Output:

```
10
30
50
```

### 8.2 Negative Indexing

Negative indexing accesses elements from the end of an array.

```
arr = np.array([10, 20, 30, 40, 50])print(arr[-1])print(arr[-2])print(arr[-3])
```

Output:

```
50
40
30
```

### 8.3 2D Array Indexing

Syntax:

```
arr[row_index, column_index]
```

Example:

```
arr = np.array([    [10, 20, 30],    [40, 50, 60]])print(arr[0, 0])print(arr[0, 2])print(arr[1, 1])
```

Output:

```
10
30
50
```

### 8.4 Negative Indexing in 2D

```
print(arr[-1, -1])
```

Output:

```
60
```

## 9. What is Slicing?

Definition: Slicing is the process of extracting a portion of an array using a range of indices.

Syntax:

```
arr[start:stop:step]
```

| Parameter | Meaning                            |
| --------- | ---------------------------------- |
| Start     | Starting index, included           |
| Stop      | Ending index, excluded             |
| Step      | Interval between selected elements |

### 9.1 Basic slicing

```
arr = np.array([10, 20, 30, 40, 50, 60])print(arr[1:4])
```

Output:

```
[20 30 40]
```

### 9.2 First elements

```
print(arr[:3])
```

Output:

```
[10 20 30]
```

### 9.3 Last elements

```
print(arr[3:])
```

Output:

```
[40 50 60]
```

### 9.4 Every second element

```
print(arr[::2])
```

Output:

```
[10 30 50]
```

### 9.5 Reverse an array

```
print(arr[::-1])
```

Output:

```
[60 50 40 30 20 10]
```

### 9.6 2D Array Slicing

```
arr = np.array([    [1, 2, 3],    [4, 5, 6],    [7, 8, 9]])print(arr[0:2, 1:3])
```

Output:

```
[[2 3]
 [5 6]]
```

Explanation:

- `0:2` selects the first two rows.
- `1:3` selects the second and third columns.

### Important Indexing Rules

| Syntax        | Meaning                    |
| ------------- | -------------------------- |
| `arr[0]`      | First element or first row |
| `arr[-1]`     | Last element or last row   |
| `arr[1:4]`    | Index 1 through 3          |
| `arr[:3]`     | First three elements       |
| `arr[::2]`    | Every second element       |
| `arr[::-1]`   | Reverse                    |
| `arr[0, 1]`   | First row, second column   |
| `arr[:, 0]`   | First column               |
| `arr[1, :]`   | Second row                 |
| `arr[:, 1:3]` | Second and third columns   |

Important: Basic slicing generally returns a view, so modifying the sliced array can modify the original array. Advanced indexing generally returns a copy.

# UNIT 6 — RESHAPING AND ARRAY MANIPULATION

## 10. What is Reshaping?

Definition: Reshaping is the process of changing the dimensions of an array without changing its total number of elements.

Example:

```
arr = np.arange(1, 7)new_arr = arr.reshape(2, 3)print(new_arr)
```

Output:

```
[[1 2 3]
 [4 5 6]]
```

### Reshaping rules

1. Total elements must remain equal.
2. New dimensions must be compatible.
3. Reshape does not change the element values.
4. It returns a view when possible, otherwise a copy.

### 10.1 Reshape into 3 × 2

```
arr = np.arange(1, 7)print(arr.reshape(3, 2))
```

Output:

```
[[1 2]
 [3 4]
 [5 6]]
```

### 10.2 Using `-1`

NumPy automatically calculates one unknown dimension.

```
arr = np.arange(12)print(arr.reshape(3, -1))
```

Output:

```
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

Only one dimension can be inferred using `-1`.

### 10.3 `flatten()`

Converts a multidimensional array into a 1D copy.

```
arr = np.array([[1, 2], [3, 4]])print(arr.flatten())
```

Output:

```
[1 2 3 4]
```

### 10.4 `ravel()`

Returns a flattened array, usually a view when possible.

```
print(arr.ravel())
```

### 10.5 `transpose()`

Changes rows into columns and columns into rows.

```
arr = np.array([    [1, 2, 3],    [4, 5, 6]])print(arr.T)
```

Output:

```
[[1 4]
 [2 5]
 [3 6]]
```

### 10.6 `resize()`

Changes the shape and size of an array in place.

```
arr = np.array([1, 2, 3, 4])arr.resize(2, 2)print(arr)
```

Output:

```
[[1 2]
 [3 4]]
```

Unlike `reshape()`, `ndarray.resize()` modifies the original array.

### Difference between reshape, flatten and ravel

| Function    | Purpose                         | Copy or View       |
| ----------- | ------------------------------- | ------------------ |
| `reshape()` | Changes shape                   | View when possible |
| `flatten()` | Converts to 1D                  | Always copy        |
| `ravel()`   | Converts to 1D                  | View when possible |
| `resize()`  | Changes original size and shape | In-place operation |

# UNIT 7 — MATHEMATICAL OPERATIONS

## 11. Arithmetic Operations

NumPy supports element-wise arithmetic operations.

```
a = np.array([10, 20, 30])b = np.array([1, 2, 3])print(a + b)print(a - b)print(a * b)print(a / b)print(a // b)print(a % b)print(a ** 2)
```

Output:

```
[11 22 33]
[ 9 18 27]
[10 40 90]
[10. 10. 10.]
[10 10 10]
[0 0 0]
[100 400 900]
```

### Arithmetic operators

| Operator | Meaning                     |
| -------- | --------------------------- |
| `+`      | Addition                    |
| `-`      | Subtraction                 |
| `*`      | Element-wise multiplication |
| `/`      | Division                    |
| `//`     | Floor division              |
| `%`      | Modulus                     |
| `**`     | Power                       |

### 11.1 Scalar Operations

```
arr = np.array([10, 20, 30])print(arr + 5)print(arr - 5)print(arr * 2)print(arr / 2)
```

### 11.2 Mathematical Functions

```
arr = np.array([1, 4, 9, 16])print(np.sqrt(arr))print(np.square(arr))print(np.exp(arr))print(np.log(arr))print(np.abs([-5, -2, 3]))
```

### 11.3 Trigonometric Functions

```
arr = np.array([0, 30, 45, 60, 90])radians = np.deg2rad(arr)print(np.sin(radians))print(np.cos(radians))print(np.tan(radians))
```

NumPy trigonometric functions use radians, not degrees.

### 11.4 Rounding Functions

```
arr = np.array([1.25, 2.65, 3.85])print(np.round(arr, 1))print(np.floor(arr))print(np.ceil(arr))
```

- `round()` → Rounds to the specified decimal precision.
- `floor()` → Rounds down.
- `ceil()` → Rounds up.

# UNIT 8 — STATISTICAL FUNCTIONS

## 12. Statistical Operations

Statistics is essential for Data Science and Machine Learning.

Suppose:

```
marks = np.array([60, 70, 80, 90, 100])
```

### 12.1 Mean

Definition: Mean is the arithmetic average of numerical values.

Formula:

\\[ Mean = \frac{\sum x_i}{n} \\]

```
print(np.mean(marks))
```

Output: `80.0`

### 12.2 Median

Definition: Median is the middle value after arranging the data in sorted order.

```
print(np.median(marks))
```

Output: `80.0`

### 12.3 Mode

NumPy does not provide a general `np.mode()` function. For simple numerical frequency counts, use:

```
arr = np.array([1, 2, 2, 3, 3, 3])values, counts = np.unique(arr, return_counts=True)mode = values[np.argmax(counts)]print(mode)
```

Output:

```
3
```

For more advanced statistical analysis, SciPy also provides mode-related functionality.

### 12.4 Standard Deviation

Definition: Standard deviation measures how spread out values are around the mean.

```
print(np.std(marks))
```

### 12.5 Variance

Definition: Variance measures the average squared deviation from the mean.

```
print(np.var(marks))
```

### 12.6 Minimum and Maximum

```
print(np.min(marks))print(np.max(marks))
```

### 12.7 Sum

```
print(np.sum(marks))
```

### 12.8 Percentile

Definition: A percentile indicates the value below which a given percentage of observations falls.

```
print(np.percentile(marks, 50))print(np.percentile(marks, 75))
```

### 12.9 Argmax and Argmin

Return the indices of maximum and minimum elements.

```
arr = np.array([10, 50, 20, 80, 30])print(np.argmax(arr))print(np.argmin(arr))
```

Output:

```
3
0
```

### Statistical Functions Summary

| Function          | Purpose            |
| ----------------- | ------------------ |
| `np.mean()`       | Average            |
| `np.median()`     | Middle value       |
| `np.std()`        | Standard deviation |
| `np.var()`        | Variance           |
| `np.min()`        | Minimum            |
| `np.max()`        | Maximum            |
| `np.sum()`        | Sum                |
| `np.percentile()` | Percentile         |
| `np.argmax()`     | Maximum index      |
| `np.argmin()`     | Minimum index      |
| `np.cumsum()`     | Cumulative sum     |
| `np.cumprod()`    | Cumulative product |

## 13. Axis in NumPy

Axis specifies the dimension along which an operation is performed.

Example:

```
arr = np.array([    [10, 20, 30],    [40, 50, 60]])
```

Understanding axis

axis=0

# ↓

Column-wise reduction

## 50, 70, 90

axis=1

# →

Row-wise reduction

## 60, 150

```
print(np.sum(arr, axis=0))print(np.sum(arr, axis=1))
```

Output:

```
[50 70 90]
[ 60 150]
```

# UNIT 9 — BOOLEAN INDEXING AND FILTERING

## 14. What is Boolean Indexing?

Definition: Boolean indexing is a technique used to select array elements based on specified conditions.

Hinglish: Ismein hum condition lagate hain aur NumPy automatically sirf matching values return karta hai.

### 14.1 Comparison Operators

```
arr = np.array([10, 20, 30, 40, 50])print(arr > 25)print(arr < 30)print(arr == 20)print(arr != 30)print(arr >= 40)print(arr <= 20)
```

Output:

```
[False False  True  True  True]
[ True  True False False False]
[False  True False False False]
[ True  True False  True  True]
[False False False  True  True]
[ True  True False False False]
```

### 14.2 Filtering Elements

```
arr = np.array([10, 20, 30, 40, 50])result = arr[arr > 25]print(result)
```

Output:

```
[30 40 50]
```

### 14.3 Multiple Conditions

NumPy provides logical operators for combining conditions.

| Operator           | Meaning     |
| ------------------ | ----------- |
| `&`                | AND         |
| `\\|`              | OR          |
| `~`                | NOT         |
| `np.logical_and()` | Logical AND |
| `np.logical_or()`  | Logical OR  |
| `np.logical_not()` | Logical NOT |

Example:

```
arr = np.array([10, 20, 30, 40, 50, 60])result = arr[(arr >= 20) & (arr <= 50)]print(result)
```

Output:

```
[20 30 40 50]
```

Important: Har condition ko parentheses mein likho.

### 14.4 `np.where()`

Selects values based on a condition.

Syntax:

```
np.where(condition, value_if_true, value_if_false)
```

Example:

```
marks = np.array([45, 80, 35, 90, 60])result = np.where(marks >= 50, "Pass", "Fail")print(result)
```

Output:

```
['Fail' 'Pass' 'Fail' 'Pass' 'Pass']
```

### 14.5 `np.select()`

Multiple conditions ke liye useful hai.

```
marks = np.array([95, 75, 55, 30])conditions = [    marks >= 90,    marks >= 70,    marks >= 50]choices = ["A", "B", "C"]result = np.select(conditions, choices, default="Fail")print(result)
```

Output:

```
['A' 'B' 'C' 'Fail']
```

### 14.6 `np.any()` and `np.all()`

`np.any()` checks whether at least one condition is true.

`np.all()` checks whether every condition is true.

```
arr = np.array([10, 20, 30, 40])print(np.any(arr > 35))print(np.all(arr > 5))
```

Output:

```
True
True
```

Real-world applications:

- Filtering student records.
- Selecting customers.
- Removing invalid measurements.
- Selecting high-value transactions.
- Filtering machine-learning datasets.

# UNIT 10 — BROADCASTING

## 15. What is Broadcasting?

Definition: Broadcasting is a NumPy mechanism that allows operations between arrays of compatible shapes without manually creating repeated copies of smaller arrays.

Hinglish Explanation:

Suppose ek array mein students ke marks hain aur tumhe har student ke marks mein 5 bonus marks add karne hain.

NumPy automatically har element par 5 apply kar deta hai.

```
marks = np.array([60, 70, 80])print(marks + 5)
```

Output:

```
[65 75 85]
```

### 15.1 Broadcasting Between 2D and 1D Arrays

```
a = np.array([    [10, 20, 30],    [40, 50, 60]])b = np.array([1, 2, 3])print(a + b)
```

Output:

```
[[11 22 33]
 [41 52 63]]
```

NumPy logically applies `b` to each row without needing you to manually duplicate it.

### 15.2 Broadcasting Rules

Compare dimensions from right to left.

Two dimensions are compatible if:

1. They are equal.
2. One of them is 1.
3. If one array has fewer dimensions, missing dimensions are treated as 1 on the left.

| Array A  | Array B  | Result       |
| -------- | -------- | ------------ |
| `(2, 3)` | `(2, 3)` | Compatible   |
| `(2, 3)` | `(3,)`   | Compatible   |
| `(2, 3)` | `(2, 1)` | Compatible   |
| `(3, 1)` | `(1, 4)` | Compatible   |
| `(2, 3)` | `(4,)`   | Incompatible |

### 15.3 Broadcasting with Columns

```
a = np.array([    [10],    [20],    [30]])b = np.array([1, 2, 3])print(a + b)
```

Output:

```
[[11 12 13]
 [21 22 23]
 [31 32 33]]
```

Shape calculation:

- A: `(3, 1)`
- B: `(3,)`, treated as `(1, 3)`
- Output: `(3, 3)`

### 15.4 Practical Application: Feature Normalization

```
data = np.array([    [10, 100],    [20, 200],    [30, 300]])mean = np.mean(data, axis=0)std = np.std(data, axis=0)normalized = (data - mean) / stdprint(normalized)
```

Broadcasting makes it possible to subtract the column means and divide by column standard deviations.

AI/ML importance: Broadcasting is widely used in feature transformations, normalization, neural-network calculations and numerical computing.

# UNIT 11 — COPY AND VIEW

## 16. What is Copy?

Definition: A copy is a new independent array with its own data.

```
arr = np.array([10, 20, 30])new_arr = arr.copy()new_arr[0] = 100print(arr)print(new_arr)
```

Output:

```
[10 20 30]
[100  20  30]
```

Original array unchanged.

### What is View?

Definition: A view is a new array object that shares its underlying data with another array.

```
arr = np.array([10, 20, 30])new_arr = arr.view()new_arr[0] = 100print(arr)print(new_arr)
```

Output:

```
[100  20  30]
[100  20  30]
```

Original array bhi change ho gaya.

### Difference Between Copy and View

| Copy                          | View                                       |
| ----------------------------- | ------------------------------------------ |
| Independent data              | Shared underlying data                     |
| More memory may be required   | Can avoid data duplication                 |
| Changes don't affect original | Shared element changes may affect original |
| `arr.copy()`                  | `arr.view()`                               |

### Check Shared Memory

```
arr = np.array([1, 2, 3])view = arr.view()copy = arr.copy()print(np.shares_memory(arr, view))print(np.shares_memory(arr, copy))
```

Output:

```
True
False
```

Important: View aur copy ka behaviour samajhna large datasets aur memory optimization ke liye important hai.

# UNIT 12 — JOINING AND SPLITTING ARRAYS

## 17. Joining Arrays

Joining means combining two or more arrays into one array.

### 17.1 `np.concatenate()`

Combines arrays along an existing axis.

```
a = np.array([1, 2, 3])b = np.array([4, 5, 6])result = np.concatenate((a, b))print(result)
```

Output:

```
[1 2 3 4 5 6]
```

### 17.2 `np.vstack()`

Stacks arrays vertically.

```
a = np.array([1, 2])b = np.array([3, 4])print(np.vstack((a, b)))
```

Output:

```
[[1 2]
 [3 4]]
```

### 17.3 `np.hstack()`

Stacks arrays horizontally.

```
a = np.array([1, 2])b = np.array([3, 4])print(np.hstack((a, b)))
```

Output:

```
[1 2 3 4]
```

### 17.4 `np.stack()`

Combines arrays along a new axis.

```
a = np.array([1, 2])b = np.array([3, 4])print(np.stack((a, b), axis=0))
```

Output:

```
[[1 2]
 [3 4]]
```

Difference:

- `concatenate()` → Existing axis.
- `stack()` → New axis.
- `vstack()` → Vertical stacking.
- `hstack()` → Horizontal stacking.

## 18. Splitting Arrays

Splitting means dividing an array into smaller arrays.

### 18.1 `np.split()`

```
arr = np.array([1, 2, 3, 4, 5, 6])result = np.split(arr, 3)print(result)
```

Output:

```
[array([1, 2]),
 array([3, 4]),
 array([5, 6])]
```

Equal divisions are required when an integer number of sections is specified.

### 18.2 `np.array_split()`

Allows unequal divisions.

```
arr = np.array([1, 2, 3, 4, 5])result = np.array_split(arr, 2)print(result)
```

Output:

```
[array([1, 2, 3]), array([4, 5])]
```

### 18.3 `np.vsplit()` and `np.hsplit()`

```
arr = np.arange(16).reshape(4, 4)print(np.vsplit(arr, 2))print(np.hsplit(arr, 2))
```

- `vsplit()` → Splits vertically into row sections.
- `hsplit()` → Splits horizontally into column sections.

# UNIT 13 — SORTING AND SEARCHING

## 19. Sorting Arrays

Sorting means arranging array elements in a particular order.

### 19.1 `np.sort()`

```
arr = np.array([40, 10, 50, 20, 30])print(np.sort(arr))
```

Output:

```
[10 20 30 40 50]
```

### 19.2 Descending Order

```
print(np.sort(arr)[::-1])
```

Output:

```
[50 40 30 20 10]
```

### 19.3 `np.argsort()`

Returns the indices that would sort the array.

```
arr = np.array([40, 10, 50, 20])print(np.argsort(arr))
```

Output:

```
[1 3 0 2]
```

Explanation:

- Index 1 contains 10.
- Index 3 contains 20.
- Index 0 contains 40.
- Index 2 contains 50.

### 19.4 Sorting 2D Arrays

```
arr = np.array([    [3, 1, 2],    [6, 4, 5]])print(np.sort(arr, axis=0))print(np.sort(arr, axis=1))
```

- `axis=0` → Sorts values within each column.
- `axis=1` → Sorts values within each row.

## 20. Unique Values

`np.unique()` returns sorted unique elements.

```
arr = np.array([1, 2, 2, 3, 3, 3, 4])print(np.unique(arr))
```

Output:

```
[1 2 3 4]
```

### Count Frequency

```
arr = np.array([1, 2, 2, 3, 3, 3])values, counts = np.unique(arr, return_counts=True)print(values)print(counts)
```

Output:

```
[1 2 3]
[1 2 3]
```

### 20.1 Search with `np.where()`

```
arr = np.array([10, 20, 30, 40, 50])print(np.where(arr == 30))
```

Returns the index where the condition is true.

### 20.2 `np.isin()`

Checks whether elements belong to a specified collection.

```
arr = np.array([1, 2, 3, 4, 5])print(np.isin(arr, [2, 4]))
```

Output:

```
[False  True False  True False]
```

# UNIT 14 — RANDOM MODULE

## 21. Random Number Generation

NumPy provides random number generation for simulations, experiments and machine-learning workflows.

### 21.1 Random Decimal Numbers

```
arr = np.random.rand(5)print(arr)
```

Generates five random values in the interval `[0, 1)`.

### 21.2 Random Integers

```
arr = np.random.randint(1, 10, size=5)print(arr)
```

Generates five integers from 1 to 9.

### 21.3 Random 2D Array

```
arr = np.random.randint(1, 100, size=(3, 3))print(arr)
```

### 21.4 Standard Normal Distribution

```
arr = np.random.randn(5)print(arr)
```

Generates random values from the standard normal distribution.

### 21.5 Random Sampling

```
arr = np.array([10, 20, 30, 40, 50])result = np.random.choice(arr, size=3, replace=False)print(result)
```

### 21.6 Shuffle an Array

```
arr = np.array([1, 2, 3, 4, 5])np.random.shuffle(arr)print(arr)
```

`shuffle()` modifies the array in place.

### 21.7 Random Seed

Seed helps make random results reproducible.

```
np.random.seed(42)print(np.random.randint(1, 100, 5))
```

### Recommended Modern Method: `default_rng()`

```
rng = np.random.default_rng(42)arr = rng.integers(1, 100, size=5)print(arr)
```

Important random functions:

| Function        | Purpose                       |
| --------------- | ----------------------------- |
| `rand()`        | Random values between 0 and 1 |
| `randint()`     | Random integers               |
| `randn()`       | Standard normal values        |
| `normal()`      | Normal distribution           |
| `uniform()`     | Uniform distribution          |
| `choice()`      | Random selection              |
| `shuffle()`     | Shuffle in place              |
| `permutation()` | Random permutation            |
| `default_rng()` | Modern random generator       |

# UNIT 15 — LINEAR ALGEBRA

## 22. What is Linear Algebra?

Definition: Linear algebra is a branch of mathematics dealing with vectors, matrices, linear equations and transformations.

It is an important mathematical foundation of machine learning and deep learning.

## 23. Matrix Creation

```
A = np.array([    [1, 2],    [3, 4]])B = np.array([    [5, 6],    [7, 8]])
```

## 24. Matrix Operations

### 24.1 Matrix Addition

```
print(A + B)
```

Output:

```
[[ 6  8]
 [10 12]]
```

### 24.2 Element-wise Multiplication

```
print(A * B)
```

Output:

```
[[ 5 12]
 [21 32]]
```

### 24.3 Matrix Multiplication

```
print(A @ B)
```

Output:

```
[[19 22]
 [43 50]]
```

Alternatively:

```
np.matmul(A, B)
```

### 24.4 Dot Product

```
a = np.array([1, 2, 3])b = np.array([4, 5, 6])print(np.dot(a, b))
```

Output:

```
32
```

### 24.5 Transpose

```
print(A.T)
```

### 24.6 Determinant

The determinant is a scalar value calculated from a square matrix.

```
print(np.linalg.det(A))
```

Output approximately:

```
-2.0
```

### 24.7 Inverse Matrix

```
print(np.linalg.inv(A))
```

An inverse exists only if the matrix is square and nonsingular.

### 24.8 Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors describe important properties of a linear transformation.

```
A = np.array([    [2, 0],    [0, 3]])values, vectors = np.linalg.eig(A)print(values)print(vectors)
```

### 24.9 Solve Linear Equations

Suppose:

\\[ 2x+y=5 \\]

\\[ x+3y=6 \\]

```
A = np.array([    [2, 1],    [1, 3]])b = np.array([5, 6])solution = np.linalg.solve(A, b)print(solution)
```

Output:

```
[1.8 1.4]
```

### 24.10 Matrix Norm

```
A = np.array([    [1, 2],    [3, 4]])print(np.linalg.norm(A))
```

A norm measures the magnitude of a vector or matrix according to a selected mathematical definition.

### Important Linear Algebra Functions

| Function                  | Use                            |
| ------------------------- | ------------------------------ |
| `np.dot()`                | Dot product                    |
| `np.matmul()`             | Matrix multiplication          |
| `@`                       | Matrix multiplication operator |
| `np.linalg.det()`         | Determinant                    |
| `np.linalg.inv()`         | Matrix inverse                 |
| `np.linalg.solve()`       | Solve linear equations         |
| `np.linalg.eig()`         | Eigenvalues and eigenvectors   |
| `np.linalg.norm()`        | Vector/matrix norm             |
| `np.linalg.svd()`         | Singular Value Decomposition   |
| `np.linalg.matrix_rank()` | Matrix rank                    |

AI/ML applications:

- Linear regression.
- Neural networks.
- Principal Component Analysis.
- Feature transformations.
- Optimization algorithms.
- Computer vision.

# UNIT 16 — MISSING VALUES AND DATA CLEANING

## 25. What is NaN?

NaN means Not a Number.

It is commonly used to represent missing or undefined numerical values.

Example:

```
arr = np.array([10.0, 20.0, np.nan, 40.0])print(arr)
```

### 25.1 Detect Missing Values

```
print(np.isnan(arr))
```

Output:

```
[False False  True False]
```

### 25.2 Count Missing Values

```
print(np.isnan(arr).sum())
```

Output:

```
1
```

### 25.3 Ignore NaN While Calculating Mean

```
print(np.nanmean(arr))
```

Output:

```
23.333333333333332
```

Other useful functions:

- `np.nanmedian()`
- `np.nansum()`
- `np.nanstd()`
- `np.nanvar()`
- `np.nanmin()`
- `np.nanmax()`

### 25.4 Replace NaN with Zero

```
arr = np.array([10.0, 20.0, np.nan, 40.0])arr[np.isnan(arr)] = 0print(arr)
```

Output:

```
[10. 20.  0. 40.]
```

### 25.5 Remove NaN Values

```
arr = np.array([10.0, 20.0, np.nan, 40.0])cleaned = arr[~np.isnan(arr)]print(cleaned)
```

Output:

```
[10. 20. 40.]
```

### 25.6 Infinity Handling

NumPy also supports positive and negative infinity.

```
arr = np.array([10, np.inf, -np.inf, np.nan])print(np.isinf(arr))print(np.isfinite(arr))
```

- `np.isinf()` detects infinite values.
- `np.isfinite()` detects values that are neither infinite nor NaN.

Important: NumPy can detect and manipulate numerical missing values, but more advanced dataset cleaning is generally done with Pandas.

# UNIT 17 — IMPORTANT ADVANCED FUNCTIONS

## 26. Useful NumPy Functions

| Function           | Description                            |
| ------------------ | -------------------------------------- |
| `np.clip()`        | Restricts values to a range            |
| `np.diff()`        | Calculates differences                 |
| `np.cumsum()`      | Cumulative sum                         |
| `np.cumprod()`     | Cumulative product                     |
| `np.maximum()`     | Element-wise maximum                   |
| `np.minimum()`     | Element-wise minimum                   |
| `np.argmax()`      | Index of maximum                       |
| `np.argmin()`      | Index of minimum                       |
| `np.unique()`      | Unique elements                        |
| `np.intersect1d()` | Common elements                        |
| `np.union1d()`     | Union of elements                      |
| `np.setdiff1d()`   | Elements in first array but not second |
| `np.where()`       | Conditional selection                  |
| `np.isin()`        | Membership checking                    |
| `np.nan_to_num()`  | Replace NaN and infinities             |
| `np.percentile()`  | Percentile calculation                 |

### 26.1 Clipping

```
arr = np.array([10, 20, 30, 40, 50])print(np.clip(arr, 20, 40))
```

Output:

```
[20 20 30 40 40]
```

### 26.2 Difference

```
arr = np.array([10, 15, 25, 40])print(np.diff(arr))
```

Output:

```
[ 5 10 15]
```

### 26.3 Cumulative Sum

```
arr = np.array([1, 2, 3, 4])print(np.cumsum(arr))
```

Output:

```
[ 1  3  6 10]
```

### 26.4 Common Elements

```
a = np.array([1, 2, 3, 4])b = np.array([3, 4, 5, 6])print(np.intersect1d(a, b))
```

Output:

```
[3 4]
```

### 26.5 Replace Invalid Numbers

```
arr = np.array([1.0, np.nan, np.inf])print(np.nan_to_num(arr))
```

By default, NaN and infinities are replaced with finite numerical values.

# UNIT 18 — UNIVERSAL FUNCTIONS (UFUNCS)

## 27. What are Universal Functions?

Definition: Universal functions are NumPy functions that operate element-wise on arrays and support broadcasting.

They are commonly called ufuncs.

Examples:

```
arr = np.array([1, 2, 3, 4])print(np.sqrt(arr))print(np.exp(arr))print(np.add(arr, 5))print(np.multiply(arr, 2))
```

### Types of ufuncs

| Category      | Examples                                |
| ------------- | --------------------------------------- |
| Arithmetic    | `add`, `subtract`, `multiply`, `divide` |
| Trigonometric | `sin`, `cos`, `tan`                     |
| Exponential   | `exp`, `exp2`                           |
| Logarithmic   | `log`, `log10`                          |
| Comparison    | `greater`, `less`, `equal`              |
| Logical       | `logical_and`, `logical_or`             |

### Example: Ufunc vs Normal Operation

```
a = np.array([1, 2, 3])b = np.array([4, 5, 6])print(np.add(a, b))print(a + b)
```

Both produce:

```
[5 7 9]
```

# UNIT 19 — NUMPY INPUT/OUTPUT

## 28. Saving and Loading Arrays

NumPy allows you to save numerical arrays to files and load them later.

### 28.1 Save a Single Array

```
arr = np.array([10, 20, 30, 40])np.save("data.npy", arr)
```

### 28.2 Load an Array

```
data = np.load("data.npy")print(data)
```

### 28.3 Save Multiple Arrays

```
a = np.array([1, 2, 3])b = np.array([4, 5, 6])np.savez("arrays.npz", first=a, second=b)
```

Load:

```
data = np.load("arrays.npz")print(data["first"])print(data["second"])
```

### 28.4 Save as CSV or Text

```
arr = np.array([[1, 2], [3, 4]])np.savetxt("data.csv", arr, delimiter=",")
```

Load:

```
data = np.loadtxt("data.csv", delimiter=",")print(data)
```

For CSV files containing headers or missing values, `np.genfromtxt()` is another useful function.

# UNIT 20 — PERFORMANCE AND MEMORY OPTIMIZATION

## 29. Vectorization

Definition: Vectorization is the process of performing operations on entire arrays rather than explicitly iterating through each element using Python loops.

Without vectorization:

```
numbers = [1, 2, 3, 4]result = []for n in numbers:    result.append(n * 2)print(result)
```

With NumPy:

```
arr = np.array([1, 2, 3, 4])print(arr * 2)
```

Output:

```
[2 4 6 8]
```

Vectorized NumPy operations are often faster for large numerical workloads because much of the computation runs in optimized compiled code.

## 30. Memory Optimization

### Use appropriate data types

```
arr = np.array([1, 2, 3, 4], dtype=np.int32)print(arr.dtype)print(arr.nbytes)
```

Choosing `float32` instead of `float64` can reduce storage requirements for suitable applications.

### Avoid unnecessary copies

```
arr = np.arange(100000)view = arr[:50000]
```

Basic slicing can provide a view without duplicating the underlying data.

### Use vectorized operations

Avoid unnecessarily writing Python loops for numerical operations that NumPy can perform directly.

### Important concepts

- `dtype`
- `itemsize`
- `nbytes`
- Vectorization
- Broadcasting
- Views and copies
- Memory layout
- Contiguous arrays

# UNIT 21 — NUMPY APPLICATIONS IN AI/ML

## 31. How NumPy is used in Machine Learning

NumPy is one of the foundational libraries in the Python data-science ecosystem.

| AI/ML Task          | NumPy Application            |
| ------------------- | ---------------------------- |
| Data preparation    | Array creation and reshaping |
| Data cleaning       | Filtering and NaN handling   |
| Feature engineering | Mathematical transformations |
| Normalization       | Mean and standard deviation  |
| Linear regression   | Matrix operations            |
| Deep learning       | Numerical tensor operations  |
| Computer vision     | Image arrays                 |
| Statistics          | Mean, median and variance    |
| Model experiments   | Random number generation     |

### Example 1: Image Representation

A grayscale image can be represented as a 2D array of pixel intensities.

```
image = np.array([    [0, 100, 200],    [50, 150, 255],    [30, 80, 180]])print(image.shape)print(image)
```

For a typical 8-bit grayscale image, values range from 0 to 255.

- 0 = Black
- 255 = White
- Values between them = Different shades of grey

A color image commonly has shape:

```
(height, width, 3)
```

The three channels represent Red, Green and Blue.

### Example 2: Feature Scaling

```
data = np.array([10, 20, 30, 40, 50])mean = np.mean(data)std = np.std(data)scaled = (data - mean) / stdprint(scaled)
```

This is standardization, which transforms data to have approximately zero mean and unit standard deviation.

### Example 3: Simple Linear Regression Calculation

```
X = np.array([    [1],    [2],    [3],    [4]])weights = np.array([2])bias = 5predictions = X @ weights + biasprint(predictions)
```

Output:

```
[ 7  9 11 13]
```

Here, the mathematical model is:

\\[ y = Xw+b \\]

This is a simplified demonstration of a linear model.

# UNIT 22 — COMPLETE NUMPY MINI PROJECT

## 32. Project: Student Performance Analyzer

Practical project

[School Data Analytics Services | EduVision Analytics](https://images.openai.com/static-rsc-4/a_La2Lc5ksogzU_YqUgYgL_aXDBhWSC42AzkvfQ4WspZjYz-W0Y2E5wZTr_zbj3fWFDjSqx6R4x6QotZiduq5InBp8yLKhHGny8-EwfZuAwDi5fGjMN2lA5WE93WOgwz3iZQCH1L_EmuMuc4hWPvEEgRa6QzDMgsKN2pQyw6aog?purpose=inline)

[eduvisionanalytics.com](https://eduvisionanalytics.com/?utm_source=chatgpt.com)

Objective: Create a numerical student performance analysis program using NumPy.

### Project requirements

1. Store student marks.
2. Calculate total marks.
3. Calculate average marks.
4. Find highest and lowest marks.
5. Identify passed students.
6. Find students scoring above 80.
7. Rank students.
8. Calculate subject-wise average.

### Complete Python code

```
import numpy as np# Student namesnames = np.array([    "Aman",    "Rahul",    "Priya",    "Neha",    "Sara"])# Marks: Mathematics, Physics, Computer Sciencemarks = np.array([    [78, 85, 90],    [65, 70, 75],    [92, 88, 95],    [55, 60, 58],    [80, 82, 84]])# Total marks per studenttotal = np.sum(marks, axis=1)# Average marks per studentaverage = np.mean(marks, axis=1)# Subject-wise averagesubject_average = np.mean(marks, axis=0)# Highest and lowest individual markshighest = np.max(marks)lowest = np.min(marks)# Students with average >= 80top_students = names[average >= 80]
```

### Concepts used in this project

- `np.array()`
- `np.sum()`
- `np.mean()`
- `np.max()`
- `np.min()`
- `np.all()`
- Boolean indexing
- `np.argsort()`
- Array indexing

### Project upgrades

After completing the basic project, add:

- CSV input using Pandas.
- Graphs using Matplotlib.
- Interactive dashboard using Streamlit.
- Subject-wise performance comparison.
- Student performance prediction using Scikit-learn.

This will connect your NumPy knowledge with your next Data Science phase.



# UNIT 23 — COMPLETE NUMPY FUNCTION CHEAT SHEET

## 33. Important Functions at a Glance

| Category        | Functions                                          |
| --------------- | -------------------------------------------------- |
| Array creation  | `array()`, `zeros()`, `ones()`, `full()`           |
| Range creation  | `arange()`, `linspace()`                           |
| Matrix creation | `eye()`, `identity()`, `diag()`                    |
| Properties      | `shape`, `ndim`, `size`, `dtype`                   |
| Indexing        | `arr[i]`, `arr[i,j]`                               |
| Slicing         | `arr[start:stop:step]`                             |
| Reshaping       | `reshape()`, `resize()`                            |
| Flattening      | `flatten()`, `ravel()`                             |
| Transpose       | `transpose()`, `.T`                                |
| Arithmetic      | `add()`, `subtract()`, `multiply()`, `divide()`    |
| Mathematics     | `sqrt()`, `square()`, `exp()`, `log()`             |
| Statistics      | `mean()`, `median()`, `std()`, `var()`             |
| Filtering       | `where()`, `select()`, `isin()`                    |
| Logic           | `any()`, `all()`, `logical_and()`                  |
| Broadcasting    | Automatic broadcasting                             |
| Joining         | `concatenate()`, `stack()`, `vstack()`, `hstack()` |
| Splitting       | `split()`, `array_split()`, `vsplit()`             |
| Sorting         | `sort()`, `argsort()`                              |
| Unique          | `unique()`                                         |
| Random          | `randint()`, `choice()`, `shuffle()`               |
| Linear algebra  | `dot()`, `matmul()`, `linalg.solve()`              |
| Missing values  | `isnan()`, `nanmean()`, `nan_to_num()`             |
| File handling   | `save()`, `load()`, `savetxt()`, `loadtxt()`       |



# UNIT 24 — REVISION AND LEARNING ROADMAP

## 34. NumPy Revision Plan

| Day   | Topics                                  | Practice     |
| ----- | --------------------------------------- | ------------ |
| Day 1 | Introduction, arrays, creation          | 15 questions |
| Day 2 | Properties, data types                  | 10 questions |
| Day 3 | Indexing and slicing                    | 15 questions |
| Day 4 | Reshaping, mathematical operations      | 15 questions |
| Day 5 | Statistics, Boolean indexing            | 15 questions |
| Day 6 | Broadcasting, copy/view, linear algebra | 15 questions |
| Day 7 | Random, missing values, project         | Mini project |

## 35. NumPy Mastery Checklist

Your NumPy Progress

0/25 completed

Tick each topic after understanding it and writing its code yourself.

Understand NumPy and ndarray

Install and import NumPy

Create 1D, 2D and 3D arrays

Understand array attributes

Understand data types and type conversion

Master indexing and negative indexing

Master 1D and 2D slicing

Understand reshape and resize

Understand flatten and ravel

Perform mathematical operations

Use statistical functions

Understand axis=0 and axis=1

Master Boolean indexing

Use np.where and np.select

Understand broadcasting rules

Understand copy and view

Join and split arrays

Sort arrays and find unique values

Use random number generation

Perform matrix operations

Use NumPy linear algebra

Handle NaN and infinity

Understand ufuncs and vectorization

Save and load NumPy arrays

Build Student Marks Analyzer

Reset checklist

# 36. What to Learn After NumPy?

For your B.Tech CS-AI/ML roadmap, follow this learning sequence:

1. Python Fundamentals and Advanced Python

   Foundation

   OOP, functions, modules, exception handling, API handling
2. NumPy

   Current topic

   Numerical computing, arrays, broadcasting, linear algebra
3. Pandas

   DataFrames, data cleaning, missing values, grouping, merging
4. Matplotlib and Seaborn

   Data visualization, charts, statistical plots
5. Data Analysis and EDA

   Outliers, feature relationships, data transformation
6. SQL

   Queries, joins, subqueries, window functions
7. Machine Learning

   Scikit-learn, regression, classification, clustering, model evaluation

                              THANK YOU