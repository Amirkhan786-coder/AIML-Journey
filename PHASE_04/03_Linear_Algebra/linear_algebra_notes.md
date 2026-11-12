
# PHASE 04 — MATHEMATICS & STATISTICS
# PART 03 — LINEAR ALGEBRA

---

# 1. INTRODUCTION TO LINEAR ALGEBRA

## 1.1 What is Linear Algebra?

**Definition:** Linear Algebra is a branch of mathematics that studies vectors, matrices, linear equations, and linear transformations.

In simple words:

Linear Algebra mein hum numbers ko vectors aur matrices ke form mein represent karna aur un par mathematical operations perform karna seekhte hain.

### Real-world examples

- Images are represented as matrices of pixel values.
- Machine Learning datasets are represented as matrices.
- Neural networks perform matrix multiplication.
- Computer graphics use vectors and transformations.
- Recommendation systems use matrix factorization.

## 1.2 Why is Linear Algebra Important in AI/ML?

| AI/ML Concept | Linear Algebra Usage |
|---|---|
| Machine Learning | Matrix and vector operations |
| Deep Learning | Matrix multiplication |
| Neural Networks | Weights and activations |
| Computer Vision | Image matrices |
| NLP | Word embeddings |
| Recommendation Systems | Matrix factorization |
| PCA | Eigenvalues and eigenvectors |

---

# 2. SCALARS, VECTORS, MATRICES AND TENSORS

## 2.1 Scalar

A scalar is a single numerical value.

Examples:

$$
a=5
$$

$$
b=10.5
$$

Scalars have magnitude but no direction.

AI/ML example:

A model's learning rate:

$$
\alpha=0.01
$$

## 2.2 Vector

A vector is an ordered collection of numbers.

It has magnitude and direction.

Example:

$$
\vec{v}=
\begin{bmatrix}
2\\
4\\
6
\end{bmatrix}
$$

This vector has three components.

It is called a 3-dimensional vector.

### Row Vector

$$
A=
\begin{bmatrix}
2 & 4 & 6
\end{bmatrix}
$$

### Column Vector

$$
B=
\begin{bmatrix}
2\\
4\\
6
\end{bmatrix}
$$

## 2.3 Matrix

A matrix is a rectangular arrangement of numbers in rows and columns.

Example:

$$
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}
$$

This matrix has:

- 2 rows.
- 3 columns.

Therefore, its order is:

$$
2\times3
$$

## 2.4 Tensor

A tensor is a generalized mathematical object that can represent scalars, vectors, matrices, and higher-dimensional arrays.

Examples:

- 0D tensor: Scalar.
- 1D tensor: Vector.
- 2D tensor: Matrix.
- 3D tensor: Three-dimensional array.
- 4D tensor: Four-dimensional array.

### Tensor Example

```python
import numpy as np

scalar = np.array(5)

vector = np.array([1, 2, 3])

matrix = np.array([
    [1, 2],
    [3, 4]
])

tensor = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(scalar.ndim)
print(vector.ndim)
print(matrix.ndim)
print(tensor.ndim)
```

Output:

```text
0
1
2
3
```

---

# 3. TYPES OF MATRICES

## 3.1 Row Matrix

A matrix containing only one row.

$$
A=
\begin{bmatrix}
1 & 2 & 3
\end{bmatrix}
$$

Order:

$$
1\times3
$$

## 3.2 Column Matrix

A matrix containing only one column.

$$
A=
\begin{bmatrix}
1\\
2\\
3
\end{bmatrix}
$$

Order:

$$
3\times1
$$

## 3.3 Rectangular Matrix

Number of rows and columns are different.

$$
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}
$$

Order:

$$
2\times3
$$

## 3.4 Square Matrix

Number of rows equals number of columns.

$$
A=
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix}
$$

Order:

$$
2\times2
$$

## 3.5 Zero Matrix

All elements are zero.

$$
A=
\begin{bmatrix}
0 & 0\\
0 & 0
\end{bmatrix}
$$

## 3.6 Identity Matrix

A square matrix with 1 on the main diagonal and 0 elsewhere.

$$
I=
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
$$

Important property:

$$
AI=IA=A
$$

## 3.7 Diagonal Matrix

All non-diagonal elements are zero.

