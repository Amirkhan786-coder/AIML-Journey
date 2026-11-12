
# PHASE 04 — MATHEMATICS & STATISTICS
# PART 02 — PROBABILITY

---

# 1. INTRODUCTION TO PROBABILITY

## 1.1 What is Probability?

**Definition:** Probability is a branch of mathematics that measures the likelihood or chance of an event occurring.

In simple words:

Probability batati hai ki koi event hone ke kitne chances hain.

Examples:
- Coin toss karne par Head aane ka chance.
- Dice roll karne par 6 aane ka chance.
- Student ke exam pass hone ki probability.
- Machine Learning model ke prediction ki probability.

### Probability Range

Probability ki value hamesha 0 aur 1 ke beech hoti hai.

$$
0 \leq P(A) \leq 1
$$

Where:

- 0 = Impossible event
- 1 = Certain event
- 0.5 = Equal chance

### Example

Agar ek fair coin toss kiya:

$$
P(Head)=\frac{1}{2}=0.5
$$

$$
P(Tail)=\frac{1}{2}=0.5
$$

---

# 2. BASIC TERMINOLOGY

## 2.1 Experiment

An experiment is an action or process that produces an outcome.

Examples:
- Tossing a coin.
- Rolling a dice.
- Selecting a card.
- Testing an ML model.

## 2.2 Outcome

An outcome is a possible result of an experiment.

Example:

Dice roll karne par possible outcomes:

$$
S=\{1,2,3,4,5,6\}
$$

## 2.3 Sample Space

**Definition:** Sample space is the set of all possible outcomes of an experiment.

It is represented by S.

Example 1: Coin toss

$$
S=\{H,T\}
$$

Example 2: Dice roll

$$
S=\{1,2,3,4,5,6\}
$$

## 2.4 Event

**Definition:** An event is a subset of the sample space that contains one or more outcomes.

Example:

Dice roll mein even number aana:

$$
A=\{2,4,6\}
$$

## 2.5 Favourable Outcomes

Favourable outcomes are the outcomes that satisfy a given event.

Example:

Dice roll mein 4 se greater number:

$$
A=\{5,6\}
$$

Favourable outcomes = 2

Total outcomes = 6

---

# 3. CLASSICAL PROBABILITY

## 3.1 Formula

When all outcomes are equally likely:

$$
P(A)=\frac{\text{Favourable Outcomes}}{\text{Total Outcomes}}
$$

### Example 1: Rolling a Dice

Question: What is the probability of getting 4?

Solution:

Total outcomes:

$$
S=\{1,2,3,4,5,6\}
$$

Favourable outcome:

$$
A=\{4\}
$$

Therefore:

$$
P(A)=\frac{1}{6}
$$

### Example 2: Getting an Even Number

Favourable outcomes:

$$
A=\{2,4,6\}
$$

$$
P(A)=\frac{3}{6}=\frac{1}{2}
$$

### Example 3: Getting a Number Greater Than 4

Favourable outcomes:

$$
A=\{5,6\}
$$

$$
P(A)=\frac{2}{6}=\frac{1}{3}
$$

---

# 4. TYPES OF PROBABILITY

## 4.1 Theoretical Probability

Probability calculated using mathematical rules and assumptions.

Example:

Fair coin toss:

$$
P(H)=\frac{1}{2}
$$

## 4.2 Experimental Probability

Probability calculated using actual observations or experiments.

Formula:

$$
P(A)=\frac{\text{Number of times A occurs}}{\text{Total number of trials}}
$$

Example:

A coin is tossed 100 times and Head appears 55 times.

$$
P(H)=\frac{55}{100}=0.55
$$

## 4.3 Subjective Probability

Probability based on personal judgement, experience, or available information.

Example:

A weather expert estimates a 70% chance of rain.

## 4.4 Axiomatic Probability

Probability defined using mathematical axioms.

Three basic axioms:

1. Non-negativity:

$$
P(A)\geq 0
$$

2. Normalization:

$$
P(S)=1
$$

3. Additivity for mutually exclusive events:

$$
P(A\cup B)=P(A)+P(B)
$$

---

# 5. TYPES OF EVENTS

## 5.1 Simple Event

An event containing only one outcome.

Example:

Getting 3 on a dice.

$$
A=\{3\}
$$

## 5.2 Compound Event

An event containing multiple outcomes.

