# 19. Important Interview Questions

Q1. What is Seaborn?

Seaborn is a Python statistical data visualization library built on Matplotlib.

Q2. Why is Seaborn used?

It is used to create statistical graphs and analyze relationships, distributions, and patterns in data.

Q3. What is the difference between Seaborn and Matplotlib?

Matplotlib provides low-level plotting control, while Seaborn provides a higher-level interface with convenient statistical visualizations.

Q4. What is a heatmap?

A heatmap represents numerical data using colors in a matrix.

Q5. What is a correlation matrix?

It is a table showing pairwise correlation coefficients between numerical variables.

Q6. What is the difference between histogram and KDE?

A histogram displays frequency in bins, while KDE estimates a smooth probability density curve.

Q7. What is a box plot?

A box plot displays quartiles, median, whiskers, and potential outliers.

Q8. What is pairplot?

Pairplot visualizes pairwise relationships between numerical features.

Q9. What is hue in Seaborn?

`hue` is used to distinguish categories using different colors.

Q10. What is EDA?

EDA is the process of analyzing data using statistical methods and visualizations before modeling.

Q11. What is the difference between axes-level and figure-level functions?

Axes-level functions draw on a particular Matplotlib Axes, whereas figure-level functions manage an entire figure and support faceting.

Q12. Can Seaborn work with Pandas?

Yes. Seaborn directly supports Pandas DataFrames and column names.

# 20. Seaborn Practice Questions

Practice these questions yourself. Use the `tips`, `iris`, `titanic`, and `penguins` datasets.

## Level 1 — Beginner

1. Import Seaborn and Matplotlib.
2. Load the `tips` dataset.
3. Display the first 10 rows.
4. Find the number of rows and columns.
5. Create a histogram of `total_bill`.
6. Create a scatter plot of `total_bill` vs `tip`.
7. Create a count plot of `day`.
8. Create a bar plot of average tips by day.
9. Create a KDE plot of total bills.
10. Change the plot style to `whitegrid`.

## Level 2 — Intermediate

11. Create a box plot of total bills by day.
12. Create a violin plot of tips by gender.
13. Create a swarm plot of total bills by day.
14. Create a scatter plot using `hue="sex"`.
15. Create a line plot using the flights dataset.
16. Create a heatmap of numerical correlations.
17. Create a pair plot of the iris dataset.
18. Create a regression plot of total bill vs tip.
19. Create a joint plot of two numerical variables.
20. Visualize missing values using a heatmap.

## Level 3 — Advanced

21. Perform complete EDA on the Titanic dataset.
22. Compare survival rates by passenger class.
23. Visualize age distribution by gender.
24. Analyze relationships between fare and passenger class.
25. Create a pair plot of the penguins dataset.
26. Use FacetGrid to compare different categories.
27. Create a customized correlation heatmap.
28. Identify potential outliers using box plots.
29. Create a dashboard containing six different visualizations.
30. Perform complete EDA on a real-world dataset and write at least 10 insights.
#