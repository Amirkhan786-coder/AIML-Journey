
# PHASE 04 — MATHEMATICS & STATISTICS
# PART 04 — CALCULUS

---

# 1. INTRODUCTION TO CALCULUS

## 1.1 What is Calculus?

**Definition:** Calculus is a branch of mathematics that studies continuous change and accumulation.

It mainly consists of two major branches:

1. Differential Calculus
2. Integral Calculus

In simple words:

Calculus hume batata hai ki koi quantity kitni fast change ho rahi hai aur small quantities ko combine karke total quantity kaise calculate karni hai.

### Real-world examples

- Speed and acceleration.
- Population growth.
- Distance and velocity.
- Area under a curve.
- Optimization of machine learning models.
- Neural network training.

## 1.2 Types of Calculus

### A. Differential Calculus

Studies rates of change using derivatives.

Example:

Finding the rate at which a car's position changes with time.

### B. Integral Calculus

Studies accumulation and areas using integration.

Example:

Finding total distance from velocity over time.

## 1.3 Importance of Calculus in AI/ML

| AI/ML Concept | Calculus Usage |
|---|---|
| Linear Regression | Gradient calculation |
| Logistic Regression | Derivatives of loss |
| Neural Networks | Backpropagation |
| Deep Learning | Chain Rule |
| Gradient Descent | Optimization |
| Loss Functions | Minimization |
| Probability | Continuous distributions |
| Reinforcement Learning | Policy optimization |

---

# 2. FUNCTIONS

## 2.1 What is a Function?

**Definition:** A function is a mathematical relationship that assigns exactly one output to each valid input.

It is represented by:

$$
y=f(x)
$$

Where:
- x = Input.
- f = Function.
- y = Output.

Example:

$$
f(x)=2x+3
$$

If x = 2:

$$
f(2)=2(2)+3
$$

$$
\boxed{f(2)=7}
$$

## 2.2 Types of Functions

### A. Constant Function

A function whose output remains constant.

$$
f(x)=5
$$

### B. Linear Function

A function whose graph is a straight line.

$$
f(x)=mx+c
$$

Where:
- m = Slope.
- c = Y-intercept.

Example:

$$
f(x)=2x+3
$$

### C. Quadratic Function

A function containing a squared variable.

$$
f(x)=ax^2+bx+c
$$

Example:

$$
f(x)=x^2+2x+1
$$

### D. Polynomial Function

A function containing non-negative integer powers of x.

$$
f(x)=a_nx^n+\cdots+a_1x+a_0
$$

### E. Exponential Function

A function in which the variable appears in the exponent.

$$
f(x)=a^x
$$

Example:

$$
f(x)=2^x
$$

### F. Logarithmic Function

A function that is the inverse of an exponential function.

$$
f(x)=\log_a x
$$

### G. Trigonometric Functions

Important trigonometric functions:

$$
\sin x,\quad \cos x,\quad \tan x
$$

### H. Sigmoid Function

An important function in Machine Learning.

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

Its output lies between 0 and 1.

Used in:
- Logistic Regression.
- Binary classification.
- Neural Networks.

---

# 3. DOMAIN AND RANGE

## 3.1 Domain

Domain is the set of all valid input values for a function.

Example:

$$
f(x)=\frac{1}{x}
$$

Here x cannot be zero.

Domain:

$$
x\in\mathbb R,\quad x\neq0
$$

## 3.2 Range

Range is the set of all possible output values of a function.

Example:

$$
f(x)=x^2
$$

For real x:

$$
f(x)\geq0
$$

Range:

$$
[0,\infty)
$$

## 3.3 Example

Given:

$$
f(x)=x^2+2
$$

For x = 1:

$$
f(1)=1^2+2=3
$$

For x = 2:

$$
f(2)=2^2+2=6
$$

For x = 3:

$$
f(3)=3^2+2=11
$$

---

# 4. LIMITS

## 4.1 Definition

A limit describes the value that a function approaches as its input approaches a particular point.

It is represented by:

$$
\lim_{x\to a}f(x)
$$

In simple words:

Jab x kisi value ke closer jaata hai, toh function ka output kis value ke closer jaata hai, usse limit kehte hain.

## 4.2 Basic Example

Find:

$$
\lim_{x\to2}(x+3)
$$

Direct substitution:

$$
=2+3
$$

$$
\boxed{5}
$$

## 4.3 Another Example

Find:

$$
\lim_{x\to2}(x^2+3x)
$$

Substitute x = 2:

$$
=2^2+3(2)
$$

$$
=4+6
$$

$$
\boxed{10}
$$

## 4.4 Left-Hand Limit (LHL)

The value approached by a function when x approaches a point from the left side.