Example:

Getting an even number.

$$
A=\{2,4,6\}
$$

## 5.3 Certain Event

An event that always occurs.

$$
P(S)=1
$$

Example: Getting a number between 1 and 6 when rolling a standard dice.

## 5.4 Impossible Event

An event that can never occur.

$$
P(\emptyset)=0
$$

Example: Getting 8 on a standard six-sided dice.

## 5.5 Mutually Exclusive Events

Two events are mutually exclusive if they cannot occur together in the same trial.

$$
P(A\cap B)=0
$$

Example:

In one dice roll:
- A = Getting an odd number.
- B = Getting an even number.

Both cannot occur simultaneously.

## 5.6 Exhaustive Events

A collection of events is exhaustive if together they cover the entire sample space.

$$
P(A_1\cup A_2\cup \cdots \cup A_n)=1
$$

Example:

For a coin toss, Head and Tail are exhaustive outcomes.

## 5.7 Equally Likely Events

Events having the same probability of occurrence.

Example:

For a fair coin:

$$
P(H)=P(T)=0.5
$$

---

# 6. COMPLEMENTARY PROBABILITY

## 6.1 Meaning

The complement of an event means that the event does not occur.

If A is an event, its complement is represented by A'.

Formula:

$$
P(A')=1-P(A)
$$

Also:

$$
P(A)+P(A')=1
$$

### Example

Probability of passing an exam is 0.8.

Find the probability of failing.

$$
P(\text{Fail})=1-0.8
$$

$$
\boxed{P(\text{Fail})=0.2}
$$

### AI/ML Application

A classification model predicts:
- Probability of spam = 0.9
- Probability of not spam = 0.1

$$
P(\text{Not Spam})=1-P(\text{Spam})
$$

---

# 7. ADDITION RULE OF PROBABILITY

## 7.1 General Addition Rule

The probability of A or B occurring:

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$

Where:
- P(A) = Probability of A.
- P(B) = Probability of B.
- P(A ∩ B) = Probability of both A and B.

### Example

A card is selected from a standard 52-card deck.

Find the probability of getting a King or a Heart.

Let:

A = Getting a King.

B = Getting a Heart.

$$
P(A)=\frac{4}{52}
$$

$$
P(B)=\frac{13}{52}
$$

There is one King of Hearts:

$$
P(A\cap B)=\frac{1}{52}
$$

Apply the formula:

$$
P(A\cup B)=\frac{4}{52}+\frac{13}{52}-\frac{1}{52}
$$

$$
=\frac{16}{52}
$$

$$
\boxed{P(A\cup B)=\frac{4}{13}}
$$

## 7.2 Addition Rule for Mutually Exclusive Events

If A and B cannot occur together:

$$
P(A\cup B)=P(A)+P(B)
$$

Example:

Getting 2 or 5 on a dice:

$$
P(A\cup B)=\frac{1}{6}+\frac{1}{6}
$$

$$
=\frac{2}{6}=\frac{1}{3}
$$

---

# 8. MULTIPLICATION RULE OF PROBABILITY

## 8.1 General Multiplication Rule

The probability of both A and B occurring:

$$
P(A\cap B)=P(A)\times P(B|A)
$$

Where P(B|A) means the probability of B occurring given that A has occurred.

### Example

A bag contains:
- 3 red balls.
- 2 blue balls.

Two balls are selected without replacement.

Find the probability that both balls are red.

First draw:

$$
P(R_1)=\frac{3}{5}
$$

After selecting one red ball:

$$
P(R_2|R_1)=\frac{2}{4}
$$

Therefore:

$$
P(R_1\cap R_2)=\frac{3}{5}\times\frac{2}{4}
$$

$$
\boxed{P(R_1\cap R_2)=\frac{3}{10}}
$$

---

# 9. INDEPENDENT AND DEPENDENT EVENTS

## 9.1 Independent Events

Two events are independent if the occurrence of one event does not affect the probability of the other.

Formula:

$$
P(A\cap B)=P(A)\times P(B)
$$

Example:

Tossing a coin twice.

First toss Head and second toss Head:

$$
P(H_1\cap H_2)=\frac{1}{2}\times\frac{1}{2}
$$

$$
=\frac{1}{4}
$$

## 9.2 Dependent Events

Two events are dependent if the occurrence of one event changes the probability of the other.

Formula:

$$
P(A\cap B)=P(A)\times P(B|A)
$$

Example:

Selecting two cards without replacement.

First card select karne ke baad total cards aur composition change ho jaate hain.

## 9.3 Difference

| Independent | Dependent |
|---|---|
| One event does not affect another | One event affects another |
| Probability remains unchanged | Probability may change |
| Example: Separate coin tosses | Example: Cards without replacement |

---

# 10. CONDITIONAL PROBABILITY

## 10.1 Definition

Conditional probability is the probability of an event occurring given that another event has already occurred.

It is represented by:

$$
P(A|B)
$$

Read as: Probability of A given B.

## 10.2 Formula

$$
P(A|B)=\frac{P(A\cap B)}{P(B)}
$$

Condition:

$$
P(B)>0
$$

### Example

In a class:
- 20 students know Python.
- 10 students know both Python and SQL.
- 30 students know SQL.

Find the probability that a student knows Python given that the student knows SQL.

Let:
- A = Knows Python.
- B = Knows SQL.

$$
P(A|B)=\frac{P(A\cap B)}{P(B)}
$$

Using counts:

$$
P(A|B)=\frac{10}{30}
$$

$$
\boxed{P(A|B)=\frac{1}{3}}
$$

### AI/ML Application

Conditional probability is used in:
- Spam detection.
- Medical diagnosis.
- Recommendation systems.
- Naive Bayes classification.
- Risk prediction.

---

# 11. BAYES' THEOREM

## 11.1 Definition

Bayes' Theorem is a mathematical rule used to update the probability of an event when new evidence becomes available.

Simple explanation:

Pehle available information se probability calculate karte hain. Jab new evidence milta hai, toh probability ko update karte hain.

## 11.2 Formula

$$
P(A|B)=\frac{P(B|A)\times P(A)}{P(B)}
$$

Where:

- P(A|B) = Posterior probability.
- P(B|A) = Likelihood.
- P(A) = Prior probability.
- P(B) = Evidence.

## 11.3 Numerical Example

A disease affects 1% of people.

A medical test has:
- 90% sensitivity.
- 95% specificity.

Find the probability that a person actually has the disease given that the test is positive.

### Step 1: Given Information

$$
P(D)=0.01
$$

$$
P(\neg D)=0.99
$$

Sensitivity:

$$
P(+|D)=0.90
$$

Specificity:

$$
P(-|\neg D)=0.95
$$

False positive rate:

$$
P(+|\neg D)=1-0.95=0.05
$$

### Step 2: Total Probability of Positive Test

$$
P(+)=P(+|D)P(D)+P(+|\neg D)P(\neg D)
$$

Substitute:

$$
P(+)=(0.90)(0.01)+(0.05)(0.99)
$$

$$
=0.009+0.0495
$$

$$
P(+)=0.0585
$$

### Step 3: Apply Bayes' Theorem

$$
P(D|+)=\frac{P(+|D)P(D)}{P(+)}
$$

$$
=\frac{0.90\times0.01}{0.0585}
$$

$$
\boxed{P(D|+)\approx0.1538}
$$

Final answer:

$$
\boxed{P(D|+)\approx15.38\%}
$$

Important: Positive test ka matlab automatically disease hona nahi hai. Actual probability base rate aur test accuracy dono par depend karti hai.

## 11.4 AI/ML Applications of Bayes' Theorem

- Naive Bayes Classifier.
- Email spam filtering.
- Text classification.
- Medical diagnosis.
- Fraud detection.
- Sentiment analysis.

---

# 12. TOTAL PROBABILITY THEOREM

## 12.1 Definition

The law of total probability calculates the probability of an event by considering all possible mutually exclusive and exhaustive cases.

## 12.2 Formula

If B1, B2, ..., Bn form a partition of the sample space:

$$
P(A)=\sum_{i=1}^{n}P(A|B_i)P(B_i)
$$

For two events:

$$
P(A)=P(A|B)P(B)+P(A|B')P(B')
$$

### Example

A factory has two machines:

- Machine A produces 60% of products.
- Machine B produces 40% of products.
- A has a 2% defect rate.
- B has a 5% defect rate.

Find the probability that a randomly selected product is defective.

Given:

$$
P(A)=0.60,\quad P(B)=0.40
$$

$$
P(D|A)=0.02
$$

$$
P(D|B)=0.05
$$

Apply total probability:

$$
P(D)=P(D|A)P(A)+P(D|B)P(B)
$$

$$
=(0.02)(0.60)+(0.05)(0.40)
$$

$$
=0.012+0.020
$$

$$
\boxed{P(D)=0.032=3.2\%}
$$

---

# 13. PERMUTATION AND COMBINATION

These concepts are used to count possible arrangements and selections.

## 13.1 Factorial

Factorial is the product of all positive integers from 1 to n.

Symbol:

$$
n!
$$

Formula:

$$
n!=n\times(n-1)\times\cdots\times1
$$

Example:

$$
5!=5\times4\times3\times2\times1
$$

$$
5!=120
$$

Special case:

$$
0!=1
$$

## 13.2 Permutation

Permutation means arranging objects where order matters.

Formula:

$$
{}^nP_r=\frac{n!}{(n-r)!}
$$

Example:

How many ways can 3 students be arranged from 5 students?

$$
{}^5P_3=\frac{5!}{(5-3)!}
$$

$$
=\frac{120}{2}
$$

$$
\boxed{60}
$$

## 13.3 Combination

Combination means selecting objects where order does not matter.

Formula:

$$
{}^nC_r=\frac{n!}{r!(n-r)!}
$$

Example:

How many ways can 3 students be selected from 5 students?

$$
{}^5C_3=\frac{5!}{3!2!}
$$

$$
=\frac{120}{6\times2}
$$

$$
\boxed{10}
$$

## 13.4 Permutation vs Combination

| Permutation | Combination |
|---|---|
| Order matters | Order does not matter |
| Arrangement | Selection |
| nPr | nCr |
| ABC and BAC are different | ABC and BAC represent the same selection |

---

# 14. RANDOM VARIABLES

## 14.1 Definition

A random variable is a variable that assigns a numerical value to each outcome of a random experiment.

It is generally represented by X.

Example:

Tossing two coins.

Sample space:

$$
S=\{HH,HT,TH,TT\}
$$

Let X = Number of Heads.

| Outcome | X |
|---|---:|
| HH | 2 |
| HT | 1 |
| TH | 1 |
| TT | 0 |

Possible values:

$$
X=\{0,1,2\}
$$

## 14.2 Types of Random Variables

### A. Discrete Random Variable

A random variable that takes countable values.

Examples:
- Number of students.
- Number of heads.
- Number of defective products.

### B. Continuous Random Variable

A random variable that can take any value within an interval.

Examples:
- Height.
- Weight.
- Temperature.
- Time.

---

# 15. PROBABILITY DISTRIBUTION

## 15.1 Definition

A probability distribution describes how probabilities are assigned to the possible values of a random variable.

For a discrete random variable:

$$
P(X=x)
$$

Two important properties:

$$
P(X=x)\geq0
$$

$$
\sum_x P(X=x)=1
$$

## 15.2 Probability Mass Function (PMF)

PMF gives the probability of each possible value of a discrete random variable.

$$
P(X=x)=p(x)
$$

Example: Tossing a fair coin twice.

| X = Number of Heads | Probability |
|---|---:|
| 0 | 1/4 |
| 1 | 2/4 |
| 2 | 1/4 |

Total:

$$
\frac14+\frac24+\frac14=1
$$

## 15.3 Probability Density Function (PDF)

PDF describes the probability density of a continuous random variable.

For a continuous variable:

$$
P(a\leq X\leq b)=\int_a^b f(x)\,dx
$$

Properties:

$$
f(x)\geq0
$$

$$
\int_{-\infty}^{\infty}f(x)\,dx=1
$$

Important:

For a continuous random variable:

$$
P(X=a)=0
$$

Probability is calculated over an interval, not at one exact point.

## 15.4 Cumulative Distribution Function (CDF)

CDF gives the probability that a random variable is less than or equal to a particular value.

Formula:

$$
F(x)=P(X\leq x)
$$

For a continuous random variable:

$$
F(x)=\int_{-\infty}^{x}f(t)\,dt
$$

---

# 16. EXPECTED VALUE

## 16.1 Definition

Expected value is the long-run average value of a random variable over many repetitions of an experiment.

It is also called mathematical expectation.

## 16.2 Discrete Formula

$$
E(X)=\sum_x xP(X=x)
$$

### Example

A random variable X has:

| X | Probability |
|---|---:|
| 1 | 0.2 |
| 2 | 0.5 |
| 3 | 0.3 |

Calculate expected value.

$$
E(X)=1(0.2)+2(0.5)+3(0.3)
$$

$$
=0.2+1.0+0.9
$$

$$
\boxed{E(X)=2.1}
$$

## 16.3 Continuous Formula

$$
E(X)=\int_{-\infty}^{\infty}xf(x)\,dx
$$

## 16.4 Expected Value Properties

$$
E(c)=c
$$

$$
E(aX+b)=aE(X)+b
$$

$$
E(X+Y)=E(X)+E(Y)
$$

### AI/ML Application

Expected value is used in:
- Expected model loss.
- Risk estimation.
- Reinforcement learning rewards.
- Decision-making under uncertainty.

---

# 17. VARIANCE AND STANDARD DEVIATION

## 17.1 Variance

Variance measures how far the values of a random variable spread around their expected value.

Formula:

$$
Var(X)=E[(X-\mu)^2]
$$

Another formula:

$$
Var(X)=E(X^2)-[E(X)]^2
$$

Where:

$$
\mu=E(X)
$$

## 17.2 Standard Deviation

Standard deviation is the square root of variance.

$$
\sigma=\sqrt{Var(X)}
$$

### Example

Suppose:

$$
X=\{2,4,6\}
$$

Mean:

$$
\mu=\frac{2+4+6}{3}=4
$$

Variance:

$$
Var(X)=\frac{(2-4)^2+(4-4)^2+(6-4)^2}{3}
$$

$$
=\frac{4+0+4}{3}
$$

$$
\boxed{Var(X)=\frac83}
$$

Standard deviation:

$$
\sigma=\sqrt{\frac83}
$$

$$
\boxed{\sigma\approx1.633}
$$

Note: This calculation treats the three values as the complete population. For a sample variance, the denominator is n - 1.

---

# 18. COVARIANCE AND CORRELATION

## 18.1 Covariance

Covariance measures how two variables change together.

Population covariance:

$$
Cov(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]
$$

Interpretation:

- Positive covariance: Variables tend to increase together.
- Negative covariance: One tends to increase when the other decreases.
- Zero covariance: No linear co-movement is indicated.

## 18.2 Correlation

Correlation measures the strength and direction of a linear relationship between two variables.

Pearson correlation:

$$
r=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}
$$

Range:

$$
-1\leq r\leq1
$$

Interpretation:

| Correlation | Meaning |
|---|---|
| +1 | Perfect positive linear relationship |
| 0 | No linear correlation |
| -1 | Perfect negative linear relationship |

Important:

Correlation does not imply causation.

### AI/ML Application

- Feature selection.
- Exploratory Data Analysis.
- Detecting relationships.
- Multicollinearity analysis.

---

# 19. IMPORTANT PROBABILITY DISTRIBUTIONS

## 19.1 Bernoulli Distribution

A Bernoulli random variable has only two possible outcomes:

- Success = 1
- Failure = 0

Formula:

$$
P(X=x)=p^x(1-p)^{1-x}
$$

Where:

$$
x\in\{0,1\}
$$

Mean:

$$
E(X)=p
$$

Variance:

$$
Var(X)=p(1-p)
$$

Example:

A student passes or fails an exam.

AI/ML application:
- Binary classification.
- Click prediction.
- Spam detection.

## 19.2 Binomial Distribution

A binomial distribution models the number of successes in n independent trials, each with the same success probability p.

Formula:

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
$$

Mean:

$$
E(X)=np
$$

Variance:

$$
Var(X)=np(1-p)
$$

Example:

A coin is tossed 5 times. Find the probability of getting exactly 3 Heads.

$$
n=5,\quad k=3,\quad p=0.5
$$

$$
P(X=3)=\binom53(0.5)^3(0.5)^2
$$

$$
=10\times0.125\times0.25
$$

$$
\boxed{P(X=3)=0.3125}
$$

## 19.3 Poisson Distribution

Poisson distribution models the number of events occurring in a fixed interval when events happen independently at a constant average rate.

Formula:

$$
P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}
$$

