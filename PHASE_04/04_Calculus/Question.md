# 1. INTERVIEW QUESTIONS AND ANSWERS

## Q1. What is Calculus?

Calculus is a branch of mathematics that studies continuous change and accumulation.

## Q2. What are the two main branches of Calculus?

Differential Calculus and Integral Calculus.

## Q3. What is a function?

A function assigns exactly one output to every valid input.

## Q4. What is a limit?

A limit describes the value a function approaches as its input approaches a particular point.

## Q5. What is continuity?

A function is continuous at a point if its limit exists and equals its function value there.

## Q6. What is a derivative?

A derivative measures the instantaneous rate of change of a function.

## Q7. What is the Chain Rule?

The Chain Rule differentiates composite functions by multiplying the derivative of the outer function by the derivative of the inner function.

## Q8. What is a partial derivative?

A partial derivative measures the change in a multivariable function with respect to one variable while keeping the others constant.

## Q9. What is a gradient?

A gradient is a vector of first-order partial derivatives.

## Q10. What is a Jacobian?

A Jacobian is a matrix of first-order partial derivatives of a vector-valued function.

## Q11. What is a Hessian?

A Hessian is a matrix of second-order partial derivatives of a scalar-valued function.

## Q12. What is integration?

Integration calculates accumulation and is the reverse operation of differentiation for suitable functions.

## Q13. What is the difference between definite and indefinite integration?

Definite integration has limits and returns a numerical value. Indefinite integration returns a family of antiderivatives with a constant of integration.

## Q14. What is Gradient Descent?

An iterative optimization algorithm that updates parameters in the direction of the negative gradient.

## Q15. What is the Chain Rule's role in Deep Learning?

It enables backpropagation to calculate gradients through multiple layers of a neural network.

## Q16. What is a learning rate?

It controls the size of parameter updates during optimization.

## Q17. What is a local minimum?

A point whose function value is less than or equal to nearby function values.

## Q18. What is the Taylor Series?

A representation of a function using its derivatives evaluated at a particular point, where the series converges appropriately.

## Q19. What is backpropagation?

An algorithm that computes neural network parameter gradients by applying the Chain Rule backward through the network.

## Q20. Which Python library supports symbolic differentiation?

SymPy.

---

# 2. PRACTICE QUESTIONS WITH SOLUTIONS

## BEGINNER LEVEL

### Q1. Find the derivative.

$$
f(x)=x^3
$$

Solution:

$$
f'(x)=3x^2
$$

### Q2. Differentiate.

$$
f(x)=5x^2+3x+7
$$

Solution:

$$
f'(x)=10x+3
$$

### Q3. Find the limit.

$$
\lim_{x\to2}(x^2+3)
$$

Solution:

$$
=2^2+3
$$

$$
\boxed{7}
$$

### Q4. Integrate.

$$
\int x^2dx
$$

Solution:

$$
\boxed{\frac{x^3}{3}+C}
$$

### Q5. Find the derivative.

$$
f(x)=e^x
$$

Answer:

$$
\boxed{f'(x)=e^x}
$$

## INTERMEDIATE LEVEL

### Q6. Differentiate using the product rule.

$$
y=x^2\sin x
$$

Solution:

$$
y'=2x\sin x+x^2\cos x
$$

### Q7. Differentiate using the chain rule.

$$
y=(2x+3)^5
$$

Solution:

$$
y'=5(2x+3)^4(2)
$$

$$
\boxed{10(2x+3)^4}
$$

### Q8. Find the derivative using the quotient rule.

$$
y=\frac{x^2}{x+1}
$$

Solution:

$$
\boxed{
y'=\frac{x^2+2x}{(x+1)^2}
}
$$

### Q9. Find the partial derivatives.

$$
f(x,y)=x^2+2xy+3y^2
$$

Solution:

$$
\boxed{
\frac{\partial f}{\partial x}=2x+2y
}
$$

$$
\boxed{
\frac{\partial f}{\partial y}=2x+6y
}
$$

### Q10. Find the indefinite integral.

$$
\int(3x^2+2x+1)dx
$$

Solution:

$$
\boxed{x^3+x^2+x+C}
$$

## ADVANCED LEVEL

### Q11. Find the gradient.

$$
f(x,y)=x^2+3xy+y^2
$$

Solution:

$$
\boxed{
\nabla f=
\begin{bmatrix}
2x+3y\\
3x+2y
\end{bmatrix}
}
$$

### Q12. Find the minimum of the function.

$$
f(x)=x^2-6x+10
$$

First derivative:

$$
f'(x)=2x-6
$$

Set equal to zero:

$$
2x-6=0
$$

$$
x=3
$$

Second derivative:

$$
f''(x)=2>0
$$

Minimum value:

$$
f(3)=9-18+10
$$

$$
\boxed{f(3)=1}
$$

### Q13. Calculate the definite integral.

$$
\int_0^3 2x\,dx
$$

Solution:

$$
=[x^2]_0^3
$$

$$
=9-0
$$

$$
\boxed{9}
$$

### Q14. Perform one Gradient Descent update.

Given:

$$
J(w)=(w-5)^2
$$

Initial weight:

$$
w=1
$$

Learning rate:

$$
\alpha=0.1
$$

Gradient:

$$
J'(w)=2(w-5)
$$

$$
=2(1-5)=-8
$$

Update:

$$
w_{new}=1-0.1(-8)
$$

$$
\boxed{w_{new}=1.8}
$$

### Q15. Find the second derivative.

$$
f(x)=x^5+2x^3
$$

First derivative:

$$
f'(x)=5x^4+6x^2
$$

Second derivative:

$$
\boxed{f''(x)=20x^3+12x}
$$

---

# 3. MULTIPLE CHOICE QUESTIONS (MCQs)

### Q1. Calculus mainly studies:

A. Sorting  
B. Continuous change and accumulation  
C. Database management  
D. Programming syntax  

**Answer: B**

### Q2. The derivative of a constant is:

A. 1  
B. 0  
C. x  
D. Infinity  

**Answer: B**

### Q3. Derivative of x⁴ is:

A. x³  
B. 4x³  
C. 4x  
D. x⁵  

**Answer: B**

### Q4. Which rule is used for composite functions?

A. Product Rule  
B. Quotient Rule  
C. Chain Rule  
D. Sum Rule  

**Answer: C**

### Q5. The derivative of sin x is:

A. -sin x  
B. cos x  
C. tan x  
D. -cos x  

**Answer: B**

### Q6. The derivative of eˣ is:

A. 0  
B. 1  
C. eˣ  
D. xeˣ  

**Answer: C**

### Q7. Which symbol represents a partial derivative?

A. ∫  
B. ∂  
C. Σ  
D. Π  

**Answer: B**

### Q8. A gradient is:

A. A scalar only  
B. A vector of partial derivatives  
C. An integral  
D. A constant  

**Answer: B**

### Q9. Which matrix contains second-order partial derivatives?

A. Jacobian  
B. Identity  
C. Hessian  
D. Diagonal  

**Answer: C**

### Q10. Integration is related to:

A. Accumulation  
B. Sorting  
C. Searching  
D. Classification only  

**Answer: A**

### Q11. Which formula represents Gradient Descent?

A. θ + α∇J(θ)  
B. θ - α∇J(θ)  
C. θ × α  
D. θ / α  

**Answer: B**

### Q12. Which rule is important for neural network backpropagation?

A. Chain Rule  
B. Factorial Rule  
C. Sorting Rule  
D. Matrix Addition Rule  

**Answer: A**

### Q13. Which library supports symbolic differentiation in Python?

A. Flask  
B. SymPy  
C. Requests  
D. BeautifulSoup  

**Answer: B**

### Q14. A local minimum may be identified using:

A. First and second derivative tests  
B. Sorting  
C. Database indexing  
D. String matching  

**Answer: A**

### Q15. The learning rate controls:

A. Dataset size  
B. Parameter update size  
C. Number of features  
D. Number of classes  

**Answer: B**

---