$$
A=
\begin{bmatrix}
2 & 0 & 0\\
0 & 4 & 0\\
0 & 0 & 6
\end{bmatrix}
$$

## 3.8 Scalar Matrix

A diagonal matrix whose diagonal elements are equal.

$$
A=
\begin{bmatrix}
5 & 0\\
0 & 5
\end{bmatrix}
$$

## 3.9 Upper Triangular Matrix

All elements below the main diagonal are zero.

$$
A=
\begin{bmatrix}
1 & 2 & 3\\
0 & 4 & 5\\
0 & 0 & 6
\end{bmatrix}
$$

## 3.10 Lower Triangular Matrix

All elements above the main diagonal are zero.

$$
A=
\begin{bmatrix}
1 & 0 & 0\\
2 & 3 & 0\\
4 & 5 & 6
\end{bmatrix}
$$

## 3.11 Symmetric Matrix

A square matrix is symmetric if its transpose is equal to itself.

$$
A^T=A
$$

Example:

$$
A=
\begin{bmatrix}
1 & 2\\
2 & 3
\end{bmatrix}
$$

## 3.12 Skew-Symmetric Matrix

A square matrix is skew-symmetric if its transpose is equal to its negative.

$$
A^T=-A
$$

Example:

$$
A=
\begin{bmatrix}
0 & 2\\
-2 & 0
\end{bmatrix}
$$

---

# 4. MATRIX DIMENSIONS AND INDEXING

## 4.1 Matrix Order

If a matrix has m rows and n columns, its order is:

$$
m\times n
$$

Example:

$$
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}
$$

Order:

$$
2\times3
$$

## 4.2 Matrix Elements

The element in the ith row and jth column is represented by:

$$
a_{ij}
$$

Example:

$$
A=
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix}
$$

Here:

$$
a_{12}=2
$$

$$
a_{21}=3
$$

## 4.3 Python Matrix Indexing

```python
import numpy as np

A = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(A[0, 0])
print(A[0, 2])
print(A[1, 1])
```

Output:

```text
10
30
50
```

Remember: Python indexing starts from 0.

---

# 5. VECTOR OPERATIONS

## 5.1 Vector Addition

Two vectors of the same dimension can be added by adding corresponding components.

Formula:

$$
A+B=
\begin{bmatrix}
a_1+b_1\\
a_2+b_2
\end{bmatrix}
$$

Example:

$$
A=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

$$
B=
\begin{bmatrix}
4\\
5
\end{bmatrix}
$$

Addition:

$$
A+B=
\begin{bmatrix}
2+4\\
3+5
\end{bmatrix}
$$

$$
\boxed{
A+B=
\begin{bmatrix}
6\\
8
\end{bmatrix}
}
$$

## 5.2 Vector Subtraction

$$
A-B=
\begin{bmatrix}
2-4\\
3-5
\end{bmatrix}
$$

$$
\boxed{
A-B=
\begin{bmatrix}
-2\\
-2
\end{bmatrix}
}
$$

## 5.3 Scalar Multiplication

Multiplying every vector component by a scalar.

$$
3A=
3
\begin{bmatrix}
2\\
4
\end{bmatrix}
$$

$$
\boxed{
3A=
\begin{bmatrix}
6\\
12
\end{bmatrix}
}
$$

## 5.4 Vector Magnitude (Norm)

The magnitude of a vector is its length.

For a vector:

$$
A=
\begin{bmatrix}
a_1\\
a_2\\
\vdots\\
a_n
\end{bmatrix}
$$

Euclidean norm:

$$
\|A\|_2=\sqrt{a_1^2+a_2^2+\cdots+a_n^2}
$$

Example:

$$
A=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

$$
\|A\|_2=\sqrt{3^2+4^2}
$$

$$
=\sqrt{9+16}
$$

$$
\boxed{\|A\|_2=5}
$$

## 5.5 Unit Vector

A unit vector has magnitude equal to 1.

Formula:

$$
\hat A=\frac{A}{\|A\|}
$$

Example:

$$
A=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

$$
\hat A=
\frac{1}{5}
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

$$
\boxed{
\hat A=
\begin{bmatrix}
0.6\\
0.8
\end{bmatrix}
}
$$

---

# 6. DOT PRODUCT

## 6.1 Definition

The dot product is an operation that multiplies corresponding vector components and adds the results.