Where:
- λ = Average number of events.
- k = Number of events.
- e = Euler's number.

Mean:

$$
E(X)=\lambda
$$

Variance:

$$
Var(X)=\lambda
$$

Example:

A website receives an average of 2 support requests per minute.

Find the probability of receiving exactly 3 requests in one minute.

$$
\lambda=2,\quad k=3
$$

$$
P(X=3)=\frac{e^{-2}2^3}{3!}
$$

$$
\boxed{P(X=3)\approx0.1804}
$$

AI/ML application:
- Website traffic analysis.
- Call center demand.
- Event frequency modelling.

## 19.4 Uniform Distribution

In a continuous uniform distribution, all values within an interval have equal probability density.

For a continuous uniform distribution on [a,b]:

$$
f(x)=\frac{1}{b-a},\quad a\leq x\leq b
$$

Mean:

$$
E(X)=\frac{a+b}{2}
$$

Variance:

$$
Var(X)=\frac{(b-a)^2}{12}
$$

Example:

A random number is selected uniformly between 0 and 10.

$$
P(2\leq X\leq5)=\frac{5-2}{10-0}
$$

$$
\boxed{P(2\leq X\leq5)=0.3}
$$

## 19.5 Normal Distribution

Normal distribution is a continuous probability distribution that forms a symmetric bell-shaped curve.

