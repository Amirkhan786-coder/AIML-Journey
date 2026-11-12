# 27. INTERVIEW QUESTIONS AND ANSWERS

## Q1. What is probability?

Probability measures the likelihood of an event occurring.

## Q2. What is sample space?

The set of all possible outcomes of an experiment.

## Q3. What is an event?

An event is a subset of the sample space.

## Q4. What is the difference between independent and dependent events?

Independent events do not affect each other's probabilities, while dependent events do.

## Q5. What is conditional probability?

It is the probability of an event given that another event has occurred.

## Q6. What is Bayes' theorem?

A theorem used to update the probability of an event using new evidence.

## Q7. What is a random variable?

A variable that assigns numerical values to outcomes of a random experiment.

## Q8. Difference between PMF and PDF?

PMF describes probabilities for discrete variables, while PDF describes probability density for continuous variables.

## Q9. What is expected value?

The theoretical long-run average of a random variable.

## Q10. What is variance?

Variance measures the spread of values around the mean.

## Q11. What is the Central Limit Theorem?

It states that under suitable conditions, the sampling distribution of the sample mean approaches a normal distribution as sample size increases.

## Q12. What is the Law of Large Numbers?

It states that the sample average tends to approach the expected value as the number of independent trials increases.

## Q13. What is a normal distribution?

A symmetric, bell-shaped continuous probability distribution.

## Q14. What is a binomial distribution?

A distribution that models the number of successes in a fixed number of independent trials with constant success probability.

## Q15. Why is probability important in Machine Learning?

It helps models handle uncertainty, estimate class probabilities, make predictions, and model random processes.

---

# 28. PRACTICE QUESTIONS WITH SOLUTIONS

## Beginner Level

### Q1. A fair coin is tossed once. Find the probability of getting Head.

Solution:

$$
P(H)=\frac12=0.5
$$

### Q2. A dice is rolled. Find the probability of getting an even number.

Solution:

$$
P(E)=\frac36=\frac12
$$

### Q3. Find the probability of not getting 6 on a dice.

Solution:

$$
P(\text{Not 6})=1-\frac16
$$

$$
=\frac56
$$

### Q4. A card is selected from 52 cards. Find the probability of getting an Ace.

Solution:

$$
P(A)=\frac4{52}=\frac1{13}
$$

### Q5. Find 5 factorial.

Solution:

$$
5!=5\times4\times3\times2\times1=120
$$

## Intermediate Level

### Q6. Two coins are tossed. Find the probability of getting exactly one Head.

Sample space:

$$
S=\{HH,HT,TH,TT\}
$$

Favourable outcomes:

$$
A=\{HT,TH\}
$$

Answer:

$$
P(A)=\frac24=\frac12
$$

### Q7. A bag contains 4 red and 6 blue balls. Find the probability of selecting a red ball.

$$
P(R)=\frac4{10}=0.4
$$

### Q8. Two red balls are selected without replacement from 5 red and 3 blue balls. Find the probability.

$$
P(R_1\cap R_2)=\frac58\times\frac47
$$

$$
\boxed{\frac5{14}}
$$

### Q9. If P(A) = 0.6, find P(A').

$$
P(A')=1-0.6
$$

$$
\boxed{0.4}
$$

### Q10. A student has a 70% probability of passing Mathematics and a 60% probability of passing Statistics. Assuming independence, find the probability of passing both.

$$
P(A\cap B)=0.7\times0.6
$$

$$
\boxed{0.42}
$$

## Advanced Level

### Q11. A test has 90% sensitivity and 95% specificity. Disease prevalence is 1%. Find the probability of disease given a positive test.

Answer using Bayes' theorem:

$$
P(D|+)=\frac{0.90(0.01)}
{0.90(0.01)+0.05(0.99)}
$$

$$
\boxed{15.38\%}
$$

### Q12. A coin is tossed 4 times. Find the probability of exactly 2 Heads.

$$
P(X=2)=\binom42(0.5)^2(0.5)^2
$$

$$
=6\times0.0625
$$

$$
\boxed{0.375}
$$

### Q13. A website receives an average of 3 requests per minute. Find the probability of exactly 2 requests in one minute.

$$
P(X=2)=\frac{e^{-3}3^2}{2!}
$$

$$
\boxed{P(X=2)\approx0.2240}
$$

### Q14. Find the Z-score if X = 85, mean = 70 and standard deviation = 5.

$$
Z=\frac{85-70}{5}
$$

$$
\boxed{Z=3}
$$

### Q15. A random variable has values 1, 2, 3 with probabilities 0.2, 0.5, 0.3. Find its expected value.

$$
E(X)=1(0.2)+2(0.5)+3(0.3)
$$

$$
\boxed{E(X)=2.1}
$$

---

# 29. MULTIPLE CHOICE QUESTIONS (MCQs)

### Q1. Probability always lies between:

A. -1 and 1  
B. 0 and 1  
C. 1 and 10  
D. -10 and 10  

**Answer: B**

### Q2. Probability of an impossible event is:

A. 1  
B. 0.5  
C. 0  
D. 2  

**Answer: C**

### Q3. Probability of a certain event is:

A. 0  
B. 0.5  
C. 1  
D. -1  

**Answer: C**

### Q4. Bayes' theorem is used to:

A. Sort data  
B. Update probability using evidence  
C. Calculate mean only  
D. Find matrix inverse  

**Answer: B**

### Q5. Which distribution is used for the number of successes in n independent trials?

A. Normal  
B. Binomial  
C. Exponential  
D. Uniform  

**Answer: B**

### Q6. Which distribution is commonly used for event counts in a fixed interval?

A. Poisson  
B. Normal  
C. Uniform  
D. t-distribution  

**Answer: A**

### Q7. A random variable with countable outcomes is:

A. Continuous  
B. Discrete  
C. Constant  
D. None  

**Answer: B**

### Q8. Which function calculates a cumulative probability?

A. PMF  
B. PDF  
C. CDF  
D. Variance  

**Answer: C**

### Q9. The standard normal distribution has:

A. Mean 1, SD 0  
B. Mean 0, SD 1  
C. Mean 1, SD 1  
D. Mean 0, SD 0  

**Answer: B**

### Q10. The expected value of a fair six-sided dice roll is:

A. 2  
B. 3  
C. 3.5  
D. 6  

**Answer: C**

---
