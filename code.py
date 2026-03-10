# 10/03/26
# Project: Breast Cancer Statistical Analysis


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Breast_cancer_data.csv")
df_copy = df.copy()

print(df.head())
print(df.shape)


# -------------------------------------------------
# Distribution of Mean Radius
# -------------------------------------------------

sns.histplot(df['mean_radius'], kde=True)
plt.title("Distribution of Mean Radius")
plt.show()


# -------------------------------------------------
# Skewness and Kurtosis
# -------------------------------------------------

from scipy.stats import skew, kurtosis

print("Skewness:", skew(df['mean_radius']))
print("Kurtosis:", kurtosis(df['mean_radius']))


# -------------------------------------------------
# KS Test (Normality Test)
# -------------------------------------------------

from scipy.stats import kstest

stat, p_value = kstest(df['mean_radius'], 'norm',
                       args=(np.mean(df['mean_radius']),
                             np.std(df['mean_radius'])))

print("KS Test p-value:", p_value)


# -------------------------------------------------
# Central Limit Theorem Simulation
# -------------------------------------------------

def estimate_clt(data, no_of_samples, sample_size):

    sample_mean = []

    for i in range(no_of_samples):

        samples = np.random.choice(data, size=sample_size)

        sample_mean.append(np.mean(samples))

    return sample_mean


data = df['mean_radius']
no_of_samples = 1000
sample_size = 30

array_estimated_mean = estimate_clt(data, no_of_samples, sample_size)

sns.histplot(array_estimated_mean, kde=True)
plt.title("CLT Distribution of Sample Means")
plt.show()


# -------------------------------------------------
# Bootstrapping Confidence Interval
# -------------------------------------------------

def bootstrapping(data, no_of_samples, sample_size, CI):

    sample_mean = []

    for i in range(no_of_samples):

        samples = np.random.choice(data,
                                   size=sample_size,
                                   replace=True)

        sample_mean.append(np.mean(samples))

    sorted_lst = np.sort(sample_mean)

    lower_index = int(((100-CI)/2)/100 * no_of_samples)
    upper_index = int((CI + (100-CI)/2)/100 * no_of_samples)

    return sorted_lst[lower_index], sorted_lst[upper_index]


data = df['mean_radius']
no_of_samples = 1000
sample_size = 30
CI = 95

CI_range = bootstrapping(data, no_of_samples, sample_size, CI)

print("Bootstrapping CI:", CI_range)


# -------------------------------------------------
# Chebyshev's Theorem
# -------------------------------------------------

def estimating_sd_range_chebyshevs(mean, sd, k):

    LL = mean - k * sd
    UL = mean + k * sd

    per = 1 - (1/(k**2))

    return LL, UL, per


data = df['mean_radius']

mean = np.mean(data)
sd = np.std(data)

print("Chebyshev Range:", estimating_sd_range_chebyshevs(mean, sd, 3))


# -------------------------------------------------
# Convert Radius into Tumor Size Category
# -------------------------------------------------

def tumor_category(radius):

    if radius <= 12:
        return "Small"

    elif radius <= 18:
        return "Medium"

    else:
        return "Large"


df['Tumor_Size'] = df['mean_radius'].apply(tumor_category)

print(df['Tumor_Size'].value_counts())


# -------------------------------------------------
# Tumor Category Distribution
# -------------------------------------------------

sns.countplot(x='Tumor_Size', data=df)

plt.title("Tumor Size Distribution")
plt.show()


# -------------------------------------------------
# Distribution by Diagnosis
# 0 = Malignant
# 1 = Benign
# -------------------------------------------------

df['Diagnosis_Label'] = df['diagnosis'].map({
    0: "Malignant",
    1: "Benign"
})

print(pd.crosstab(df['Tumor_Size'], df['Diagnosis_Label']))


sns.countplot(x='Tumor_Size', hue='Diagnosis_Label', data=df)

plt.title("Tumor Size by Diagnosis")
plt.show()


# -------------------------------------------------
# Skewness & Kurtosis by Diagnosis
# -------------------------------------------------

for diagnosis in df['Diagnosis_Label'].unique():

    data = df[df['Diagnosis_Label'] == diagnosis]['mean_radius']

    print("Diagnosis:", diagnosis)
    print("Skewness:", skew(data))
    print("Kurtosis:", kurtosis(data))
    print()


# -------------------------------------------------
# KS Test by Diagnosis
# -------------------------------------------------

for diagnosis in df['Diagnosis_Label'].unique():

    data = df[df['Diagnosis_Label'] == diagnosis]['mean_radius']

    stat, p = kstest(data,
                     'norm',
                     args=(np.mean(data),
                           np.std(data)))

    print("Diagnosis:", diagnosis)
    print("KS Test p-value:", p)
    print()


# -------------------------------------------------
# Distribution Visualization
# -------------------------------------------------

sns.histplot(data=df,
             x='mean_radius',
             hue='Diagnosis_Label',
             kde=True)

plt.title("Mean Radius Distribution by Diagnosis")

plt.show()