Formula:

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

Where:
- μ = Mean.
- σ = Standard deviation.
- σ² = Variance.

Properties:
- Bell-shaped curve.
- Symmetric around the mean.
- Mean = Median = Mode.
- Total area under the curve = 1.

### Empirical Rule

For a normal distribution:

| Range | Approximate Data |
|---|---:|
| μ ± 1σ | 68% |
| μ ± 2σ | 95% |
| μ ± 3σ | 99.7% |

## 19.6 Standard Normal Distribution

A standard normal distribution has:

$$
\mu=0,\quad \sigma=1
$$

Z-score formula:

$$
Z=\frac{X-\mu}{\sigma}
$$

Example:

Mean marks = 70.

Standard deviation = 10.

Student marks = 90.

$$
Z=\frac{90-70}{10}
$$

$$
\boxed{Z=2}
$$

Meaning: The student's score is 2 standard deviations above the mean.

## 19.7 Exponential Distribution

Exponential distribution models the waiting time between events in a Poisson process.

PDF:

$$
f(x)=\lambda e^{-\lambda x},\quad x\geq0
$$

Mean:

$$
E(X)=\frac{1}{\lambda}
$$

Variance:

$$
Var(X)=\frac{1}{\lambda^2}
$$

AI/ML application:
- Waiting-time modelling.
- Reliability analysis.
- Time-to-event modelling.

