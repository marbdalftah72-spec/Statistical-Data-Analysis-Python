# 📊 Statistical Data Analysis & Exploratory Modeling in Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Data Science](https://img.shields.io/badge/Libraries-Pandas%20%7C%20NumPy%20%7C%20Seaborn%20%7C%20SciPy-informational.svg)](https://scipy.org/)
[![Kaggle](https://img.shields.io/badge/Datasets-Kaggle%20Curated-20BEFF.svg?logo=kaggle&logoColor=white)](https://kaggle.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An exhaustive, mathematically rigorous empirical study conducting **Statistical Hypothesis Testing, Inferential Analytics, and Exploratory Data Analysis (EDA)** across real-world datasets sourced from Kaggle. Authored by **Ammar Abdelfattah** at **Faculty of Engineering – New Ismailia National University (NINU)**.

---

## 📌 Analytical Methodologies & Modules

This repository covers the complete analytical lifecycle from raw data ingestion to hypothesis validation:

1. **Data Cleaning & Munging Pipeline**:
   - Treatment of missing data patterns (MCAR, MAR, MNAR) via median/mode imputation and iterative multivariate methods.
   - Robust detection of outliers using Interquartile Range ($IQR = Q_3 - Q_1$) and Mahalanobis distance.
   - Detection and remediation of heteroscedasticity and non-normality via Box-Cox and Yeo-Johnson power transformations.

2. **Descriptive Statistics & Dispersion Analysis**:
   - Parametric measures: Mean ($\mu$), Variance ($\sigma^2$), Standard Deviation ($\sigma$).
   - Non-parametric measures: Median, Median Absolute Deviation (MAD), Interquartile Range.
   - Shape metrics: Pearson's Skewness coefficient and Fisher's Kurtosis (measuring tail-heaviness vs Gaussian distributions).

3. **Inferential Statistics & Hypothesis Testing**:
   - Normality verification: Shapiro-Wilk test, D'Agostino-Pearson omnibus test, and Q-Q probability plots.
   - Two-sample comparison: Independent Student's $t$-test vs Mann-Whitney $U$ test (non-parametric rank-sum).
   - Multi-group variance: One-way ANOVA ($F$-statistic) and Kruskal-Wallis $H$-test followed by Tukey's HSD post-hoc pairwise testing.
   - Categorical association: Pearson's Chi-Square ($\chi^2$) test of independence and Fisher's Exact test.

4. **Correlation & Bivariate Association**:
   - Pearson's product-moment correlation ($r$).
   - Spearman's monotonic rank correlation ($\rho$) and Kendall's Tau ($\tau$).
   - Covariance matrices and multicollinearity diagnosis via Variance Inflation Factor (VIF).

---

## 📁 Repository Structure

```text
├── notebooks/
│   └── Comprehensive_Statistical_Analysis.ipynb # Full reproducible Jupyter Notebook
├── scripts/
│   └── statistical_engine.py                    # Modular statistical functions
├── data/
│   └── sample_dataset.csv                       # Benchmark dataset
├── requirements.txt                             # Python dependencies
└── README.md                                    # Project documentation
```

---

## 🚀 Quickstart

```bash
# Clone the repository
git clone https://github.com/marbdalftah72-spec/Statistical-Data-Analysis-Python.git
cd Statistical-Data-Analysis-Python

# Install dependencies
pip install -r requirements.txt

# Run analytical notebook
jupyter notebook notebooks/Comprehensive_Statistical_Analysis.ipynb
```

---

## 👨‍💻 Author

- **Ammar Abdelfattah**
- Faculty of Engineering, **New Ismailia National University (NINU)**
