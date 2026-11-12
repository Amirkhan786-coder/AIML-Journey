## 1. IMPORTANT INTERVIEW QUESTIONS AND ANSWERS

**Q1. What is Statistics?**

Statistics is the science of collecting, organizing, analyzing and interpreting data.

**Q2. What are the two main types of Statistics?**

Descriptive Statistics and Inferential Statistics.

**Q3. What is the difference between Population and Sample?**

Population is the complete group, whereas Sample is a subset selected from that group.

**Q4. What is Mean?**

Mean is the sum of all observations divided by the total number of observations.

**Q5. What is Median?**

Median is the middle value of an ordered dataset.

**Q6. What is Mode?**

Mode is the most frequently occurring value.

**Q7. Which measure is less affected by outliers: Mean or Median?**

Median.

**Q8. What is Variance?**

Variance measures the average squared deviation from the mean.

**Q9. What is Standard Deviation?**

Standard Deviation is the square root of variance.

**Q10. What is IQR?**

IQR is the difference between the third quartile and first quartile.

$$
IQR=Q_3-Q_1
$$

**Q11. What is an Outlier?**

An outlier is an observation that is unusually far from the rest of the dataset.

**Q12. What is Covariance?**

Covariance measures how two variables change together.

**Q13. What is Correlation?**

Correlation measures the strength and direction of a relationship between two variables.

**Q14. What is the range of Pearson Correlation?**

$$
-1\leq r\leq+1
$$

**Q15. Does correlation imply causation?**

No. Correlation does not prove a cause-and-effect relationship.

**Q16. What is Skewness?**

Skewness measures the asymmetry of a distribution.

**Q17. What is Kurtosis?**

Kurtosis describes the tail heaviness of a distribution relative to a normal distribution.

**Q18. What is a Normal Distribution?**

A continuous, symmetric, bell-shaped probability distribution.

**Q19. What is Z-Score?**

Z-score measures how many standard deviations an observation is away from the mean.

**Q20. What is MAE?**

MAE measures the average absolute prediction error.

**Q21. What is MSE?**

MSE measures the average squared prediction error.

**Q22. What is RMSE?**

RMSE is the square root of MSE.

**Q23. What is R² Score?**

R² measures the proportion of target variation explained by a regression model relative to a mean baseline.

---

## 2. PRACTICE QUESTIONS WITH SOLUTIONS

### Q1. Find the Mean.

Dataset:

$$
[10,20,30,40,50]
$$

Solution:

$$
Mean=\frac{10+20+30+40+50}{5}
$$

$$
\boxed{Mean=30}
$$

### Q2. Find the Median.

Dataset:

$$
[5,10,15,20,25]
$$

Solution:

Middle value = 15.

$$
\boxed{Median=15}
$$

### Q3. Find the Median of an Even Dataset.

Dataset:

$$
[10,20,30,40]
$$

Solution:

$$
Median=\frac{20+30}{2}
$$

$$
\boxed{Median=25}
$$

### Q4. Find the Mode.

Dataset:

$$
[2,3,3,4,5,3,6]
$$

Solution:

3 occurs three times.

$$
\boxed{Mode=3}
$$

### Q5. Find the Range.

Dataset:

$$
[12,25,30,45,60]
$$

Solution:

$$
Range=60-12
$$

$$
\boxed{Range=48}
$$

### Q6. Find Population Variance.

Dataset:

$$
[2,4,6]
$$

Solution:

$$
Mean=4
$$

$$
Variance=\frac{(2-4)^2+(4-4)^2+(6-4)^2}{3}
$$

$$
=\frac{4+0+4}{3}
$$

$$
\boxed{Variance=2.67}
$$

### Q7. If Variance = 25, find Standard Deviation.

$$
SD=\sqrt{25}
$$

$$
\boxed{SD=5}
$$

### Q8. Find IQR.

Given:

$$
Q_1=20,\quad Q_3=60
$$

$$
IQR=60-20
$$

$$
\boxed{IQR=40}
$$

### Q9. Find Z-Score.

Given:

$$
X=70,\quad\mu=50,\quad\sigma=10
$$

$$
Z=\frac{70-50}{10}
$$

$$
\boxed{Z=2}
$$

### Q10. Find MAE.

Actual:

$$
[10,20,30]
$$

Predicted:

$$
[12,18,35]
$$

$$
MAE=\frac{2+2+5}{3}
$$

$$
\boxed{MAE=3}
$$

### Q11. Find MSE.

$$
MSE=\frac{(10-12)^2+(20-18)^2+(30-35)^2}{3}
$$

$$
=\frac{4+4+25}{3}
$$

$$
\boxed{MSE=11}
$$

### Q12. Find RMSE.

$$
RMSE=\sqrt{11}
$$

$$
\boxed{RMSE\approx3.32}
$$

---

## 3. MULTIPLE CHOICE QUESTIONS (MCQs)

**Q1. Which measure represents the average of a dataset?**

A. Median  
B. Mode  
C. Mean  
D. Range  

**Answer: C. Mean**

**Q2. Which measure is less affected by extreme outliers?**

A. Mean  
B. Median  
C. Variance  
D. Range  

**Answer: B. Median**

**Q3. What does Mode represent?**

A. Average value  
B. Middle value  
C. Most frequent value  
D. Maximum value  

**Answer: C. Most frequent value**

**Q4. What is the formula for Range?**

A. Maximum + Minimum  
B. Maximum - Minimum  
C. Mean / Count  
D. Sum / Count  

**Answer: B. Maximum - Minimum**

**Q5. Standard Deviation is the square root of:**

A. Mean  
B. Median  
C. Variance  
D. Range  

**Answer: C. Variance**

**Q6. What is the range of Pearson Correlation?**

A. 0 to 100  
B. -1 to +1  
C. 1 to 10  
D. -10 to +10  

**Answer: B. -1 to +1**

**Q7. What is IQR?**

A. Q1 + Q3  
B. Q3 - Q1  
C. Q2 - Q1  
D. Q3 + Q2  

**Answer: B. Q3 - Q1**

**Q8. Which distribution is bell-shaped and symmetric?**

A. Normal  
B. Poisson  
C. Bernoulli  
D. Binomial  

**Answer: A. Normal**

**Q9. Which metric penalizes large errors more strongly due to squaring?**

A. MAE  
B. MSE  
C. Median  
D. Mode  

**Answer: B. MSE**

**Q10. Which library provides `np.mean()`?**

A. Pandas  
B. Matplotlib  
C. NumPy  
D. Seaborn  

**Answer: C. NumPy**

**Q11. Which function calculates correlation in NumPy?**

A. `np.mean()`  
B. `np.corrcoef()`  
C. `np.median()`  
D. `np.std()`  

**Answer: B. `np.corrcoef()`**

**Q12. What does a positive correlation indicate?**

A. Variables generally move in opposite directions  
B. Variables generally move in the same direction  
C. No relationship of any kind  
D. One variable is always the cause of another  

**Answer: B. Variables generally move in the same direction**

**Q13. What does Z-Score measure?**

A. Total observations  
B. Number of standard deviations from the mean  
C. Median value  
D. Variance only  

**Answer: B. Number of standard deviations from the mean**

**Q14. Which statistic is useful for finding the most frequent category?**

A. Mean  
B. Median  
C. Mode  
D. Variance  

**Answer: C. Mode**

**Q15. What does R² evaluate in regression?**

A. Classification accuracy  
B. Explained variation relative to a mean baseline  
C. Number of features  
D. Dataset size  

**Answer: B. Explained variation relative to a mean baseline**

---


