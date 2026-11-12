
# PART 05 — OPTIMIZATION
## Complete Mathematics & Statistics Notes for AI/ML

---

# 1. Introduction to Optimization

### Definition

Optimization is the mathematical process of finding the best possible solution to a problem by maximizing or minimizing an objective function while satisfying given conditions or constraints.

### Easy Explanation (Hinglish)

Optimization ka simple meaning hai kisi problem ka best solution find karna.

Machine Learning mein hum model ki prediction error ko minimum karna chahte hain.

For example:
- Reduce prediction error.
- Minimize training loss.
- Find the best model parameters.
- Improve model accuracy.
- Reduce computational cost.

### Real-Life Examples

| Problem | Optimization Goal |
|---|---|
| Delivery system | Minimize delivery time |
| Business | Maximize profit |
| Machine Learning | Minimize loss |
| Transportation | Minimize fuel cost |
| Neural Network | Find optimal weights |

### Optimization in AI/ML

Suppose a model predicts house prices.

Actual price = ₹50 lakh

Predicted price = ₹60 lakh

Error = ₹10 lakh

Optimization algorithms adjust model parameters to reduce this error.

---

# 2. Important Terms in Optimization

## 2.1 Decision Variables

Variables whose values we want to determine to obtain the best solution.

Example:

$$
f(x)=x^2+4x+4
$$

Here, $x$ is the decision variable.

## 2.2 Objective Function

The function that we want to maximize or minimize.

Example:

$$
\boxed{f(x)=x^2+4x+4}
$$

## 2.3 Constraints

Conditions that must be satisfied by a solution.

Example:

$$
x+y\leq 10
$$

$$
x\geq 0,\quad y\geq 0
$$

## 2.4 Feasible Solution

A solution that satisfies all the constraints.

## 2.5 Optimal Solution

The best feasible solution that gives the minimum or maximum objective-function value.

---

# 3. Types of Optimization

## 3.1 Minimization

Finding the smallest possible value of a function.

Example:

$$
\min f(x)=x^2
$$

The minimum value occurs at:

$$
x=0,\quad f(0)=0
$$

## 3.2 Maximization

Finding the largest possible value of a function.

Example:

$$
\max f(x)=-(x-3)^2+9
$$

The maximum value occurs at:

$$
x=3,\quad f(3)=9
$$

## 3.3 Unconstrained Optimization

Optimization without explicit constraints.

Example:

$$
\min f(x)=x^2+6x+9
$$

## 3.4 Constrained Optimization

Optimization with one or more restrictions.

Example:

$$
\min f(x,y)=x^2+y^2
$$

Subject to:

$$
x+y=10
$$

---

# 4. Local and Global Optimum

## 4.1 Local Minimum

A point where the function has a lower value than nearby points.

## 4.2 Global Minimum

The lowest value of the function over its entire domain.

## 4.3 Local Maximum

A point where the function has a higher value than nearby points.

## 4.4 Global Maximum

The highest value of the function over its entire domain.

### Example

Consider:

$$
f(x)=x^2
$$

Its global minimum is:

$$
x=0,\quad f(x)=0
$$

### Important Difference

| Local Optimum | Global Optimum |
|---|---|
| Best in a nearby region | Best in the entire domain |
| May not be the overall best | Overall best solution |
| Depends on neighborhood | Depends on full search space |

---

# 5. Convex and Non-Convex Functions

## 5.1 Convex Function

A function is convex if the line segment joining any two points on its graph lies on or above the graph.

Mathematical condition:

$$
f(\lambda x+(1-\lambda)y)
\leq
\lambda f(x)+(1-\lambda)f(y)
$$

Where:

$$
0\leq\lambda\leq1
$$

### Example

$$
f(x)=x^2
$$

This is a convex function.

For a twice-differentiable single-variable function, a sufficient condition for convexity on an interval is:

$$
\boxed{f''(x)\geq0}
$$