Formula:

$$
A\cdot B=\sum_{i=1}^{n}a_ib_i
$$

For two-dimensional vectors:

$$
A\cdot B=a_1b_1+a_2b_2
$$

### Example

$$
A=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

$$
B=
\begin{bmatrix}
4\\
5
\end{bmatrix}
$$

$$
A\cdot B=(2\times4)+(3\times5)
$$

$$
=8+15
$$

$$
\boxed{A\cdot B=23}
$$

## 6.2 Geometric Interpretation

The dot product is also:

$$
A\cdot B=\|A\|\|B\|\cos\theta
$$

Where θ is the angle between the vectors.

Important:

- Positive dot product: Angle is acute.
- Zero dot product: Vectors are perpendicular, if both are non-zero.
- Negative dot product: Angle is obtuse.

## 6.3 Python Implementation

```python
import numpy as np

A = np.array([2, 3])
B = np.array([4, 5])

result = np.dot(A, B)

print(result)
```

Output:

```text
23
```

## 6.4 AI/ML Application

Dot product is used in:

- Neural network calculations.
- Similarity calculations.
- Word embeddings.
- Linear regression.
- Attention mechanisms in Transformers.

---

# 7. CROSS PRODUCT

## 7.1 Definition

The cross product is an operation on two three-dimensional vectors that produces another vector perpendicular to both input vectors.

Formula:

$$
A\times B=
\begin{bmatrix}
a_2b_3-a_3b_2\\
a_3b_1-a_1b_3\\
a_1b_2-a_2b_1
\end{bmatrix}
$$

### Example

$$
A=
\begin{bmatrix}
1\\
2\\
3
\end{bmatrix}
$$

$$
B=
\begin{bmatrix}
4\\
5\\
6
\end{bmatrix}
$$

$$
A\times B=
\begin{bmatrix}
(2)(6)-(3)(5)\\
(3)(4)-(1)(6)\\
(1)(5)-(2)(4)
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
12-15\\
12-6\\
5-8
\end{bmatrix}
$$

$$
\boxed{
A\times B=
\begin{bmatrix}
-3\\
6\\
-3
\end{bmatrix}
}
$$

## 7.2 Python Implementation

```python
import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

result = np.cross(A, B)

print(result)
```

Output:

```text
[-3  6 -3]
```

Applications:
- 3D graphics.
- Computer vision geometry.
- Physics simulations.
- Robotics.

---

# 8. MATRIX ADDITION AND SUBTRACTION

## 8.1 Matrix Addition

Two matrices can be added only if they have the same dimensions.

Formula:

$$
C=A+B
$$

Each corresponding element is added.

### Example

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

$$
A+B=
\begin{bmatrix}
1+5 & 2+6\\
3+7 & 4+8
\end{bmatrix}
$$

$$
\boxed{
A+B=
\begin{bmatrix}
6 & 8\\
10 & 12
\end{bmatrix}
}
$$

## 8.2 Matrix Subtraction

$$
A-B=
\begin{bmatrix}
1-5 & 2-6\\
3-7 & 4-8
\end{bmatrix}
$$

$$
\boxed{
A-B=
\begin{bmatrix}
-4 & -4\\
-4 & -4
\end{bmatrix}
}
$$

## 8.3 Python Implementation

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Addition:")
print(A + B)

print("Subtraction:")
print(A - B)
```

---

# 9. MATRIX SCALAR MULTIPLICATION

Every element of a matrix is multiplied by the scalar.

Formula:

$$
kA=
\begin{bmatrix}
ka_{11} & ka_{12}\\
ka_{21} & ka_{22}
\end{bmatrix}
$$

Example:

$$
A=
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix}
$$

$$
3A=
\begin{bmatrix}
3 & 6\\
9 & 12
\end{bmatrix}
$$

Python:

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

print(3 * A)
```

---

# 10. MATRIX MULTIPLICATION

## 10.1 Definition

Matrix multiplication is an operation in which rows of the first matrix are multiplied by columns of the second matrix.

## 10.2 Dimension Rule

If:

$$
A_{m\times n}
$$

and:

$$
B_{n\times p}
$$

Then:

$$
AB=C_{m\times p}
$$

Important condition:

Number of columns in A must equal the number of rows in B.

### Example

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

Calculate AB:

First row, first column:

$$
(1\times5)+(2\times7)=19
$$

First row, second column:

$$
(1\times6)+(2\times8)=22
$$

Second row, first column:

$$
(3\times5)+(4\times7)=43
$$

Second row, second column:

$$
(3\times6)+(4\times8)=50
$$

Final result:

$$
\boxed{
AB=
\begin{bmatrix}
19 & 22\\
43 & 50
\end{bmatrix}
}
$$

## 10.3 Important Properties

Matrix multiplication is generally not commutative.

$$
AB\neq BA
$$

It is associative:

$$
(AB)C=A(BC)
$$

It is distributive:

$$
A(B+C)=AB+AC
$$

## 10.4 Python Implementation

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

result = A @ B

print(result)
```

Output:

```text
[[19 22]
 [43 50]]
```

Note:

- `A * B` performs element-wise multiplication.
- `A @ B` performs matrix multiplication.
- `np.matmul(A, B)` also performs matrix multiplication.

---

# 11. ELEMENT-WISE MULTIPLICATION

Element-wise multiplication multiplies corresponding elements of two same-shaped arrays.

Formula:

$$
C_{ij}=A_{ij}B_{ij}
$$

Example:

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

$$
A\odot B=
\begin{bmatrix}
1(5) & 2(6)\\
3(7) & 4(8)
\end{bmatrix}
$$

$$
\boxed{
A\odot B=
\begin{bmatrix}
5 & 12\\
21 & 32
\end{bmatrix}
}
$$

Python:

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A * B)
```

---

# 12. TRANSPOSE OF A MATRIX

## 12.1 Definition

Transpose is an operation that converts rows into columns and columns into rows.

It is represented by:

$$
A^T
$$

Example:

$$
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}
$$

Transpose:

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

Original dimension:

$$
2\times3
$$

Transposed dimension:

$$
3\times2
$$

## 12.2 Properties

$$
(A^T)^T=A
$$

$$
(A+B)^T=A^T+B^T
$$

$$
(AB)^T=B^TA^T
$$

## 12.3 Python Implementation

```python
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.T)
```

---

# 13. DETERMINANT OF A MATRIX

## 13.1 Definition

A determinant is a scalar value calculated from a square matrix.

It is represented by:

$$
|A| \quad \text{or} \quad \det(A)
$$

A determinant helps determine whether a square matrix is invertible.

## 13.2 Determinant of a 2×2 Matrix

For:

$$
A=
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
$$

Formula:

$$
\boxed{\det(A)=ad-bc}
$$

### Example

$$
A=
\begin{bmatrix}
2 & 3\\
1 & 4
\end{bmatrix}
$$

$$
\det(A)=(2\times4)-(3\times1)
$$

$$
=8-3
$$

$$
\boxed{\det(A)=5}
$$

## 13.3 Determinant of a 3×3 Matrix

For:

$$
A=
\begin{bmatrix}
a & b & c\\
d & e & f\\
g & h & i
\end{bmatrix}
$$

Formula:

$$
\det(A)=a(ei-fh)-b(di-fg)+c(dh-eg)
$$

### Example

$$
A=
\begin{bmatrix}
1 & 2 & 3\\
0 & 1 & 4\\
5 & 6 & 0
\end{bmatrix}
$$

$$
\det(A)=1(1\times0-4\times6)
$$

$$
-2(0\times0-4\times5)
$$

$$
+3(0\times6-1\times5)
$$

$$
=-24+40-15
$$

$$
\boxed{\det(A)=1}
$$

## 13.4 Important Properties

- If determinant is zero, the square matrix is singular.
- If determinant is non-zero, the matrix is invertible.
- Determinant of identity matrix is 1.
- Determinant of a triangular matrix equals the product of its diagonal entries.

## 13.5 Python Implementation

```python
import numpy as np

A = np.array([
    [2, 3],
    [1, 4]
])

det = np.linalg.det(A)

print(det)
```

---

# 14. MINOR AND COFACTOR

## 14.1 Minor

The minor of an element is the determinant obtained by deleting the row and column containing that element.

For element aᵢⱼ, its minor is represented by:

$$
M_{ij}
$$

### Example

$$
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{bmatrix}
$$

Find the minor of element 5.

Delete its row and column:

$$
\begin{bmatrix}
1 & 3\\
7 & 9
\end{bmatrix}
$$

$$
M_{22}=1(9)-3(7)
$$

$$
\boxed{M_{22}=-12}
$$

## 14.2 Cofactor

Cofactor is calculated using:

$$
C_{ij}=(-1)^{i+j}M_{ij}
$$

For the previous example:

$$
C_{22}=(-1)^{2+2}(-12)
$$

$$
\boxed{C_{22}=-12}
$$

Sign pattern:

$$
\begin{bmatrix}
+ & - & +\\
- & + & -\\
+ & - & +
\end{bmatrix}
$$

---

# 15. ADJOINT OF A MATRIX

## 15.1 Definition

The adjoint (also called adjugate) of a square matrix is the transpose of its cofactor matrix.

Formula:

$$
\operatorname{adj}(A)=C^T
$$

Where C is the cofactor matrix.

Example:

$$
A=
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
$$

Cofactor matrix:

$$
C=
\begin{bmatrix}
d & -c\\
-b & a
\end{bmatrix}
$$

Adjoint:

$$
\boxed{
\operatorname{adj}(A)=
\begin{bmatrix}
d & -b\\
-c & a
\end{bmatrix}
}
$$

---

# 16. INVERSE OF A MATRIX

## 16.1 Definition

The inverse of a square matrix is a matrix that produces the identity matrix when multiplied by the original matrix.

It is represented by:

$$
A^{-1}
$$

Formula:

$$
AA^{-1}=A^{-1}A=I
$$

## 16.2 Inverse Formula

For a square matrix with non-zero determinant:

$$
\boxed{
A^{-1}=\frac{\operatorname{adj}(A)}{\det(A)}
}
$$

Condition:

$$
\det(A)\neq0
$$

## 16.3 Inverse of a 2×2 Matrix

For:

$$
A=
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
$$

Formula:

$$
A^{-1}=
\frac{1}{ad-bc}
\begin{bmatrix}
d & -b\\
-c & a
\end{bmatrix}
$$

### Example

$$
A=
\begin{bmatrix}
2 & 1\\
1 & 1
\end{bmatrix}
$$

Step 1: Calculate determinant.

$$
\det(A)=2(1)-1(1)=1
$$

Step 2: Find adjoint.

$$
\operatorname{adj}(A)=
\begin{bmatrix}
1 & -1\\
-1 & 2
\end{bmatrix}
$$

Step 3: Calculate inverse.

$$
A^{-1}=\frac11
\begin{bmatrix}
1 & -1\\
-1 & 2
\end{bmatrix}
$$

Final answer:

$$
\boxed{
A^{-1}=
\begin{bmatrix}
1 & -1\\
-1 & 2
\end{bmatrix}
}
$$

## 16.4 Python Implementation

```python
import numpy as np

A = np.array([
    [2, 1],
    [1, 1]
])

inverse = np.linalg.inv(A)

print(inverse)
```

## 16.5 Singular Matrix

A square matrix is singular if its determinant is zero.

$$
\det(A)=0
$$

Such a matrix does not have an ordinary inverse.

## 16.6 Non-Singular Matrix

A square matrix is non-singular if its determinant is non-zero.

$$
\det(A)\neq0
$$

It has an inverse.

---

# 17. RANK OF A MATRIX

## 17.1 Definition

The rank of a matrix is the maximum number of linearly independent rows or columns.

It is represented by:

$$
\operatorname{rank}(A)
$$

### Example

$$
A=
\begin{bmatrix}
1 & 2\\
2 & 4
\end{bmatrix}
$$

Second row is twice the first row.

Therefore, only one row is linearly independent.

$$
\boxed{\operatorname{rank}(A)=1}
$$

## 17.2 Important Properties

For an m × n matrix:

$$
0\leq\operatorname{rank}(A)\leq\min(m,n)
$$

For a square n × n matrix:

$$
\operatorname{rank}(A)=n
$$

means the matrix has full rank.

## 17.3 Python Implementation

```python
import numpy as np

A = np.array([
    [1, 2],
    [2, 4]
])

print(np.linalg.matrix_rank(A))
```

---

# 18. TRACE OF A MATRIX

## 18.1 Definition

The trace of a square matrix is the sum of its main diagonal elements.

Formula:

