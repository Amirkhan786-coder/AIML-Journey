# 1. INTERVIEW QUESTIONS AND ANSWERS

## Q1. What is Linear Algebra?

Linear Algebra is the study of vectors, matrices, linear equations, and linear transformations.

## Q2. What is a scalar?

A scalar is a single numerical value.

## Q3. What is a vector?

A vector is an ordered collection of numbers with magnitude and direction.

## Q4. What is a matrix?

A matrix is a rectangular arrangement of numbers in rows and columns.

## Q5. What is a tensor?

A tensor is a generalized representation of numerical data across different dimensions.

## Q6. What is an identity matrix?

A square matrix with ones on the main diagonal and zeros elsewhere.

## Q7. What is a transpose?

Transpose converts rows into columns and columns into rows.

## Q8. What is the difference between dot product and cross product?

Dot product returns a scalar, while the cross product of two 3D vectors returns a vector perpendicular to both.

## Q9. What is a determinant?

A scalar calculated from a square matrix that helps determine whether the matrix is invertible.

## Q10. When does a matrix have an inverse?

A square matrix has an inverse if its determinant is non-zero.

## Q11. What is matrix rank?

The maximum number of linearly independent rows or columns.

## Q12. What are eigenvalues?

Eigenvalues are scalar values describing how eigenvectors are scaled by a matrix transformation.

## Q13. What are eigenvectors?

Non-zero vectors whose direction remains unchanged under a matrix transformation, apart from possible reversal.

## Q14. What is PCA?

PCA is a dimensionality reduction technique that transforms data into orthogonal principal components ordered by explained variance.

## Q15. What is SVD?

SVD is a matrix factorization technique that decomposes a matrix into U, Σ, and Vᵀ.

## Q16. Why is matrix multiplication important in Deep Learning?

Neural networks use matrix multiplication to calculate weighted sums and transform batches of input features.

## Q17. What is linear independence?

A set of vectors is linearly independent if none can be represented as a linear combination of the others.

## Q18. What is the difference between element-wise and matrix multiplication?

Element-wise multiplication multiplies corresponding entries. Matrix multiplication uses row-by-column dot products.

## Q19. What is an orthogonal matrix?

A square matrix Q satisfying QᵀQ = I.

## Q20. What is the least squares method?

A method that estimates parameters by minimizing the sum of squared residuals.

---

# 2. PRACTICE QUESTIONS WITH SOLUTIONS

## BEGINNER LEVEL

### Q1. Find the order of the matrix.

$$
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}
$$

Solution:

Rows = 2, Columns = 3.

Answer:

$$
\boxed{2\times3}
$$

### Q2. Add the following vectors.

$$
A=
\begin{bmatrix}
2\\
4
\end{bmatrix}
,\quad
B=
\begin{bmatrix}
3\\
5
\end{bmatrix}
$$

Solution:

$$
A+B=
\begin{bmatrix}
2+3\\
4+5
\end{bmatrix}
$$

$$
\boxed{
\begin{bmatrix}
5\\
9
\end{bmatrix}
}
$$

### Q3. Find the magnitude.

$$
A=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

Solution:

$$
\|A\|=\sqrt{3^2+4^2}
$$

$$
\boxed{5}
$$

### Q4. Find the dot product.

$$
A=
\begin{bmatrix}
1\\
2
\end{bmatrix}
,\quad
B=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

Solution:

$$
A\cdot B=1(3)+2(4)
$$

$$
\boxed{11}
$$

### Q5. Find the transpose.

$$
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}
$$

Answer:

$$
\boxed{
A^T=
\begin{bmatrix}
1 & 4\\
2 & 5\\
3 & 6
\end{bmatrix}
}
$$

## INTERMEDIATE LEVEL

### Q6. Add the matrices.

$$
A=
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix}
$$

$$
B=
\begin{bmatrix}
5 & 6\\
7 & 8
\end{bmatrix}
$$

Answer:

$$
\boxed{
\begin{bmatrix}
6 & 8\\
10 & 12
\end{bmatrix}
}
$$

### Q7. Multiply the matrices.

$$
A=
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix}
$$

$$
B=
\begin{bmatrix}
5 & 6\\
7 & 8
\end{bmatrix}
$$

Answer:

$$
\boxed{
AB=
\begin{bmatrix}
19 & 22\\
43 & 50
\end{bmatrix}
}
$$

### Q8. Find the determinant.

$$
A=
\begin{bmatrix}
3 & 2\\
1 & 4
\end{bmatrix}
$$

Solution:

