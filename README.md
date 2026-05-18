# Customer Churn Prediction using Machine Learning

## Project Overview

This project predicts customer churn for a telecom company using machine learning techniques. The objective was to identify customers likely to leave the service and understand the key factors driving churn.

The project combines:

* SQL analytics
* PostgreSQL database integration
* Python data preprocessing
* Machine learning classification models
* Data visualisation

---

## Technologies Used

* Python
* PostgreSQL
* SQLAlchemy
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn

---

## Dataset

Telco Customer Churn dataset from Kaggle.

The dataset contains customer information such as:

* tenure
* monthly charges
* contract type
* internet service
* payment methods
* churn status

---

## Project Workflow

### 1. Data Loading

* Imported CSV data into PostgreSQL
* Connected PostgreSQL with Python using SQLAlchemy

### 2. SQL Analysis

Performed SQL queries to analyse:

* churn distribution
* churn by contract type
* churn by payment method
* customer behaviour trends

### 3. Data Preprocessing

* handled missing values
* converted categorical variables using one-hot encoding
* removed non-predictive columns

### 4. Machine Learning Models

Models used:

* Logistic Regression
* Random Forest Classifier

### 5. Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## Key Findings

* Customers with shorter tenure were more likely to churn.
* Higher monthly charges were associated with increased churn risk.
* Customers on two-year contracts were less likely to churn.

Logistic Regression achieved better overall performance and recall than Random Forest on this dataset.

---

## Business Recommendations

* Improve onboarding for new customers
* Target high-risk customers with retention campaigns
* Review pricing strategies for customers with high monthly charges

---

## Future Improvements

* Hyperparameter tuning
* Cross-validation
* Deployment using FastAPI or Flask
* Real-time churn prediction API

---

## Author

Stephen Sefa
# Customer Churn Prediction using Machine Learning

## Project Overview

This project predicts customer churn for a telecom company using machine learning techniques. The objective was to identify customers likely to leave the service and understand the key factors driving churn.

The project combines:

* SQL analytics
* PostgreSQL database integration
* Python data preprocessing
* Machine learning classification models
* Data visualisation

---

## Technologies Used

* Python
* PostgreSQL
* SQLAlchemy
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn

---

## Dataset

Telco Customer Churn dataset from Kaggle.

The dataset contains customer information such as:

* tenure
* monthly charges
* contract type
* internet service
* payment methods
* churn status

---

## Project Workflow

### 1. Data Loading

* Imported CSV data into PostgreSQL
* Connected PostgreSQL with Python using SQLAlchemy

### 2. SQL Analysis

Performed SQL queries to analyse:

* churn distribution
* churn by contract type
* churn by payment method
* customer behaviour trends

### 3. Data Preprocessing

* handled missing values
* converted categorical variables using one-hot encoding
* removed non-predictive columns

### 4. Machine Learning Models

Models used:

* Logistic Regression
* Random Forest Classifier

### 5. Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## Key Findings

* Customers with shorter tenure were more likely to churn.
* Higher monthly charges were associated with increased churn risk.
* Customers on two-year contracts were less likely to churn.

Logistic Regression achieved better overall performance and recall than Random Forest on this dataset.

---

## Business Recommendations

* Improve onboarding for new customers
* Target high-risk customers with retention campaigns
* Review pricing strategies for customers with high monthly charges

---

## Future Improvements

* Hyperparameter tuning
* Cross-validation
* Deployment using FastAPI or Flask
* Real-time churn prediction API

---

## Author

Stephen Sefa