$$
\operatorname{tr}(A)=\sum_{i=1}^{n}a_{ii}
$$

Example:

$$
A=
\begin{bmatrix}
2 & 3\\
4 & 5
\end{bmatrix}
$$

$$
\operatorname{tr}(A)=2+5
$$

$$
\boxed{\operatorname{tr}(A)=7}
$$

Python:

```python
import numpy as np

A = np.array([
    [2, 3],
    [4, 5]
])

print(np.trace(A))
```

---

# 19. LINEAR EQUATIONS

## 19.1 Definition

A linear equation is an equation in which variables have degree one.

Example:

$$
2x+3y=8
$$

Another example:

$$
x+y=5
$$

## 19.2 System of Linear Equations

Consider:

$$
2x+y=5
$$

$$
x+y=3
$$

Matrix form:

$$
AX=B
$$

Where:

$$
A=
\begin{bmatrix}
2 & 1\\
1 & 1
\end{bmatrix}
$$

$$
X=
\begin{bmatrix}
x\\
y
\end{bmatrix}
$$

$$
B=
\begin{bmatrix}
5\\
3
\end{bmatrix}
$$

If A is invertible:

$$
X=A^{-1}B
$$

Solution:

$$
x=2,\quad y=1
$$

## 19.3 Python Implementation

```python
import numpy as np

A = np.array([
    [2, 1],
    [1, 1]
])

B = np.array([5, 3])

solution = np.linalg.solve(A, B)

print(solution)
```

Output:

```text
[2. 1.]
```

---

# 20. LINEAR INDEPENDENCE AND DEPENDENCE

## 20.1 Linearly Independent Vectors

Vectors are linearly independent if no vector can be expressed as a linear combination of the others.

For vectors v1, v2, ..., vn:

$$
c_1v_1+c_2v_2+\cdots+c_nv_n=0
$$

The vectors are linearly independent if the only solution is:

$$
c_1=c_2=\cdots=c_n=0
$$

Example:

$$
v_1=
\begin{bmatrix}
1\\
0
\end{bmatrix}
,\quad
v_2=
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

These vectors are linearly independent.

## 20.2 Linearly Dependent Vectors

Vectors are dependent if at least one vector can be represented as a linear combination of the others.

Example:

$$
v_1=
\begin{bmatrix}
1\\
2
\end{bmatrix}
,\quad
v_2=
\begin{bmatrix}
2\\
4
\end{bmatrix}
$$

Because:

$$
v_2=2v_1
$$

They are linearly dependent.

## 20.3 AI/ML Application

Linear independence is important in:

- Feature redundancy detection.
- Multicollinearity.
- Matrix rank.
- Model parameter estimation.
- Dimensionality reduction.

---

# 21. BASIS AND DIMENSION

## 21.1 Basis

A basis is a set of linearly independent vectors that spans a vector space.

Example: Standard basis of R²:

$$
e_1=
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

$$
e_2=
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

These vectors form a basis for R².

## 21.2 Dimension

Dimension is the number of vectors in a basis of a vector space.

Examples:

- R¹ has dimension 1.
- R² has dimension 2.
- R³ has dimension 3.

---

# 22. VECTOR SPACES

## 22.1 Definition

A vector space is a collection of vectors that is closed under vector addition and scalar multiplication and satisfies the vector-space axioms.

In simple words:

Vector space ek mathematical set hai jahan vectors ko add karne aur scalar se multiply karne par result bhi usi space mein rehta hai.

Example:

$$
\mathbb R^2
$$

is the set of all two-dimensional real vectors.

A vector in R²:

$$
v=
\begin{bmatrix}
x\\
y
\end{bmatrix}
$$

Where x and y are real numbers.

---

# 23. EIGENVALUES AND EIGENVECTORS

## 23.1 Definition

An eigenvector of a square matrix is a non-zero vector whose direction remains unchanged after multiplication by the matrix, except for possible reversal of direction.

The corresponding scaling factor is called an eigenvalue.

## 23.2 Formula

$$
Av=\lambda v
$$

Where:

- A = Square matrix.
- v = Eigenvector.
- λ = Eigenvalue.

Rearranging:

$$
(A-\lambda I)v=0
$$

Characteristic equation:

$$
\boxed{\det(A-\lambda I)=0}
$$

## 23.3 Numerical Example