$$
\lim_{x\to a^-}f(x)
$$

## 4.5 Right-Hand Limit (RHL)

The value approached by a function when x approaches a point from the right side.

$$
\lim_{x\to a^+}f(x)
$$

## 4.6 Condition for a Limit to Exist

A two-sided limit exists when:

$$
\boxed{
\lim_{x\to a^-}f(x)
=
\lim_{x\to a^+}f(x)
}
$$

## 4.7 Important Limit Formulas

$$
\lim_{x\to0}\frac{\sin x}{x}=1
$$

$$
\lim_{x\to0}\frac{1-\cos x}{x^2}=\frac12
$$

$$
\lim_{x\to0}\frac{e^x-1}{x}=1
$$

$$
\lim_{x\to0}\frac{\ln(1+x)}{x}=1
$$

Note: Trigonometric limit formulas use angles measured in radians.

---

# 5. CONTINUITY

## 5.1 Definition

A function is continuous at a point if its limit exists at that point and equals the actual function value.

In simple words:

A continuous function ka graph us point par bina break ya jump ke continue hota hai.

## 5.2 Mathematical Conditions

A function f(x) is continuous at x = a if:

1. f(a) is defined.
2. The limit exists.
3. The limit equals f(a).

Formula:

$$
\boxed{
\lim_{x\to a}f(x)=f(a)
}
$$

## 5.3 Example

Given:

$$
f(x)=x^2+2
$$

Check continuity at x = 2.

Function value:

$$
f(2)=2^2+2=6
$$

Limit:

$$
\lim_{x\to2}(x^2+2)=6
$$

Therefore:

$$
\boxed{\lim_{x\to2}f(x)=f(2)}
$$

The function is continuous at x = 2.

## 5.4 Types of Discontinuity

- Removable discontinuity.
- Jump discontinuity.
- Infinite discontinuity.

---

# 6. DERIVATIVES

## 6.1 What is a Derivative?

**Definition:** A derivative measures the instantaneous rate of change of a function with respect to its independent variable.

It is represented by:

$$
\frac{dy}{dx}
$$

Other notations:

$$
f'(x)
$$

$$
\frac{d}{dx}f(x)
$$

In simple words:

Derivative batata hai ki x mein chhota sa change hone par y kitni fast change hota hai.

### Real-world example

If a car's position is represented by s(t), then its instantaneous velocity is:

$$
v(t)=\frac{ds}{dt}
$$

## 6.2 First Principle of Derivatives

Derivative is defined using limits.

Formula:

$$
\boxed{
f'(x)=
\lim_{h\to0}
\frac{f(x+h)-f(x)}{h}
}
$$

Where:
- f(x) = Original function.
- h = Small change in x.
- f(x+h) = Function after changing x.

### Numerical Example

Find the derivative of:

$$
f(x)=x^2
$$

Using first principles:

$$
f'(x)=
\lim_{h\to0}
\frac{(x+h)^2-x^2}{h}
$$

Expand:

$$
=\lim_{h\to0}
\frac{x^2+2xh+h^2-x^2}{h}
$$

Cancel x²:

$$
=\lim_{h\to0}
\frac{2xh+h^2}{h}
$$

Take h common:

$$
=\lim_{h\to0}(2x+h)
$$

Put h = 0:

$$
\boxed{f'(x)=2x}
$$

---

# 7. BASIC RULES OF DIFFERENTIATION

## 7.1 Constant Rule

The derivative of a constant is zero.

$$
\boxed{\frac{d}{dx}(c)=0}
$$

Example:

$$
\frac{d}{dx}(5)=0
$$

## 7.2 Power Rule

If:

$$
f(x)=x^n
$$

Then:

$$
\boxed{
\frac{d}{dx}(x^n)=nx^{n-1}
}
$$

Example:

$$
f(x)=x^3
$$

$$
f'(x)=3x^2
$$

Another example:

$$
f(x)=x^5
$$

$$
\boxed{f'(x)=5x^4}
$$

## 7.3 Constant Multiple Rule

$$
\frac{d}{dx}[cf(x)]=cf'(x)
$$

Example:

$$
f(x)=5x^3
$$

$$
f'(x)=5(3x^2)
$$

$$
\boxed{f'(x)=15x^2}
$$

## 7.4 Sum Rule

$$
\frac{d}{dx}[f(x)+g(x)]
=
f'(x)+g'(x)
$$

Example:

$$
f(x)=x^2+3x+5
$$

$$
f'(x)=2x+3+0
$$

$$
\boxed{f'(x)=2x+3}
$$

## 7.5 Difference Rule

$$
\frac{d}{dx}[f(x)-g(x)]
=
f'(x)-g'(x)
$$

Example:

$$
f(x)=x^3-2x^2
$$

$$
\boxed{f'(x)=3x^2-4x}
$$

---

# 8. PRODUCT RULE

## 8.1 Definition

Product Rule is used when two differentiable functions are multiplied together.

Formula:

$$
\boxed{
\frac{d}{dx}[uv]
=
u\frac{dv}{dx}
+
v\frac{du}{dx}
}
$$

Short form:

$$
(uv)'=u'v+uv'
$$

### Example

Find the derivative:

$$
y=x^2\sin x
$$

Let:

$$
u=x^2,\quad v=\sin x
$$

Differentiate:

$$
u'=2x,\quad v'=\cos x
$$

Apply product rule:

$$
y'=2x\sin x+x^2\cos x
$$

Final answer:

$$
\boxed{y'=2x\sin x+x^2\cos x}
$$

---

# 9. QUOTIENT RULE

## 9.1 Definition

Quotient Rule is used when one differentiable function is divided by another.

Formula:

$$
\boxed{
\frac{d}{dx}\left(\frac{u}{v}\right)
=
\frac{vu'-uv'}{v^2}
}
$$

Condition:

$$
v\neq0
$$

### Example

Find the derivative:

$$
y=\frac{x^2}{x+1}
$$

Let:

$$
u=x^2,\quad v=x+1
$$

Then:

$$
u'=2x,\quad v'=1
$$

Apply quotient rule:

$$
y'=
\frac{(x+1)(2x)-x^2(1)}
{(x+1)^2}
$$

Expand:

$$
=\frac{2x^2+2x-x^2}{(x+1)^2}
$$

Final answer:

$$
\boxed{
y'=\frac{x^2+2x}{(x+1)^2}
}
$$

---

# 10. CHAIN RULE

## 10.1 Definition

The Chain Rule is used to differentiate composite functions, where one function is inside another function.

In simple words:

Agar function ke andar another function ho, toh outer function aur inner function ko step-by-step differentiate karte hain.

## 10.2 Formula

If:

$$
y=f(g(x))
$$

Then:

$$
\boxed{
\frac{dy}{dx}
=
f'(g(x))\cdot g'(x)
}
$$

Another notation:

$$
\frac{dy}{dx}
=
\frac{dy}{du}\cdot\frac{du}{dx}
$$

## 10.3 Numerical Example

Find the derivative:

$$
y=(3x+2)^4
$$

Step 1: Let inner function be:

$$
u=3x+2
$$

Step 2: Differentiate outer function:

$$
\frac{dy}{du}=4u^3
$$

Step 3: Differentiate inner function:

$$
\frac{du}{dx}=3
$$

Step 4: Apply Chain Rule:

$$
\frac{dy}{dx}
=
4u^3\times3
$$

Substitute u:

$$
\boxed{
\frac{dy}{dx}=12(3x+2)^3
}
$$

## 10.4 AI/ML Application

Chain Rule is the mathematical foundation of backpropagation in neural networks.

A neural network has multiple layers of functions.

Chain Rule calculates how the final loss changes with respect to each layer's weights.

---

# 11. DERIVATIVES OF IMPORTANT FUNCTIONS

## 11.1 Exponential Functions

$$
\frac{d}{dx}(e^x)=e^x
$$

$$
\frac{d}{dx}(a^x)=a^x\ln a
$$

Example:

$$
\frac{d}{dx}(e^{3x})=3e^{3x}
$$

## 11.2 Logarithmic Functions

$$
\frac{d}{dx}(\ln x)=\frac1x
$$

$$
\frac{d}{dx}(\log_a x)=\frac{1}{x\ln a}
$$

Example:

$$
\frac{d}{dx}(\ln(2x+1))
=
\frac{2}{2x+1}
$$

## 11.3 Trigonometric Functions

$$
\frac{d}{dx}(\sin x)=\cos x
$$

$$
\frac{d}{dx}(\cos x)=-\sin x
$$

$$
\frac{d}{dx}(\tan x)=\sec^2x
$$

$$
\frac{d}{dx}(\cot x)=-\csc^2x
$$

$$
\frac{d}{dx}(\sec x)=\sec x\tan x
$$

$$
\frac{d}{dx}(\csc x)=-\csc x\cot x
$$

## 11.4 Inverse Trigonometric Functions

$$
\frac{d}{dx}(\sin^{-1}x)=\frac{1}{\sqrt{1-x^2}}
$$

$$
\frac{d}{dx}(\cos^{-1}x)=-\frac{1}{\sqrt{1-x^2}}
$$

$$
\frac{d}{dx}(\tan^{-1}x)=\frac{1}{1+x^2}
$$

These formulas apply on their respective domains.

---

# 12. HIGHER-ORDER DERIVATIVES

## 12.1 Definition

Higher-order derivatives are derivatives calculated repeatedly from the original function.

First derivative:

$$
f'(x)
$$

Second derivative:

$$
f''(x)
$$

Third derivative:

$$
f'''(x)
$$

nth derivative:

$$
f^{(n)}(x)
$$

### Example

Given:

$$
f(x)=x^4
$$

First derivative:

$$
f'(x)=4x^3
$$

Second derivative:

$$
f''(x)=12x^2
$$

Third derivative:

$$
f'''(x)=24x
$$

Fourth derivative:

$$
\boxed{f^{(4)}(x)=24}
$$

## 12.2 Applications

- Acceleration from position.
- Curvature of functions.
- Optimization.
- Taylor series.
- Analysis of loss functions.

---

# 13. PARTIAL DERIVATIVES

## 13.1 Definition

A partial derivative measures how a multivariable function changes with respect to one variable while keeping the other variables constant.

It is represented by:

$$
\frac{\partial f}{\partial x}
$$

## 13.2 Example

Given:

$$
f(x,y)=x^2+3xy+y^2
$$

Find the partial derivative with respect to x.

Treat y as a constant:

$$
\frac{\partial f}{\partial x}
=
2x+3y
$$

Find the partial derivative with respect to y.

Treat x as a constant:

$$
\frac{\partial f}{\partial y}
=
3x+2y
$$

Final answers:

$$
\boxed{
\frac{\partial f}{\partial x}=2x+3y
}
$$

$$
\boxed{
\frac{\partial f}{\partial y}=3x+2y
}
$$

## 13.3 Numerical Evaluation

For:

$$
f(x,y)=x^2+3xy+y^2
$$

At:

$$
x=2,\quad y=1
$$

Partial derivative with respect to x:

$$
\frac{\partial f}{\partial x}=2x+3y
$$

$$
=2(2)+3(1)
$$

$$
\boxed{7}
$$

Partial derivative with respect to y:

$$
\frac{\partial f}{\partial y}=3x+2y
$$

$$
=3(2)+2(1)
$$

$$
\boxed{8}
$$

## 13.4 AI/ML Application

Partial derivatives are used when a model has multiple parameters.

For example:

$$
L(w_1,w_2)
$$

We calculate:

$$
\frac{\partial L}{\partial w_1}
$$

and:

$$
\frac{\partial L}{\partial w_2}
$$

These values tell us how the loss changes when each parameter changes independently.

---

# 14. IMPLICIT DIFFERENTIATION

## 14.1 Definition

Implicit differentiation is used when x and y are related by an equation instead of y being explicitly written as a function of x.

### Example

Given:

$$
x^2+y^2=25
$$

Differentiate both sides with respect to x:

$$
2x+2y\frac{dy}{dx}=0
$$

Why is there dy/dx?

Because y is also a function of x, so the Chain Rule is applied.

Rearrange:

$$
2y\frac{dy}{dx}=-2x
$$

Final answer:

$$
\boxed{
\frac{dy}{dx}=-\frac{x}{y}
}
$$

---

# 15. LOGARITHMIC DIFFERENTIATION

## 15.1 Definition

Logarithmic differentiation is a technique used to simplify differentiation of complicated products, quotients, and variable powers.

### Example

Given:

$$
y=x^x
$$

Take natural logarithm on both sides:

$$
\ln y=\ln(x^x)
$$

$$
\ln y=x\ln x
$$

Differentiate:

$$
\frac1y\frac{dy}{dx}=\ln x+1
$$

Multiply by y:

$$
\frac{dy}{dx}=y(\ln x+1)
$$

Substitute y:

$$
\boxed{
\frac{dy}{dx}=x^x(\ln x+1)
}
$$

For real-valued differentiation, this example assumes x > 0.

---

# 16. GRADIENT

## 16.1 Definition

The gradient is a vector containing the partial derivatives of a multivariable function.

It points in the direction of steepest increase of a differentiable scalar function.

It is represented by:

$$
\nabla f
$$

## 16.2 Formula

For:

$$
f(x,y,z)
$$

Gradient:

$$
\boxed{
\nabla f=
\begin{bmatrix}
\frac{\partial f}{\partial x}\\
\frac{\partial f}{\partial y}\\
\frac{\partial f}{\partial z}
\end{bmatrix}
}
$$

## 16.3 Numerical Example

Given:

$$
f(x,y)=x^2+3xy+y^2
$$

We already calculated:

$$
\frac{\partial f}{\partial x}=2x+3y
$$

$$
\frac{\partial f}{\partial y}=3x+2y
$$

Therefore:

$$
\nabla f=
\begin{bmatrix}
2x+3y\\
3x+2y
\end{bmatrix}
$$

At x = 2 and y = 1:

$$
\boxed{
\nabla f(2,1)=
\begin{bmatrix}
7\\
8
\end{bmatrix}
}
$$

## 16.4 AI/ML Application

Gradient tells a machine learning algorithm how the loss changes with respect to its model parameters.

Gradient Descent uses the negative gradient to reduce the loss.

---

# 17. DIRECTIONAL DERIVATIVE

## 17.1 Definition

A directional derivative measures the rate of change of a function in a particular direction.

Formula:

$$
\boxed{
D_{\hat u}f=\nabla f\cdot\hat u
}
$$

Where:

- ∇f = Gradient.
- û = Unit direction vector.

### Example

Given:

$$
\nabla f=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

Direction vector:

$$
u=
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

This is already a unit vector.

Directional derivative:

$$
D_uf=
\begin{bmatrix}
3 & 4
\end{bmatrix}
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

$$
\boxed{D_uf=3}
$$

---

# 18. JACOBIAN MATRIX

## 18.1 Definition

The Jacobian is a matrix containing the first-order partial derivatives of a vector-valued function.

Suppose:

$$
F(x,y)=
\begin{bmatrix}
f_1(x,y)\\
f_2(x,y)
\end{bmatrix}
$$

Then:

$$
\boxed{
J=
\begin{bmatrix}
\frac{\partial f_1}{\partial x} &
\frac{\partial f_1}{\partial y}\\
\frac{\partial f_2}{\partial x} &
\frac{\partial f_2}{\partial y}
\end{bmatrix}
}
$$

## 18.2 Example

Given:

$$
f_1(x,y)=x^2+y
$$

$$
f_2(x,y)=xy
$$

Calculate partial derivatives:

$$
\frac{\partial f_1}{\partial x}=2x
$$

$$
\frac{\partial f_1}{\partial y}=1
$$

$$
\frac{\partial f_2}{\partial x}=y
$$

$$
\frac{\partial f_2}{\partial y}=x
$$

Therefore:

$$
\boxed{
J=
\begin{bmatrix}
2x & 1\\
y & x
\end{bmatrix}
}
$$

## 18.3 AI/ML Application

- Neural network transformations.
- Backpropagation.
- Coordinate transformations.
- Sensitivity analysis.

---

# 19. HESSIAN MATRIX

## 19.1 Definition

The Hessian is a square matrix containing all second-order partial derivatives of a scalar-valued function.

It is represented by:

$$
H(f)
$$

## 19.2 Formula

For a function f(x,y):

$$
\boxed{
H(f)=
\begin{bmatrix}
\frac{\partial^2 f}{\partial x^2} &
\frac{\partial^2 f}{\partial x\partial y}\\
\frac{\partial^2 f}{\partial y\partial x} &
\frac{\partial^2 f}{\partial y^2}
\end{bmatrix}
}
$$

## 19.3 Example

Given:

$$
f(x,y)=x^2+3xy+y^2
$$

First derivatives:

$$
f_x=2x+3y
$$

$$
f_y=3x+2y
$$

Second derivatives:

$$
f_{xx}=2
$$

$$
f_{xy}=3
$$

$$
f_{yx}=3
$$

$$
f_{yy}=2
$$

Therefore:

$$
\boxed{
H(f)=
\begin{bmatrix}
2 & 3\\
3 & 2
\end{bmatrix}
}
$$

## 19.4 Applications

- Second-order optimization.
- Newton's method.
- Curvature analysis.
- Convexity analysis.

---

# 20. MAXIMA AND MINIMA

## 20.1 Maximum

A maximum is a point where a function reaches a local or global high value.

## 20.2 Minimum

A minimum is a point where a function reaches a local or global low value.

## 20.3 Critical Points

A critical point occurs where the derivative is zero or where the derivative does not exist, provided the point is in the function's domain.

For differentiable functions:

$$
f'(x)=0
$$

## 20.4 First Derivative Test

- If derivative changes from positive to negative, there is a local maximum.
- If derivative changes from negative to positive, there is a local minimum.

## 20.5 Second Derivative Test

At a critical point x = c:

If:

$$
f''(c)>0
$$

Then local minimum.

If:

$$
f''(c)<0
$$

Then local maximum.

If:

$$
f''(c)=0
$$

The test is inconclusive.

### Numerical Example

Find the minimum of:

$$
f(x)=x^2-4x+5
$$

Step 1: First derivative.

$$
f'(x)=2x-4
$$

Step 2: Set derivative equal to zero.

$$
2x-4=0
$$

$$
x=2
$$

Step 3: Second derivative.

$$
f''(x)=2
$$

Since:

$$
f''(2)=2>0
$$

There is a local minimum at x = 2.

Step 4: Calculate minimum value.

$$
f(2)=2^2-4(2)+5
$$

$$
=4-8+5
$$

$$
\boxed{f(2)=1}
$$

Final answer:

Minimum value = 1 at x = 2.

---

# 21. INTEGRATION

## 21.1 What is Integration?

**Definition:** Integration is a mathematical process used to calculate accumulation, total quantities, and areas under curves.

It is the reverse process of differentiation for suitable functions.

It is represented by:

$$
\int f(x)\,dx
$$

In simple words:

Derivative change ki rate batata hai, while integration small changes ko accumulate karke total quantity calculate karta hai.

## 21.2 Types of Integration

1. Indefinite Integration.
2. Definite Integration.

---

# 22. INDEFINITE INTEGRATION

## 22.1 Definition

Indefinite integration finds a family of antiderivatives of a function.

Formula:

$$
\int f(x)\,dx=F(x)+C
$$

Where:

- F(x) = Antiderivative.
- C = Arbitrary constant.

## 22.2 Basic Integration Rules

### Constant Rule

$$
\int c\,dx=cx+C
$$

### Power Rule

For n ≠ -1:

$$
\boxed{
\int x^n\,dx=
\frac{x^{n+1}}{n+1}+C
}
$$

### Example

$$
\int x^3\,dx
$$

Apply power rule:

$$
=\frac{x^{3+1}}{3+1}+C
$$

$$
\boxed{\frac{x^4}{4}+C}
$$

### Constant Multiple Rule

$$
\int cf(x)\,dx
=
c\int f(x)\,dx
$$

### Sum Rule

$$
\int[f(x)+g(x)]dx
=
\int f(x)dx+\int g(x)dx
$$

## 22.3 Integration of Exponential Functions

$$
\int e^x\,dx=e^x+C
$$

For a ≠ 0:

$$
\int e^{ax}\,dx=\frac{e^{ax}}{a}+C
$$

## 22.4 Integration of Trigonometric Functions

$$
\int\sin x\,dx=-\cos x+C
$$

$$
\int\cos x\,dx=\sin x+C
$$

$$
\int\sec^2x\,dx=\tan x+C
$$

$$
\int\csc^2x\,dx=-\cot x+C
$$

---

# 23. DEFINITE INTEGRATION

## 23.1 Definition

Definite integration calculates the accumulated value of a function between two limits.

Formula:

$$
\boxed{
\int_a^b f(x)\,dx=F(b)-F(a)
}
$$

Where F is an antiderivative of f.

## 23.2 Example

Calculate:

$$
\int_0^2 x^2\,dx
$$

Step 1: Integrate.

$$
\int x^2dx=\frac{x^3}{3}
$$

Step 2: Apply limits.

$$
=\left[\frac{x^3}{3}\right]_0^2
$$

Step 3: Substitute upper and lower limits.

$$
=\frac{2^3}{3}-\frac{0^3}{3}
$$

$$
=\frac83-0
$$

Final answer:

$$
\boxed{\frac83}
$$

## 23.3 Geometric Interpretation

A definite integral represents signed area between a function and the x-axis over an interval.

Area above the x-axis contributes positively, while area below it contributes negatively.

---

# 24. METHODS OF INTEGRATION

## 24.1 Substitution Method

Used to simplify an integral by replacing an inner expression with a new variable.

Example:

$$
\int 2x(x^2+1)^3dx
$$

Let:

$$
u=x^2+1
$$

Then:

$$
du=2x\,dx
$$

Substitute:

$$
=\int u^3du
$$

$$
=\frac{u^4}{4}+C
$$

Final answer:

$$
\boxed{
\frac{(x^2+1)^4}{4}+C
}
$$

## 24.2 Integration by Parts

Formula:

$$
\boxed{
\int u\,dv=uv-\int v\,du
}
$$

Example:

$$
\int xe^x\,dx
$$

Choose:

$$
u=x,\quad dv=e^x dx
$$

Then:

$$
du=dx,\quad v=e^x
$$

Apply formula:

$$
=xe^x-\int e^x dx
$$

Final answer:

$$
\boxed{xe^x-e^x+C}
$$

## 24.3 Partial Fractions

Partial fraction decomposition expresses a rational function as a sum of simpler fractions.

Example:

$$
\frac{1}{x(x+1)}
=
\frac1x-\frac1{x+1}
$$

Therefore:

$$
\int\frac{1}{x(x+1)}dx
$$

$$
=\int\left(\frac1x-\frac1{x+1}\right)dx
$$

$$
\boxed{
\ln|x|-\ln|x+1|+C
}
$$

---

# 25. FUNDAMENTAL THEOREM OF CALCULUS

## 25.1 Definition

The Fundamental Theorem of Calculus connects differentiation and integration.

It establishes that differentiation and integration are inverse operations under suitable conditions.

## 25.2 First Part

If:

$$
F(x)=\int_a^x f(t)\,dt
$$

Then:

$$
\boxed{F'(x)=f(x)}
$$

## 25.3 Second Part

If F is an antiderivative of f:

$$
\boxed{
\int_a^b f(x)\,dx=F(b)-F(a)
}
$$

This theorem makes it possible to evaluate definite integrals using antiderivatives.

---

# 26. TAYLOR SERIES

## 26.1 Definition

Taylor Series represents a sufficiently differentiable function as an infinite sum of terms involving derivatives evaluated at a point.

Formula around x = a:

$$
\boxed{
f(x)=
f(a)+f'(a)(x-a)
+\frac{f''(a)}{2!}(x-a)^2
+\cdots
}
$$

General form:

$$
f(x)=
\sum_{n=0}^{\infty}
\frac{f^{(n)}(a)}{n!}(x-a)^n
$$

The equality holds where the Taylor series converges to the function.

## 26.2 Maclaurin Series

Maclaurin Series is a Taylor Series centered at a = 0.

$$
f(x)=
f(0)+f'(0)x+
\frac{f''(0)}{2!}x^2+\cdots
$$

Important expansions:

$$
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots
$$

$$
\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots
$$

$$
\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots
$$

## 26.3 Applications

- Numerical approximation.
- Optimization.
- Mathematical modelling.
- Scientific computing.
- Approximation of activation functions.

---

# 27. GRADIENT DESCENT

## 27.1 Definition

Gradient Descent is an iterative optimization algorithm that updates model parameters in the direction of the negative gradient to reduce a differentiable objective function.

In simple words:

Gradient Descent model ki error ko kam karne ke liye weights ko repeatedly update karta hai.

## 27.2 Formula

$$
\boxed{
\theta_{new}
=
\theta_{old}
-
\alpha\nabla J(\theta)
}
$$

Where:

- θ = Model parameters.
- α = Learning rate.
- ∇J(θ) = Gradient of the loss function.

## 27.3 Numerical Example

Given:

$$
J(w)=(w-3)^2
$$

Step 1: Differentiate.

$$
\frac{dJ}{dw}=2(w-3)
$$

Step 2: Choose initial values.

$$
w=0,\quad\alpha=0.1
$$

Step 3: Calculate gradient.

$$
\frac{dJ}{dw}=2(0-3)
$$

$$
=-6
$$

Step 4: Update weight.

$$
w_{new}=0-0.1(-6)
$$

$$
\boxed{w_{new}=0.6}
$$

The parameter moves closer to the minimum at w = 3.

## 27.4 Python Implementation

```python
# Define learning rate
learning_rate = 0.1

# Initial parameter
w = 0.0

# Number of iterations
epochs = 20

for epoch in range(epochs):

    # Calculate gradient
    gradient = 2 * (w - 3)

    # Update parameter
    w = w - learning_rate * gradient

    # Calculate loss
    loss = (w - 3) ** 2

    print(
        f"Epoch: {epoch + 1}, "
        f"Weight: {w:.4f}, "
        f"Loss: {loss:.4f}"
    )

print("Final Weight:", w)
```

Explanation:

- `learning_rate`: Controls the update size.
- `w`: Initial model parameter.
- `epochs`: Number of update iterations.
- `gradient`: Derivative of the loss function.
- `w = w - learning_rate * gradient`: Updates the parameter.
- `loss`: Calculates the current error.
- `print()`: Displays training progress.

The weight approaches 3 and the loss approaches 0.

---

# 28. TYPES OF GRADIENT DESCENT

## 28.1 Batch Gradient Descent

Uses the complete training dataset to calculate one gradient update.

Advantages:
- Stable gradient estimate.
- Uses all training samples.

Disadvantages:
- Can be computationally expensive for large datasets.

## 28.2 Stochastic Gradient Descent (SGD)

Uses one randomly selected training example per update.

Advantages:
- Frequent updates.
- Useful for large datasets.

Disadvantages:
- Noisy updates.

## 28.3 Mini-Batch Gradient Descent

Uses a small batch of training examples for each update.

Advantages:
- Efficient computation.
- Suitable for GPU processing.
- Commonly used in Deep Learning.

---

# 29. LEARNING RATE

## 29.1 Definition

Learning rate controls how large a parameter update is during optimization.

It is represented by:

$$
\alpha
$$

## 29.2 Effects of Learning Rate

### Very Small Learning Rate

- Training can be slow.
- Requires many iterations.

### Very Large Learning Rate

- May overshoot the minimum.
- Can cause oscillations.
- May fail to converge.

### Appropriate Learning Rate

- Makes useful progress.
- Helps achieve stable convergence.

---

# 30. ACTIVATION FUNCTION DERIVATIVES

Activation functions introduce non-linearity into neural networks.

Their derivatives are important in backpropagation.

## 30.1 Sigmoid

Formula:

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

Derivative:

$$
\boxed{
\sigma'(x)=\sigma(x)(1-\sigma(x))
}
$$

## 30.2 Tanh

Formula:

$$
\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
$$

Derivative:

$$
\boxed{
\tanh'(x)=1-\tanh^2(x)
}
$$

## 30.3 ReLU

Formula:

$$
ReLU(x)=\max(0,x)
$$

Derivative:

$$
ReLU'(x)=
\begin{cases}
0 & x<0\\
1 & x>0
\end{cases}
$$

At x = 0, the ordinary derivative is not defined; implementations choose a subgradient convention, commonly 0.

## 30.4 Softmax

For a vector z:

$$
softmax(z_i)=
\frac{e^{z_i}}{\sum_j e^{z_j}}
$$

It converts a vector of scores into a probability distribution.

The Jacobian entries are:

$$
\frac{\partial s_i}{\partial z_j}
=
s_i(\delta_{ij}-s_j)
$$

Where δᵢⱼ is 1 when i = j and 0 otherwise.

---

# 31. BACKPROPAGATION

## 31.1 Definition

Backpropagation is an algorithm used to calculate gradients of a neural network's loss with respect to its parameters by applying the Chain Rule from the output layer backward through the network.

In simple words:

Neural network prediction karta hai, loss calculate hota hai, phir backpropagation calculate karta hai ki har weight ki wajah se loss kitna change ho raha hai.

## 31.2 Basic Workflow

1. Forward propagation.
2. Calculate predicted output.
3. Calculate loss.
4. Apply Chain Rule backward.
5. Calculate gradients.
6. Update weights using an optimizer.

## 31.3 Simple Mathematical Example

Suppose:

$$
z=wx+b
$$

$$
a=\sigma(z)
$$

Loss:

$$
L=(a-y)^2
$$

Using Chain Rule:

$$
\frac{dL}{dw}
=
\frac{dL}{da}
\cdot
\frac{da}{dz}
\cdot
\frac{dz}{dw}
$$

Calculate each term:

$$
\frac{dL}{da}=2(a-y)
$$

$$
\frac{da}{dz}=\sigma(z)(1-\sigma(z))
$$

$$
\frac{dz}{dw}=x
$$

Therefore:

$$
\boxed{
\frac{dL}{dw}
=
2(a-y)a(1-a)x
}
$$

This is a simplified example using sigmoid activation and squared error loss.

---

# 32. NUMPY AND SYMPY FOR CALCULUS

## 32.1 Using SymPy

SymPy is a Python library for symbolic mathematics.

Installation:

```bash
pip install sympy
```

### Derivative Example

```python
import sympy as sp

x = sp.symbols('x')

f = x**3 + 2*x**2 + 5*x + 1

derivative = sp.diff(f, x)

print(derivative)
```

Output:

```text
3*x**2 + 4*x + 5
```

Explanation:

- `import sympy as sp`: Imports SymPy.
- `symbols('x')`: Defines a symbolic variable.
- `x**3`: Represents x cubed.
- `sp.diff()`: Calculates the derivative.
- `print()`: Displays the symbolic result.

## 32.2 Partial Derivatives Using SymPy

```python
import sympy as sp

x, y = sp.symbols('x y')

f = x**2 + 3*x*y + y**2

df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

print("Partial derivative w.r.t x:", df_dx)
print("Partial derivative w.r.t y:", df_dy)
```

## 32.3 Integration Using SymPy

```python
import sympy as sp

x = sp.symbols('x')

f = x**3 + 2*x

integral = sp.integrate(f, x)

print(integral)
```

Output:

```text
x**4/4 + x**2
```

## 32.4 Definite Integration

```python
import sympy as sp

x = sp.symbols('x')

f = x**2

result = sp.integrate(f, (x, 0, 2))

print(result)
```

Output:

```text
8/3
```

## 32.5 Gradient Using SymPy

```python
import sympy as sp

x, y = sp.symbols('x y')

f = x**2 + 3*x*y + y**2

gradient = [
    sp.diff(f, x),
    sp.diff(f, y)
]

print(gradient)
```

Output:

```text
[2*x + 3*y, 3*x + 2*y]
```

---