## 19.8 Student's t-Distribution

The t-distribution is used for statistical inference about a population mean, especially when the population standard deviation is unknown and the sample is relatively small under suitable assumptions.

It is symmetric and has heavier tails than the standard normal distribution.

AI/ML and statistics applications:
- Confidence intervals.
- Hypothesis testing.
- Comparing sample means.

---

# 20. LAW OF LARGE NUMBERS

## 20.1 Definition

The Law of Large Numbers states that as the number of independent repetitions increases, the sample average tends to approach the expected value.

In simple words:

Experiment jitni baar repeat karoge, observed average theoretical expected value ke closer aa sakta hai.

Example:

Fair coin toss:

$$
P(H)=0.5
$$

Agar coin ko 10 times toss karte hain, observed Head ratio 0.5 se different ho sakta hai.

Agar coin ko bahut zyada times toss karte hain, observed Head ratio generally 0.5 ke closer approach karega.

## 20.2 AI/ML Application

- Monte Carlo simulation.
- Model evaluation.
- Statistical estimation.
- Sampling techniques.

---

# 21. CENTRAL LIMIT THEOREM (CLT)

## 21.1 Definition

The Central Limit Theorem states that, under suitable conditions, the sampling distribution of the sample mean approaches a normal distribution as sample size becomes sufficiently large, even if the original population is not normally distributed.

