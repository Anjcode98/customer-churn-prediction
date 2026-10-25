# Customer Churn Prediction System

An end-to-end machine learning project for predicting
customer churn in a telecommunications business.

## Project Goals

- Explore and preprocess customer data
- Train classification models
- Evaluate model performance
- Build a prediction API using FastAPI
- Containerize the application using Docker

## Technologies

- Python
- pandas and NumPy
- scikit-learn
- FastAPI
- Docker
- GitHub Actions

## Project Status

In development — Lesson 1: Environment Setup

## Author

Anjana MAdusanka Weerarathna


## Dataset

This project uses the IBM Telco Customer Churn dataset,
available on Kaggle:

https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Download:
WA_Fn-UseC_-Telco-Customer-Churn.csv

Place the file in:
data/raw/

Raw data is not committed to this repository.

## Exploratory Data Analysis

Notebook:
notebooks/01_exploratory_data_analysis.ipynb

Key findings:
- 7,043 customers
- Approximately 26.5% churn rate
- 11 missing/unconvertible TotalCharges values
- Higher observed churn among month-to-month customers

## Run Data Validation

From the project root:

python -m src.validate_data

## Project Progress

- [x] Lesson 1: Environment setup
- [x] Lesson 2: Dataset acquisition and EDA
- [ ] Lesson 3: Data preprocessing
- [ ] Lesson 4: Logistic Regression
- [ ] Lesson 5: Random Forest and evaluation
- [ ] Lesson 6: FastAPI
- [ ] Lesson 7: Docker and testing
- [ ] Lesson 8: Portfolio documentation