Given:

$$
A=
\begin{bmatrix}
2 & 0\\
0 & 3
\end{bmatrix}
$$

Find its eigenvalues.

Step 1: Write characteristic equation.

$$
\det(A-\lambda I)=0
$$

$$
\begin{vmatrix}
2-\lambda & 0\\
0 & 3-\lambda
\end{vmatrix}=0
$$

Step 2: Calculate determinant.

$$
(2-\lambda)(3-\lambda)=0
$$

Step 3: Solve.

$$
\boxed{\lambda_1=2,\quad\lambda_2=3}
$$

Corresponding eigenvectors can be:

For λ = 2:

$$
v_1=
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

For λ = 3:

$$
v_2=
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

## 23.4 Python Implementation

```python
import numpy as np

A = np.array([
    [2, 0],
    [0, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)
```

## 23.5 AI/ML Applications

- Principal Component Analysis (PCA).
- Dimensionality reduction.
- Image compression.
- Spectral clustering.
- Understanding matrix transformations.

---

# 24. MATRIX DIAGONALIZATION

## 24.1 Definition

Diagonalization is the process of representing a square matrix in diagonal form using a suitable basis of eigenvectors.

Formula:

$$
A=PDP^{-1}
$$

Where:

- P = Matrix of linearly independent eigenvectors.
- D = Diagonal matrix of eigenvalues.
- P⁻¹ = Inverse of P.

A matrix is diagonalizable if it has enough linearly independent eigenvectors to form P.

### Example

For:

$$
A=
\begin{bmatrix}
2 & 0\\
0 & 3
\end{bmatrix}
$$

It is already diagonal, so:

$$
P=I,\quad D=A
$$

---

# 25. ORTHOGONAL VECTORS AND MATRICES

## 25.1 Orthogonal Vectors

Two vectors are orthogonal if their dot product is zero.

$$
A\cdot B=0
$$

Example:

$$
A=
\begin{bmatrix}
1\\
0
\end{bmatrix}
,\quad
B=
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

$$
A\cdot B=1(0)+0(1)=0
$$

Therefore, they are orthogonal.

## 25.2 Orthonormal Vectors

Vectors are orthonormal if:

1. They are mutually orthogonal.
2. Each vector has magnitude 1.

## 25.3 Orthogonal Matrix

A square matrix Q is orthogonal if:

$$
Q^TQ=QQ^T=I
$$

Therefore:

$$
Q^{-1}=Q^T
$$

Applications:
- Computer graphics.
- Coordinate transformations.
- Numerical algorithms.
- PCA.

---

# 26. MATRIX TRANSFORMATIONS

## 26.1 Definition

A linear transformation is a mapping between vector spaces that preserves vector addition and scalar multiplication.

A transformation T is linear if:

$$
T(u+v)=T(u)+T(v)
$$

and:

$$
T(cv)=cT(v)
$$

Matrix representation:

$$
y=Ax
$$

Where A represents the transformation.

## 26.2 Scaling

A scaling transformation changes the size of a vector.

$$
A=
\begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix}
$$

For:

$$
x=
\begin{bmatrix}
1\\
2
\end{bmatrix}
$$

Then:

$$
Ax=
\begin{bmatrix}
2\\
4
\end{bmatrix}
$$

## 26.3 Rotation

A two-dimensional rotation by angle θ:

$$
R(\theta)=
\begin{bmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{bmatrix}
$$

For 90 degrees:

$$
R(90^\circ)=
\begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$

Applications:
- Image rotation.
- Computer vision.
- Robotics.
- 3D graphics.

---

# 27. SINGULAR VALUE DECOMPOSITION (SVD)

## 27.1 Definition

Singular Value Decomposition is a matrix factorization technique that represents a matrix as the product of three matrices.

Formula:

$$
\boxed{A=U\Sigma V^T}
$$

Where:

- U = Left singular vectors.
- Σ = Diagonal matrix of singular values.
- Vᵀ = Transpose of right singular vectors.

## 27.2 Why SVD is Important?

SVD is used for:

- Dimensionality reduction.
- Image compression.
- Recommendation systems.
- Noise reduction.
- Data approximation.

## 27.3 Python Implementation

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

U, S, VT = np.linalg.svd(A)

print("U:")
print(U)

print("Singular Values:")
print(S)

print("VT:")
print(VT)
```

Note: `np.linalg.svd()` returns singular values as a one-dimensional array. They can be placed on the diagonal of Σ.

---

# 28. PRINCIPAL COMPONENT ANALYSIS (PCA)

## 28.1 Definition

Principal Component Analysis is a dimensionality reduction technique that transforms data into a new set of orthogonal directions called principal components.

These components are ordered by the amount of variance they explain.

## 28.2 Why PCA is Used?

- Reduce number of features.
- Remove redundant dimensions.
- Visualize high-dimensional data.
- Reduce computational cost.
- Compress information.

## 28.3 Basic PCA Steps

1. Standardize the dataset when features have different scales.
2. Calculate the covariance matrix.
3. Calculate eigenvalues and eigenvectors.
4. Sort components by decreasing eigenvalues.
5. Select the top k components.
6. Project the data onto the selected components.

## 28.4 Python Implementation

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = np.array([
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7]
])

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=1)

X_reduced = pca.fit_transform(X_scaled)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_reduced.shape)
print(X_reduced)
```

Explanation:

- `StandardScaler()`: Standardizes features.
- `fit_transform()`: Learns scaling parameters and transforms data.
- `PCA(n_components=1)`: Selects one principal component.
- `fit_transform()`: Learns PCA directions and projects the data.
- `shape`: Displays the dimensions.

---

# 29. LEAST SQUARES METHOD

## 29.1 Definition

The Least Squares Method estimates unknown parameters by minimizing the sum of squared differences between observed and predicted values.

For a linear system:

$$
Ax\approx b
$$

The objective is:

$$
\boxed{\min_x\|Ax-b\|_2^2}
$$

## 29.2 Linear Regression Connection

Linear regression can be written as:

$$
y=Xw+b
$$

Where:

- X = Feature matrix.
- w = Model weights.
- b = Bias.
- y = Predicted output.

A common least-squares objective is:

$$
\min_w\|Xw-y\|_2^2
$$

If X has full column rank, the ordinary least-squares solution is:

$$
w=(X^TX)^{-1}X^Ty
$$

In practice, numerical solvers such as QR or SVD are often preferred over explicitly calculating the inverse.

---

# 30. NUMPY LINEAR ALGEBRA FUNCTIONS

| Function | Purpose |
|---|---|
| np.array() | Creates arrays |
| np.dot() | Dot product |
| np.cross() | Cross product |
| np.matmul() | Matrix multiplication |
| np.transpose() | Matrix transpose |
| np.linalg.det() | Determinant |
| np.linalg.inv() | Matrix inverse |
| np.linalg.solve() | Solves linear systems |
| np.linalg.matrix_rank() | Matrix rank |
| np.trace() | Matrix trace |
| np.linalg.eig() | Eigenvalues and eigenvectors |
| np.linalg.svd() | Singular Value Decomposition |
| np.linalg.norm() | Vector or matrix norm |
| np.linalg.pinv() | Moore-Penrose pseudoinverse |

---

# 31. COMPLETE PYTHON PRACTICE

```python
import numpy as np

# Create vectors
A = np.array([2, 3])
B = np.array([4, 5])

print("Vector Addition:", A + B)
print("Vector Subtraction:", A - B)

# Dot product
print("Dot Product:", np.dot(A, B))

# Vector magnitude
print("Magnitude:", np.linalg.norm(A))

# Create matrices
M1 = np.array([
    [1, 2],
    [3, 4]
])

M2 = np.array([
    [5, 6],
    [7, 8]
])

# Matrix operations
print("Addition:\n", M1 + M2)
print("Subtraction:\n", M1 - M2)
print("Element-wise Multiplication:\n", M1 * M2)
print("Matrix Multiplication:\n", M1 @ M2)

# Transpose
print("Transpose:\n", M1.T)

# Determinant
print("Determinant:", np.linalg.det(M1))

# Inverse
print("Inverse:\n", np.linalg.inv(M1))

# Rank
print("Rank:", np.linalg.matrix_rank(M1))

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(M1)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Solve linear equations
coefficients = np.array([
    [2, 1],
    [1, 1]
])

constants = np.array([5, 3])

solution = np.linalg.solve(coefficients, constants)

print("Solution:", solution)
```

---