## 21.2 Formula

For sample mean:

$$
\mu_{\bar X}=\mu
$$

Standard error:

$$
SE=\frac{\sigma}{\sqrt n}
$$

Where:
- μ = Population mean.
- σ = Population standard deviation.
- n = Sample size.

### Example

Population mean:

$$
\mu=100
$$

Population standard deviation:

$$
\sigma=20
$$

Sample size:

$$
n=100
$$

Standard error:

$$
SE=\frac{20}{\sqrt{100}}
$$

$$
\boxed{SE=2}
$$

### AI/ML Application

- Sampling distributions.
- Confidence intervals.
- Statistical inference.
- Model performance estimation.

---

# 22. SAMPLING TECHNIQUES

Sampling means selecting a subset of a population to study the population.

## 22.1 Simple Random Sampling

Every population member has an equal chance of selection.

## 22.2 Systematic Sampling

Select every kth member after a random starting point.

## 22.3 Stratified Sampling

Divide the population into groups called strata and sample from each group.

Example:
- First-year students.
- Second-year students.
- Third-year students.

## 22.4 Cluster Sampling

Divide the population into clusters, randomly select clusters, and study members within selected clusters.

## 22.5 Sampling in Machine Learning

Train-test split is a common sampling technique.

Example:

- 80% training data.
- 20% testing data.