$$
\det(A)=3(4)-2(1)
$$

$$
\boxed{10}
$$

### Q9. Find the trace.

$$
A=
\begin{bmatrix}
2 & 5\\
3 & 7
\end{bmatrix}
$$

Solution:

$$
\operatorname{tr}(A)=2+7
$$

$$
\boxed{9}
$$

### Q10. Find the rank.

$$
A=
\begin{bmatrix}
1 & 2\\
2 & 4
\end{bmatrix}
$$

Solution:

Second row is twice the first row.

$$
\boxed{\operatorname{rank}(A)=1}
$$

## ADVANCED LEVEL

### Q11. Find the inverse.

$$
A=
\begin{bmatrix}
2 & 1\\
1 & 1
\end{bmatrix}
$$

Answer:

$$
\boxed{
A^{-1}=
\begin{bmatrix}
1 & -1\\
-1 & 2
\end{bmatrix}
}
$$

### Q12. Find eigenvalues.

$$
A=
\begin{bmatrix}
2 & 0\\
0 & 3
\end{bmatrix}
$$

Solution:

$$
\det(A-\lambda I)=0
$$

$$
(2-\lambda)(3-\lambda)=0
$$

Answer:

$$
\boxed{\lambda_1=2,\quad\lambda_2=3}
$$

### Q13. Solve the linear equations.

$$
2x+y=5
$$

$$
x+y=3
$$

Answer:

$$
\boxed{x=2,\quad y=1}
$$

### Q14. Are the following vectors linearly dependent?

$$
A=
\begin{bmatrix}
1\\
2
\end{bmatrix}
,\quad
B=
\begin{bmatrix}
3\\
6
\end{bmatrix}
$$

Solution:

$$
B=3A
$$

Answer:

They are linearly dependent.

### Q15. Find the standard score of x = 90 when mean = 70 and standard deviation = 10.

$$
Z=\frac{90-70}{10}
$$

$$
\boxed{Z=2}
$$

---

# 3. MULTIPLE CHOICE QUESTIONS (MCQs)

### Q1. A matrix is an arrangement of numbers in:

A. Only rows  
B. Only columns  
C. Rows and columns  
D. Circles  

**Answer: C**

### Q2. The order of a matrix with 3 rows and 4 columns is:

A. 4 × 3  
B. 3 × 4  
C. 3 × 3  
D. 4 × 4  

**Answer: B**

### Q3. The determinant of an identity matrix is:

A. 0  
B. 1  
C. -1  
D. 2  

**Answer: B**

### Q4. Matrix multiplication is generally:

A. Commutative  
B. Not commutative  
C. Always zero  
D. Always identity  

**Answer: B**

### Q5. Dot product returns:

A. Scalar  
B. Matrix  
C. Always vector  
D. Tensor  

**Answer: A**

### Q6. Cross product of two 3D vectors returns:

A. Scalar  
B. Vector  
C. Number only  
D. Matrix  

**Answer: B**

### Q7. A matrix is singular when:

A. Determinant = 1  
B. Determinant = 0  
C. Determinant = 5  
D. Rank is always full  

**Answer: B**

### Q8. The inverse of a matrix exists when:

A. Determinant is zero  
B. Determinant is non-zero  
C. Matrix has one row  
D. Matrix is always rectangular  

**Answer: B**

### Q9. Which function calculates the determinant in NumPy?

A. np.sum()  
B. np.linalg.det()  
C. np.mean()  
D. np.array()  

**Answer: B**

### Q10. Which technique uses eigenvalues and eigenvectors for dimensionality reduction?

A. PCA  
B. KNN  
C. Decision Tree  
D. Naive Bayes  

**Answer: A**

### Q11. What is the characteristic equation?

A. det(A + λI) = 0  
B. det(A - λI) = 0  
C. A + B = 0  
D. A × B = 1  

**Answer: B**

### Q12. What is the formula for SVD?

A. A = UΣVᵀ  
B. A = U + V  
C. A = UV  
D. A = U - V  

**Answer: A**

### Q13. Which function solves a linear system in NumPy?

A. np.linalg.solve()  
B. np.linalg.trace()  
C. np.linalg.mean()  
D. np.linalg.sort()  

**Answer: A**

### Q14. What is the rank of a matrix?

A. Sum of elements  
B. Number of columns only  
C. Maximum number of linearly independent rows or columns  
D. Product of diagonal elements  

**Answer: C**

### Q15. Which operation converts rows into columns?

A. Multiplication  
B. Transpose  
C. Addition  
D. Determinant  

**Answer: B**

---