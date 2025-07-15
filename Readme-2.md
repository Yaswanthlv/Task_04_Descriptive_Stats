# Task_04_Descriptive_Stats

This project focuses on descriptive statistics using three different approaches in Python:

1. Pure Python (no third-party libraries)
2. Pandas
3. Polars

The dataset used represents real-world app metadata from the **Apple App Store (10,000 apps)** dataset available on [Kaggle](https://www.kaggle.com/datasets/ramamet4/app-store-apple-data-set-10k-apps).

> **Note**: The dataset file is not included in this repository. Please download it manually from Kaggle and place it in the `data/` directory.

---

## Repository Structure
.
├── .gitignore
├── pure_python_stats.py
├── pandas_stats.py
├── polars_stats.py
├── README.md
└── data/
    └── AppleStore.csv 

---

## Summary of Work

Each script performs:

- Count, Mean, Min, Max, and Standard Deviation for numeric columns
- Unique value counts and most frequent values for categorical columns
- Grouped stats by:
  - `prime_genre`
  - `prime_genre + track_name`

---

## Requirements

You will need:

- Python 3.8+
- The following libraries:
  - `pandas`
  - `polars`

---

## Key Insights

> Example (you can customize this based on your findings):

- Games and Entertainment are the most dominant genres in the App Store.
- Most apps are free, but a small number of paid apps drive high user engagement.
- Average user rating across all apps is around 3.5.
- Polars performs better with large group-by operations compared to Pandas.
- Pure Python works but is verbose and slower for large datasets.

---

## Dataset Source

**Apple App Store (10K Apps)**  
🔗 https://www.kaggle.com/datasets/ramamet4/app-store-apple-data-set-10k-apps