For classification, stratified splitting can help preserve class proportions.

---

# 23. MONTE CARLO SIMULATION

## 23.1 Definition

Monte Carlo simulation is a computational technique that uses repeated random sampling to estimate numerical results or probabilities.

### Example: Estimate Probability of Getting Heads

```python
import random

trials = 100000
heads = 0

for _ in range(trials):
    result = random.choice(["H", "T"])

    if result == "H":
        heads += 1

probability = heads / trials

print("Estimated Probability:", probability)
```

Explanation:

- `import random`: Imports Python's random module.
- `trials`: Number of coin tosses.
- `heads`: Counts the number of Heads.
- `random.choice()`: Randomly selects H or T.
- `if result == "H"`: Checks whether Head occurred.
- `heads += 1`: Increases the Head count.
- `heads / trials`: Calculates the experimental probability.

Expected output: A value close to 0.5.

---

# 24. PYTHON IMPLEMENTATION OF PROBABILITY

## 24.1 Using Basic Python

```python
favourable = 3
total = 6

probability = favourable / total

print("Probability:", probability)
```

## 24.2 Using NumPy

```python
import numpy as np

data = np.array([1, 2, 3, 4, 5, 6])

even_numbers = data[data % 2 == 0]

probability = len(even_numbers) / len(data)

print("Even Number Probability:", probability)
```

Explanation:

- `np.array()`: Creates an array.
- `data % 2 == 0`: Checks which values are even.
- `data[...]`: Selects even values.
- `len()`: Counts the selected values.
- Division calculates the probability.

## 24.3 Binomial Distribution Using SciPy

```python
from scipy.stats import binom

n = 5
p = 0.5
k = 3

probability = binom.pmf(k, n, p)

print("Probability:", probability)
```

`binom.pmf()` calculates the probability of exactly k successes in n independent Bernoulli trials.

## 24.4 Normal Distribution Using SciPy

```python
from scipy.stats import norm

mean = 70
std = 10

probability = norm.cdf(80, loc=mean, scale=std)

print("P(X <= 80):", probability)
```

`norm.cdf()` calculates the probability that X is less than or equal to 80.

## 24.5 Bayes' Theorem Using Python

```python
prior = 0.01
sensitivity = 0.90
specificity = 0.95

false_positive = 1 - specificity

positive_probability = (
    sensitivity * prior
    + false_positive * (1 - prior)
)

posterior = (
    sensitivity * prior
    / positive_probability
)

print("Posterior Probability:", posterior)
print("Percentage:", posterior * 100)
```

This code calculates the probability of disease given a positive test result using Bayes' theorem.

---

# 25. APPLICATIONS OF PROBABILITY IN AI/ML

## 25.1 Naive Bayes Classifier

Uses Bayes' theorem to predict class probabilities.

Applications:
- Spam detection.
- Sentiment analysis.
- Document classification.

## 25.2 Logistic Regression

Predicts class probabilities for binary classification.

Sigmoid function:

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

Output lies between 0 and 1.

## 25.3 Decision Trees

Can estimate class probabilities using the proportion of training samples in a leaf.

## 25.4 Hidden Markov Models

Use probabilities to model sequences with hidden states.

Applications:
- Speech recognition.
- Sequence analysis.
- Natural Language Processing.

## 25.5 Reinforcement Learning

Uses probability to model uncertain actions, transitions, and rewards.

## 25.6 Bayesian Machine Learning

Uses prior distributions and observed data to update beliefs about model parameters.

---


