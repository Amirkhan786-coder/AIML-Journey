# 1. NUMPY PRACTICE QUESTIONS

## 1. Beginner Level — 1 to 15

1. Create a NumPy array containing numbers from 1 to 20.
2. Create an array containing even numbers from 2 to 50.
3. Create a 3 × 3 zero matrix.
4. Create a 4 × 4 identity matrix.
5. Create an array containing five equally spaced values between 0 and 100.
6. Find the shape of a 2D array.
7. Find the total number of elements in an array.
8. Find the data type of an array.
9. Extract the first three elements.
10. Extract the last three elements.
11. Reverse an array.
12. Extract the second row of a matrix.
13. Extract the third column of a matrix.
14. Convert a 1D array into a 3 × 3 array.
15. Convert a 2D array into a 1D array.

## 2. Intermediate Level — 16 to 30

16. Calculate the mean of an array.
17. Calculate the median.
18. Calculate standard deviation and variance.
19. Find maximum and minimum values.
20. Find the index of the maximum element.
21. Filter all values greater than 50.
22. Extract all even numbers.
23. Replace negative values with zero.
24. Find unique elements.
25. Count the frequency of each unique value.
26. Combine two arrays horizontally.
27. Combine two arrays vertically.
28. Split an array into three parts.
29. Sort an array in descending order.
30. Generate a 5 × 5 array of random integers.

## 3. Advanced Level — 31 to 45

31. Explain broadcasting with an example.
32. Demonstrate copy and view.
33. Find the transpose of a matrix.
34. Calculate the determinant of a matrix.
35. Calculate the inverse of a matrix.
36. Solve two simultaneous linear equations.
37. Find eigenvalues and eigenvectors.
38. Perform matrix multiplication.
39. Replace NaN values with the mean.
40. Normalize a numerical dataset.
41. Calculate column-wise averages.
42. Calculate row-wise sums.
43. Find common elements between two arrays.
44. Calculate cumulative sums.
45. Use `np.where()` to classify student marks.

#  2. IMPORTANT NUMPY INTERVIEW QUESTIONS

## 1. Beginner Interview Questions

Q1. What is NumPy?

NumPy is a Python library used for numerical computing and multidimensional array operations.

Q2. What is ndarray?

`ndarray` is the main N-dimensional array object in NumPy.

Q3. What is the difference between a list and an array?

Lists are general-purpose collections, whereas NumPy arrays are designed for efficient numerical operations.

Q4. What is the difference between `shape` and `size`?

- `shape` gives the dimensions of an array.
- `size` gives the total number of elements.

Q5. What is dtype?

`dtype` specifies the data type of array elements.

Q6. What is vectorization?

Performing operations on entire arrays instead of explicitly iterating through individual elements using Python loops.

## 2. Intermediate Interview Questions

Q7. What is broadcasting?

Broadcasting allows arithmetic operations between arrays of compatible shapes.

Q8. Difference between `arange()` and `linspace()`?

`arange()` uses a step size, while `linspace()` uses the required number of equally spaced values.

Q9. Difference between `flatten()` and `ravel()`?

`flatten()` returns a copy; `ravel()` returns a view when possible.

Q10. Difference between copy and view?

A copy has independent data; a view shares underlying data.

Q11. What is Boolean indexing?

Selecting array elements based on Boolean conditions.

Q12. What is axis in NumPy?

Axis identifies the dimension along which an operation is performed.

Q13. What is `np.where()`?

It selects values or returns indices based on a condition, depending on how it is called.

Q14. What is `np.unique()`?

It returns the sorted unique elements of an array by default.

## 3. Advanced Interview Questions

Q15. Difference between `*` and `@`?

- `*` performs element-wise multiplication.
- `@` performs matrix multiplication.

Q16. What is `np.linalg`?

It is NumPy's linear algebra module.

Q17. What is NaN?

NaN means Not a Number and is used to represent undefined or missing numerical values.

Q18. What is the difference between `np.mean()` and `np.nanmean()`?

`np.mean()` generally propagates NaN values, whereas `np.nanmean()` ignores NaN values.

Q19. What is a ufunc?

A universal function performs element-wise operations on arrays and supports broadcasting.

Q20. How can you optimize NumPy performance?

Use vectorized operations, suitable data types, broadcasting and avoid unnecessary copies.