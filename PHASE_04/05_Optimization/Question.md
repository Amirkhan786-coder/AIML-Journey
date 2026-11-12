# 1. Interview Questions and Answers

### Q1. What is optimization?

Optimization is the process of finding the best solution by maximizing or minimizing an objective function.

### Q2. What is an objective function?

It is a mathematical function representing the quantity we want to minimize or maximize.

### Q3. What is Gradient Descent?

It is an iterative algorithm that updates parameters in the opposite direction of the gradient to minimize a function.

### Q4. What is a learning rate?

It controls the step size of parameter updates.

### Q5. What happens if the learning rate is too high?

Training may become unstable or fail to converge.

### Q6. What is a convex function?

A function satisfying the convexity inequality over its domain.

### Q7. What is a non-convex function?

A function that is not convex over its domain.

### Q8. What is SGD?

Stochastic Gradient Descent updates parameters using one training example at a time.

### Q9. What is Mini-Batch Gradient Descent?

It updates parameters using a small group of training examples.

### Q10. What is Momentum?

It uses accumulated past gradients to influence the current update.

### Q11. What is Adam?

Adam is an adaptive optimization algorithm that combines first- and second-moment estimates of gradients.

### Q12. What is Regularization?

A technique that adds a penalty to the loss to discourage excessive model complexity.

### Q13. What is L1 regularization?

A penalty based on the absolute values of model coefficients.

### Q14. What is L2 regularization?

A penalty based on the squared values of model coefficients.

### Q15. What is Newton's Method?

A second-order optimization method that uses first and second derivatives.

### Q16. What are Lagrange multipliers?

A method for finding extrema subject to equality constraints.

### Q17. What are KKT conditions?

Optimality conditions used in constrained optimization, including inequality constraints.

### Q18. What is hyperparameter tuning?

Finding suitable configuration values to improve model performance.

### Q19. What is early stopping?

Stopping training when validation performance stops improving according to a chosen rule.

### Q20. Why is optimization important in AI/ML?

It helps models learn suitable parameters by minimizing loss or maximizing a target objective.

---

# 2. Practice Questions

## Beginner Level

1. Define optimization.
2. What is an objective function?
3. Differentiate between minimization and maximization.
4. What is a feasible solution?
5. Define Gradient Descent.
6. What is a learning rate?
7. What is a convex function?
8. Define loss function.
9. What is regularization?
10. Differentiate between parameters and hyperparameters.

## Intermediate Level

11. Explain Batch Gradient Descent.
12. Explain Stochastic Gradient Descent.
13. Explain Mini-Batch Gradient Descent.
14. Compare Momentum and Adam.
15. Explain L1 and L2 regularization.
16. What is Newton's Method?
17. Explain Lagrange multipliers.
18. What is early stopping?
19. Explain learning rate scheduling.
20. Explain hyperparameter tuning.

## Advanced Level

21. Explain the KKT conditions.
22. Explain convex and non-convex optimization.
23. Why is deep-learning optimization non-convex?
24. Explain Adam bias correction.
25. Compare first-order and second-order optimization.
26. Explain the role of optimization in backpropagation.
27. Explain constrained optimization with an example.
28. Explain Bayesian optimization.
29. What is the relationship between Hessian and optimization?
30. Explain why regularization can improve generalization.

---

# 3. MCQs

### Q1. What is the primary goal of optimization in ML?

A. Increase file size  
B. Minimize or maximize an objective  
C. Delete training data  
D. Increase memory usage  

**Answer: B**

### Q2. Which algorithm uses gradients?

A. Gradient Descent  
B. Sorting  
C. Searching  
D. Hashing  

**Answer: A**

### Q3. Which optimizer combines first and second moment estimates?

A. SGD  
B. Adam  
C. Linear Regression  
D. KNN  

**Answer: B**

### Q4. Which method uses one example per update?

A. Batch GD  
B. SGD  
C. Mini-Batch GD  
D. Grid Search  

**Answer: B**

### Q5. Which regularization can produce zero coefficients?

A. L1  
B. L2  
C. Neither  
D. Both always  

**Answer: A**

### Q6. Which method uses second derivatives?

A. Basic SGD  
B. Newton's Method  
C. Random Search  
D. Grid Search  

**Answer: B**

### Q7. What does a learning rate control?

A. Dataset size  
B. Update step size  
C. Number of features  
D. Number of classes  

**Answer: B**

### Q8. Which optimizer uses an exponentially weighted average of squared gradients?

A. RMSProp  
B. Basic Batch GD  
C. Linear Regression  
D. KNN  

**Answer: A**

### Q9. What is overfitting?

A. Model learns too little  
B. Model memorizes training patterns and generalizes poorly  
C. Model has no parameters  
D. Model has no loss  

**Answer: B**

### Q10. Which method is used for equality-constrained optimization?

A. Lagrange Multipliers  
B. Sorting  
C. PCA  
D. KNN  

**Answer: A**

### Q11. Which algorithm searches a predefined parameter grid?

A. Random Search  
B. Grid Search  
C. SGD  
D. Momentum  

**Answer: B**

### Q12. What does early stopping monitor?

A. File size  
B. Validation performance  
C. CPU brand  
D. Dataset filename  

**Answer: B**

### Q13. What is a feasible solution?

A. A solution satisfying constraints  
B. Any random solution  
C. An invalid solution  
D. A solution with maximum error  

**Answer: A**

### Q14. Which loss is commonly used for regression?

A. Mean Squared Error  
B. Accuracy  
C. Confusion Matrix  
D. Precision  

**Answer: A**

### Q15. What is the main purpose of regularization?

A. Increase overfitting  
B. Reduce overfitting  
C. Delete labels  
D. Increase the number of classes  

**Answer: B**

---