## 5.2 Concave Function

A function is concave if the line segment joining two points lies on or below its graph.

Condition:

$$
f(\lambda x+(1-\lambda)y)
\geq
\lambda f(x)+(1-\lambda)f(y)
$$

For a twice-differentiable function, a sufficient condition is:

$$
f''(x)\leq0
$$

## 5.3 Non-Convex Function

A function that does not satisfy the convexity condition over its domain.

Example:

$$
f(x)=x^4-4x^2
$$

Non-convex functions can have multiple local minima and maxima.

### Importance in AI/ML

- Convex optimization is generally easier to solve globally.
- Many neural-network loss functions are non-convex.
- Linear regression with squared error is convex in its parameters.
- Training deep neural networks generally involves non-convex optimization.

---

# 6. First-Order and Second-Order Optimization

## 6.1 First-Order Optimization

Uses the first derivative or gradient to update parameters.

Example:

$$
\boxed{x_{new}=x_{old}-\alpha f'(x)}
$$

Gradient Descent is a first-order optimization method.

## 6.2 Second-Order Optimization

Uses second derivatives or the Hessian matrix.

Example:

Newton's Method:

$$
\boxed{x_{new}=x_{old}-\frac{f'(x)}{f''(x)}}
$$

For multiple variables:

$$
\boxed{
\theta_{new}
=
\theta_{old}
-
H^{-1}\nabla f(\theta)
}
$$

Where:

- $H$ = Hessian matrix.
- $\nabla f(\theta)$ = Gradient.
- $H^{-1}$ = Inverse Hessian, when it exists.

### Difference

| First-Order | Second-Order |
|---|---|
| Uses gradient | Uses gradient and Hessian |
| Usually cheaper per iteration | Usually more expensive per iteration |
| Example: Gradient Descent | Example: Newton's Method |
| Does not directly use curvature | Uses curvature information |

---

# 7. Optimization and Loss Functions

A loss function measures how far a model's predictions are from actual values.

The objective of training is generally to minimize the loss.

## 7.1 Mean Squared Error (MSE)

Used mainly for regression problems.

$$
\boxed{
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2
}
$$

Where:

- $y_i$ = Actual value.
- $\hat y_i$ = Predicted value.
- $n$ = Number of observations.

### Numerical Example

Actual values:

$$
y=[10,20,30]
$$

Predicted values:

$$
\hat y=[12,18,33]
$$

Step 1: Calculate errors.

$$
[10-12,\ 20-18,\ 30-33]
$$

$$
[-2,2,-3]
$$

Step 2: Square errors.

$$
[4,4,9]
$$

Step 3: Calculate mean.

$$
MSE=\frac{4+4+9}{3}
$$

$$
\boxed{MSE=5.67}
$$

## 7.2 Mean Absolute Error (MAE)

$$
\boxed{
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat y_i|
}
$$

Using the previous example:

$$
MAE=\frac{2+2+3}{3}
$$

$$
\boxed{MAE=2.33}
$$

## 7.3 Binary Cross-Entropy

Used for binary classification.

$$
\boxed{
L=-\frac{1}{n}\sum_{i=1}^{n}
[y_i\log(p_i)+(1-y_i)\log(1-p_i)]
}
$$

Where:
- $y_i$ = Actual class (0 or 1).
- $p_i$ = Predicted probability of class 1.

## 7.4 Categorical Cross-Entropy

Used for multi-class classification.

$$
\boxed{
L=-\sum_{i=1}^{C}y_i\log(p_i)
}
$$

Where:
- $C$ = Number of classes.
- $y_i$ = Actual class indicator.
- $p_i$ = Predicted probability.

---

# 8. Gradient Descent

### Definition

Gradient Descent is an iterative optimization algorithm that minimizes a function by moving its parameters in the direction opposite to the gradient.

### Easy Explanation

Imagine you are standing on a mountain and want to reach the lowest point.

You look at the slope and move downward step by step.

Gradient Descent does the same thing with a loss function.

### Mathematical Formula

$$
\boxed{
\theta_{new}=\theta_{old}-\alpha\nabla J(\theta)
}
$$

Where:

- $\theta$ = Model parameters.
- $\alpha$ = Learning rate.
- $\nabla J(\theta)$ = Gradient of the loss function.

### Step-by-Step Example

Consider:

$$
f(x)=x^2
$$

Step 1: Differentiate.

$$
f'(x)=2x
$$

Step 2: Choose initial values.

$$
x_0=4,\quad \alpha=0.1
$$

Step 3: Apply Gradient Descent.

$$
x_1=x_0-\alpha f'(x_0)
$$

$$
x_1=4-0.1(8)
$$

$$
\boxed{x_1=3.2}
$$

Step 4: Calculate the next iteration.

$$
x_2=3.2-0.1(6.4)
$$

$$
\boxed{x_2=2.56}
$$

The value gradually moves towards zero.

### Python Implementation

```python
def gradient_descent(x, learning_rate, iterations):

    for i in range(iterations):

        gradient = 2 * x

        x = x - learning_rate * gradient

        print(f"Iteration {i+1}: x = {x:.4f}")

    return x


result = gradient_descent(
    x=4,
    learning_rate=0.1,
    iterations=10
)

print("Final Result:", result)
```

### Code Explanation

- `def gradient_descent(...)`: Defines the optimization function.
- `x`: Initial parameter value.
- `learning_rate`: Controls the size of each update.
- `iterations`: Number of updates.
- `gradient = 2 * x`: Calculates the derivative of $x^2$.
- `x = x - learning_rate * gradient`: Updates the parameter.
- `print()`: Displays each iteration.
- `return x`: Returns the final value.

---

# 9. Types of Gradient Descent

There are three major types of Gradient Descent.

## 9.1 Batch Gradient Descent

Uses the entire training dataset to calculate the gradient for each update.

$$
\boxed{
\theta=\theta-\alpha
\frac{1}{N}\sum_{i=1}^{N}\nabla_\theta L_i
}
$$

Advantages:
- Stable gradient estimate.
- Uses all training examples.

Disadvantages:
- Can be slow for large datasets.
- Requires processing the full dataset per update.

## 9.2 Stochastic Gradient Descent (SGD)

Uses one training example per update.

$$
\boxed{
\theta=\theta-\alpha\nabla_\theta L_i
}
$$

Advantages:
- Frequent updates.
- Useful for large datasets.
- Can escape some shallow local regions due to noisy updates.

Disadvantages:
- Updates can fluctuate.
- Loss may not decrease smoothly.

## 9.3 Mini-Batch Gradient Descent

Uses a small batch of training examples per update.

$$
\boxed{
\theta=\theta-\alpha
\frac{1}{B}\sum_{i=1}^{B}\nabla_\theta L_i
}
$$

Where $B$ is the batch size.

Advantages:
- Efficient computation.
- Works well with GPUs.
- Balances stability and speed.

### Comparison

| Type | Data Used Per Update |
|---|---|
| Batch GD | Entire dataset |
| SGD | One example |
| Mini-Batch GD | Small batch |

Mini-batch Gradient Descent is widely used in deep-learning training.

---

# 10. Learning Rate

### Definition

Learning rate is a hyperparameter that controls how large a step an optimization algorithm takes while updating model parameters.

Formula:

$$
\theta_{new}=\theta_{old}-\alpha\nabla J(\theta)
$$

Here, $\alpha$ is the learning rate.

### Three Cases

**1. Very Small Learning Rate**

- Training may be very slow.
- Requires many iterations.
- May take a long time to converge.

**2. Very Large Learning Rate**

- May overshoot the minimum.
- Can cause unstable updates.
- May fail to converge.

**3. Suitable Learning Rate**

- Makes steady progress.
- Helps the model converge efficiently.

### Example

For:

$$
f(x)=x^2,\quad x=4
$$

Gradient:

$$
f'(x)=8
$$

If learning rate is 0.1:

$$
x_{new}=4-0.1(8)=3.2
$$

If learning rate is 0.5:

$$
x_{new}=4-0.5(8)=0
$$

The best learning rate depends on the function and optimization problem.

---

# 11. Momentum Optimization

### Definition

Momentum is an optimization technique that uses a moving accumulation of past gradients to accelerate learning and reduce oscillations.

### Easy Explanation

Normal Gradient Descent uses the current gradient.

Momentum also considers previous update directions.

### Formula

$$
\boxed{
v_t=\beta v_{t-1}+\nabla J(\theta_t)
}
$$

$$
\boxed{
\theta_{t+1}=\theta_t-\alpha v_t
}
$$

Where:

- $v_t$ = Accumulated gradient.
- $\beta$ = Momentum coefficient.
- $\alpha$ = Learning rate.

### Typical Value

$$
\beta=0.9
$$

### Advantages

- Reduces oscillations.
- Can accelerate convergence.
- Uses information from previous steps.

---

# 12. AdaGrad Optimizer

### Definition

AdaGrad adapts the learning rate separately for each parameter using the accumulated squared gradients.

### Formula

$$
G_t=G_{t-1}+g_t^2
$$

$$
\boxed{
\theta_{t+1}
=
\theta_t-
\frac{\alpha}{\sqrt{G_t}+\epsilon}g_t
}
$$

Where:

- $g_t$ = Current gradient.
- $G_t$ = Accumulated squared gradients.
- $\epsilon$ = Small constant to avoid division by zero.

### Advantages

- Parameter-specific learning rates.
- Useful for sparse features.

### Disadvantage

The accumulated squared gradients keep increasing, which can make the learning rate extremely small.

---

# 13. RMSProp Optimizer

### Definition

RMSProp is an adaptive optimization algorithm that uses an exponentially weighted average of squared gradients.

### Formula

$$
\boxed{
v_t=\beta v_{t-1}+(1-\beta)g_t^2
}
$$

Parameter update:

$$
\boxed{
\theta_{t+1}
=
\theta_t-
\frac{\alpha}{\sqrt{v_t}+\epsilon}g_t
}
$$

### Advantages

- Adapts learning rates.
- Avoids the continuously growing accumulator problem of AdaGrad.
- Useful for many non-stationary optimization problems.

---

# 14. Adam Optimizer

### Definition

Adam (Adaptive Moment Estimation) combines ideas from Momentum and RMSProp.

It maintains estimates of:
1. First moment: Mean of gradients.
2. Second moment: Mean of squared gradients.

### Step 1: First Moment

$$
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
$$

### Step 2: Second Moment

$$
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
$$

### Step 3: Bias Correction

$$
\hat m_t=\frac{m_t}{1-\beta_1^t}
$$

$$
\hat v_t=\frac{v_t}{1-\beta_2^t}
$$

### Step 4: Parameter Update

$$
\boxed{
\theta_{t+1}
=
\theta_t-
\frac{\alpha}{\sqrt{\hat v_t}+\epsilon}\hat m_t
}
$$

### Common Default Values

$$
\alpha=0.001
$$

$$
\beta_1=0.9,\quad \beta_2=0.999
$$

### Advantages

- Adaptive learning rates.
- Uses first and second moment estimates.
- Often works well with little initial tuning.
- Widely used in deep learning.

### Python Example

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Create a simple model
model = nn.Linear(1, 1)

# Define loss function
criterion = nn.MSELoss()

# Create Adam optimizer
optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

# Sample input and target
x = torch.tensor([[2.0]])
y = torch.tensor([[5.0]])

# Forward pass
prediction = model(x)

# Calculate loss
loss = criterion(prediction, y)

# Clear old gradients
optimizer.zero_grad()

# Calculate gradients
loss.backward()

# Update model parameters
optimizer.step()

print("Loss:", loss.item())
```

### Code Explanation

- `torch`: Provides tensor operations.
- `nn.Linear(1, 1)`: Creates a linear layer with one input and one output.
- `nn.MSELoss()`: Defines Mean Squared Error loss.
- `optim.Adam(...)`: Creates the Adam optimizer.
- `model.parameters()`: Gives the trainable model parameters.
- `lr=0.001`: Sets the learning rate.
- `prediction = model(x)`: Performs the forward pass.
- `loss = criterion(...)`: Calculates prediction error.
- `optimizer.zero_grad()`: Clears gradients from the previous update.
- `loss.backward()`: Computes gradients using backpropagation.
- `optimizer.step()`: Updates model parameters.

---

# 15. Comparison of Optimization Algorithms

| Algorithm | Main Idea | Important Feature |
|---|---|---|
| Gradient Descent | Uses gradients | Basic optimization |
| Momentum | Uses past gradients | Faster movement |
| AdaGrad | Accumulates squared gradients | Adaptive learning rate |
| RMSProp | Moving average of squared gradients | Controls learning-rate decay |
| Adam | Combines first and second moments | Adaptive updates |

### Which Optimizer Should You Know?

For AI/ML engineering, understand these in this order:

1. Gradient Descent
2. SGD
3. Mini-Batch Gradient Descent
4. Momentum
5. RMSProp
6. Adam
7. AdaGrad

---

# 16. Newton's Method

### Definition

Newton's Method is a second-order optimization algorithm that uses the first and second derivatives to find a minimum or maximum.

### Formula

$$
\boxed{
x_{new}=x_{old}-\frac{f'(x)}{f''(x)}
}
$$

### Example

Consider:

$$
f(x)=x^2+4x+4
$$

First derivative:

$$
f'(x)=2x+4
$$

Second derivative:

$$
f''(x)=2
$$

Initial value:

$$
x_0=3
$$

Apply Newton's Method:

$$
x_1=3-\frac{2(3)+4}{2}
$$

$$
x_1=3-\frac{10}{2}
$$

$$
\boxed{x_1=-2}
$$

At $x=-2$, the function reaches its minimum.

### Advantages

- Can converge very quickly near a suitable optimum.
- Uses curvature information.

### Disadvantages

- Computing and storing the Hessian can be expensive.
- The Hessian may be singular or poorly conditioned.
- It may not converge to a minimum without suitable safeguards.

---

# 17. Constrained Optimization

### Definition

Constrained optimization finds the best solution while satisfying specified equality or inequality restrictions.

### General Form

$$
\min f(x)
$$

Subject to:

$$
g_i(x)\leq0
$$

$$
h_j(x)=0
$$

### Example

Minimize:

$$
f(x,y)=x^2+y^2
$$

Subject to:

$$
x+y=10
$$

The optimal solution is:

$$
\boxed{x=5,\quad y=5}
$$

Minimum value:

$$
f(5,5)=25+25
$$

$$
\boxed{f_{min}=50}
$$

---

# 18. Lagrange Multipliers

### Definition

Lagrange Multipliers are a mathematical technique for solving constrained optimization problems involving equality constraints.

### Main Formula

Suppose we want to optimize:

$$
f(x,y)
$$

Subject to:

$$
g(x,y)=0
$$

Construct the Lagrangian:

$$
\boxed{
\mathcal{L}(x,y,\lambda)
=
f(x,y)+\lambda g(x,y)
}
$$

Then solve:

$$
\frac{\partial\mathcal L}{\partial x}=0
$$

$$
\frac{\partial\mathcal L}{\partial y}=0
$$

$$
\frac{\partial\mathcal L}{\partial\lambda}=0
$$

### Step-by-Step Example

Minimize:

$$
f(x,y)=x^2+y^2
$$

Subject to:

$$
x+y=10
$$

Step 1: Construct Lagrangian.

$$
\mathcal L=x^2+y^2+\lambda(x+y-10)
$$

Step 2: Partial derivatives.

$$
\frac{\partial\mathcal L}{\partial x}=2x+\lambda=0
$$

$$
\frac{\partial\mathcal L}{\partial y}=2y+\lambda=0
$$

$$
\frac{\partial\mathcal L}{\partial\lambda}=x+y-10=0
$$

Step 3: Compare first two equations.

$$
2x+\lambda=2y+\lambda
$$

$$
x=y
$$

Step 4: Apply the constraint.

$$
x+y=10
$$

$$
2x=10
$$

$$
x=5,\quad y=5
$$

Final answer:

$$
\boxed{x=5,\quad y=5}
$$

---

# 19. KKT Conditions

### Definition

Karush-Kuhn-Tucker (KKT) conditions are necessary optimality conditions for many constrained optimization problems.

They extend Lagrange multiplier methods to inequality constraints.

For a problem:

$$
\min f(x)
$$

Subject to:

$$
g_i(x)\leq0
$$

The Lagrangian is:

$$
\mathcal L(x,\lambda)
=
f(x)+\sum_i\lambda_i g_i(x)
$$

Important KKT conditions:

### 1. Stationarity

$$
\nabla f(x)+\sum_i\lambda_i\nabla g_i(x)=0
$$

### 2. Primal Feasibility

$$
g_i(x)\leq0
$$

### 3. Dual Feasibility

$$
\lambda_i\geq0
$$

### 4. Complementary Slackness

$$
\boxed{\lambda_i g_i(x)=0}
$$

KKT conditions are especially important in constrained optimization, convex optimization and Support Vector Machines (SVMs).

Note: KKT conditions are generally necessary under suitable regularity conditions. For convex problems, they can also provide global optimality conditions.

---

# 20. Regularization in Machine Learning

### Definition

Regularization is a technique used to reduce overfitting by adding a penalty term to the model's loss function.

### Easy Explanation

A model may memorize training data instead of learning general patterns.

Regularization discourages overly complex models and can improve performance on unseen data.

## 20.1 L1 Regularization (Lasso)

Adds the absolute values of model parameters to the loss.

$$
\boxed{
J(\theta)=L(\theta)+\lambda\sum_{j=1}^{m}|\theta_j|
}
$$

Important point:

- Can drive some coefficients exactly to zero.
- Encourages sparse models.
- Can perform feature selection.

## 20.2 L2 Regularization (Ridge)

Adds squared parameter values to the loss.

$$
\boxed{
J(\theta)=L(\theta)+\lambda\sum_{j=1}^{m}\theta_j^2
}
$$

Important point:

- Penalizes large weights.
- Usually shrinks weights towards zero.
- Generally does not make them exactly zero.

## 20.3 Elastic Net

Combines L1 and L2 regularization.

$$
\boxed{
J(\theta)=L(\theta)+
\lambda_1\sum_j|\theta_j|
+
\lambda_2\sum_j\theta_j^2
}
$$

### Comparison

| L1 | L2 |
|---|---|
| Absolute penalty | Squared penalty |
| Can produce zero coefficients | Usually shrinks coefficients |
| Encourages sparsity | Encourages smaller weights |
| Lasso | Ridge |

---

# 21. Overfitting and Underfitting

## 21.1 Overfitting

A model performs very well on training data but poorly on unseen data.

Possible solutions:
- Regularization.
- More training data.
- Data augmentation.
- Early stopping.
- Simpler models.

## 21.2 Underfitting

A model fails to learn the important patterns in the training data.

Possible solutions:
- Use a more suitable model.
- Add useful features.
- Train longer when appropriate.
- Reduce excessive regularization.

### Comparison

| Overfitting | Underfitting |
|---|---|
| Model learns training data too closely | Model fails to learn enough |
| Training error low | Training error high |
| Test error often high | Test error often high |
| High model complexity may contribute | Model may be too simple |

---

# 22. Early Stopping

### Definition

Early Stopping is a regularization technique that stops training when validation performance stops improving.

### Working

1. Train the model.
2. Measure training loss.
3. Measure validation loss.
4. Monitor validation performance.
5. Stop when validation performance no longer improves for a chosen patience period.
6. Restore the best model checkpoint.

### Why Important?

- Prevents unnecessary training.
- Can reduce overfitting.
- Saves computational resources.

---

# 23. Learning Rate Scheduling

### Definition

Learning Rate Scheduling changes the learning rate during training according to a predefined rule or observed training progress.

### Common Types

**1. Step Decay**

Reduces the learning rate after fixed intervals.

**2. Exponential Decay**

$$
\boxed{
\alpha_t=\alpha_0e^{-kt}
}
$$

**3. Cosine Annealing**

Gradually changes the learning rate following a cosine curve.

**4. Reduce on Plateau**

Reduces the learning rate when a monitored metric stops improving.

### Why Use It?

- Larger steps can help early learning.
- Smaller steps can improve fine-tuning.
- Can make training more stable.

---

# 24. Optimization in Linear Regression

Linear Regression predicts a continuous target using a weighted combination of input features.

### Model Equation

$$
\boxed{
\hat y=wx+b
}
$$

Where:
- $w$ = Weight.
- $b$ = Bias.
- $x$ = Input.
- $\hat y$ = Prediction.

### Loss Function

$$
J(w,b)=\frac{1}{n}\sum_{i=1}^{n}
(y_i-(wx_i+b))^2
$$

### Goal

Find the values of $w$ and $b$ that minimize the loss.

$$
\boxed{
(w^*,b^*)=\arg\min_{w,b}J(w,b)
}
$$

### Python Example

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Input data
X = np.array([[1], [2], [3], [4], [5]])

# Target values
y = np.array([2, 4, 6, 8, 10])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Make prediction
prediction = model.predict([[6]])

print("Weight:", model.coef_)
print("Bias:", model.intercept_)
print("Prediction:", prediction)
```

### Explanation

- `numpy`: Used for numerical arrays.
- `LinearRegression`: Imports the linear regression model.
- `X`: Contains input features.
- `y`: Contains actual target values.
- `LinearRegression()`: Creates the model.
- `model.fit(X, y)`: Learns model parameters.
- `model.predict([[6]])`: Predicts the output for input 6.
- `model.coef_`: Displays the learned weight.
- `model.intercept_`: Displays the learned bias.

---

# 25. Optimization in Neural Networks

Neural networks contain trainable parameters called weights and biases.

The goal is to find parameter values that minimize the loss function.

### Main Training Steps

1. Initialize weights and biases.
2. Perform forward propagation.
3. Calculate loss.
4. Perform backpropagation.
5. Calculate gradients.
6. Update parameters using an optimizer.
7. Repeat for multiple batches and epochs.

### Mathematical Objective

$$
\boxed{
\theta^*=\arg\min_\theta J(\theta)
}
$$

Where $\theta$ represents all trainable parameters.

### Connection Between Concepts

- Calculus calculates derivatives.
- Backpropagation calculates gradients.
- Optimization algorithms use gradients.
- Loss functions measure errors.
- Neural networks update weights to reduce loss.

---

# 26. Hyperparameters vs Parameters

## Parameters

Values learned by the model during training.

Examples:
- Weights.
- Biases.

## Hyperparameters

Values selected before or during training configuration.

Examples:
- Learning rate.
- Batch size.
- Number of epochs.
- Momentum coefficient.
- Regularization strength.

### Comparison

| Parameters | Hyperparameters |
|---|---|
| Learned from training data | Set by user or tuning process |
| Weights and biases | Learning rate and batch size |
| Updated during training | Control training/model configuration |

---

# 27. Hyperparameter Tuning

### Definition

Hyperparameter tuning is the process of finding suitable hyperparameter values to improve model performance.

### Common Methods

## 27.1 Grid Search

Tests every combination in a predefined parameter grid.

Advantages:
- Systematic.
- Easy to understand.

Disadvantages:
- Expensive when many parameters are involved.

## 27.2 Random Search

Tests randomly selected combinations.

Advantages:
- Can be more efficient than grid search.
- Useful for large search spaces.

## 27.3 Bayesian Optimization

Uses information from previous evaluations to select promising configurations.

Advantages:
- Can reduce the number of expensive evaluations.
- Useful for costly model training.

### Python Example

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Create model
model = RandomForestClassifier(random_state=42)

# Define parameter grid
params = {
    "n_estimators": [50, 100],
    "max_depth": [3, 5, None]
}

# Perform grid search
search = GridSearchCV(
    model,
    params,
    cv=5,
    scoring="accuracy"
)

# Train and search
search.fit(X_train, y_train)

print("Best Parameters:", search.best_params_)
print("Best Score:", search.best_score_)
```

Note: `X_train` and `y_train` must be defined before running this example.

---

# 28. Important Mathematical Formulas

| Concept | Formula |
|---|---|
| Gradient Descent | $\theta_{new}=\theta-\alpha\nabla J(\theta)$ |
| Newton's Method | $x_{new}=x-\frac{f'(x)}{f''(x)}$ |
| MSE | $\frac{1}{n}\sum(y_i-\hat y_i)^2$ |
| MAE | $\frac{1}{n}\sum|y_i-\hat y_i|$ |
| L1 Regularization | $L+\lambda\sum|\theta_j|$ |
| L2 Regularization | $L+\lambda\sum\theta_j^2$ |
| Momentum | $v_t=\beta v_{t-1}+g_t$ |
| Adam First Moment | $m_t=\beta_1m_{t-1}+(1-\beta_1)g_t$ |
| Adam Second Moment | $v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2$ |
| Convexity Condition | $f''(x)\geq0$ |

---

# 29. Important Python Libraries for Optimization

| Library | Purpose |
|---|---|
| NumPy | Numerical calculations |
| SciPy | Scientific and numerical optimization |
| Scikit-learn | ML models and optimization tools |
| PyTorch | Deep-learning optimization |
| TensorFlow | Deep-learning optimization |
| CVXPY | Convex optimization modeling |
| Optuna | Hyperparameter optimization |

### SciPy Example

```python
from scipy.optimize import minimize

# Define objective function
def objective(x):
    return x[0]**2 + x[1]**2

# Initial values
initial = [5, 8]

# Minimize function
result = minimize(objective, initial)

print("Optimal Values:", result.x)
print("Minimum Value:", result.fun)
```

### Explanation

- `minimize`: Finds a minimum of an objective function.
- `objective(x)`: Defines the function to minimize.
- `initial`: Provides the starting point.
- `minimize(objective, initial)`: Runs the optimization procedure.
- `result.x`: Returns the estimated optimal variables.
- `result.fun`: Returns the objective value at the solution.

---

# 30. AI/ML Applications of Optimization

Optimization is used in:

1. Linear Regression — minimizing squared error.
2. Logistic Regression — minimizing cross-entropy loss.
3. Neural Networks — updating weights and biases.
4. Deep Learning — training complex architectures.
5. Support Vector Machines — finding a maximum-margin classifier.
6. Recommendation Systems — learning user and item parameters.
7. Computer Vision — optimizing model parameters.
8. Natural Language Processing — training language models.
9. Reinforcement Learning — optimizing policy or value objectives.
10. Feature Selection — choosing useful features.

---



