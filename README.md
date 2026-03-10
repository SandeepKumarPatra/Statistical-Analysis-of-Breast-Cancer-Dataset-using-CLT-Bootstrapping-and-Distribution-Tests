# Breast Cancer Statistical Analysis

## Project Overview

This project performs statistical analysis on a breast cancer dataset using Python.  
The objective is to understand data distribution and apply important statistical concepts such as:

- Distribution Analysis
- Skewness and Kurtosis
- Kolmogorov–Smirnov (KS) Test for normality
- Central Limit Theorem (CLT)
- Bootstrapping for Confidence Intervals
- Chebyshev’s Theorem
- Feature Categorization
- Comparative Analysis by Diagnosis (Benign vs Malignant)

This project helps demonstrate how statistical theory can be applied to real-world medical datasets.

---

## Dataset

Breast Cancer Dataset containing tumor measurement features such as:

- mean_radius
- mean_texture
- mean_perimeter
- mean_area
- mean_smoothness
- diagnosis

Diagnosis values:
- 0 → Malignant
- 1 → Benign

---

## Key Analysis

### 1 Distribution Analysis
Visualize the distribution of tumor radius using histogram and KDE.

### 2 Skewness and Kurtosis
Measure asymmetry and tail behavior of the distribution.

### 3 Normality Testing
Use the Kolmogorov–Smirnov test to determine whether the feature follows a normal distribution.

### 4 Central Limit Theorem Simulation
Random samples are drawn from the dataset to demonstrate that the sampling distribution of the mean approaches normal distribution.

### 5 Bootstrapping
Bootstrapping is used to estimate the confidence interval of the population mean.

### 6 Chebyshev’s Theorem
Estimate the probability range of values within k standard deviations.

### 7 Tumor Size Categorization
Tumors are categorized into:

- Small
- Medium
- Large

based on mean radius.

### 8 Diagnosis Comparison
Statistical properties and distributions are compared between:

- Benign tumors
- Malignant tumors

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy

---

## Learning Outcomes

This project demonstrates practical applications of:

- Statistical inference
- Sampling theory
- Distribution analysis
- Medical dataset exploration
- Data visualization

---

## Future Improvements

Possible extensions include:

- Logistic Regression for cancer prediction
- Feature importance analysis
- Machine Learning classification models
- ROC curve analysis
