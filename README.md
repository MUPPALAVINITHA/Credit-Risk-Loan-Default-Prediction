# Credit-Risk-Loan-Default-Prediction

### 🚀 Project Overview

This project presents an end-to-end Credit Risk Prediction System designed to identify loan applicants who are likely to default.

The solution simulates a real-world banking risk assessment workflow by applying:
- Dataset overview and understanding
- Exploratory Data Analysis (EDA)
- Data preprocessing 
- Model Used (Logistic Regression, Random Forest, XGBoost)
- Threshold optimization for business decision-making
- Business-aligned evaluation metrics (ROC-AUC, recall focus)
- Deployment using Streamlit for real-time predictions

The final system enables financial institutions to make data-driven loan approval decisions while minimizing default risk.

### 🎯 Problem Statement

Loan defaults significantly impact financial institutions.

The objective of this project is to:
- Predict whether a loan applicant will default
- Maximize detection of high-risk applicants (defaulters)
- Align model performance with business risk priorities
  
### 📂 Dataset Description
- Dataset Source: Kaggle – Home Credit Default Risk
- Number of Records: 307,511 loan applications
- Number of Features: 122 (mix of numerical and categorical)
- Target Variable: TARGET
   - 0 → No default (282,686 cases)
   - 1 → Default (24,825 cases)
- Data Type: Structured tabular dataset

### Exploratory Data Analysis
##### Purpose of EDA:
To understand customer behavior, identify risk patterns, and support meaningful feature engineering.

#### Key EDA Findings:
##### 1. Target Variable Distribution:
- The dataset is highly imbalanced, with far more non-defaulters than defaulters.
- This can bias models toward predicting “no default.”
- To address this, ROC-AUC was used instead of accuracy, and threshold tuning was applied to improve defaulter detection and risk sensitivity.

<img width="989" height="466" alt="image" src="https://github.com/user-attachments/assets/a79b2585-8b1f-4868-98c8-4727c57a85de" />

##### 2. Income vs Default Behavior
- Applicants with lower total income show a higher default rate. 
- High-income customers are more stable and less risky.
- Insight used to create: Credit-to-Income and Annuity-to-Income ratios.
  
<img width="989" height="466" alt="image" src="https://github.com/user-attachments/assets/5a7c2326-90f9-4d5a-8011-599638d60b92" />

##### 3. Education Level vs Default
- Applicants with lower education have slightly higher default rates.
- Higher education correlates with lower risk of default.

<img width="989" height="499" alt="image" src="https://github.com/user-attachments/assets/08378e09-0251-4485-bd87-6594ba18925d" />
 
##### 4. Family Status vs Default                                                                                                
- Individuals in civil marriages and those who are single have a higher probability of default compared to married or widowed applicants.
- Widows have lowest defaults; unknown status may indicate missing data.

<img width="989" height="499" alt="image" src="https://github.com/user-attachments/assets/ba28792f-56e5-46f4-ae6a-0b178063af56" />

### 🛠️ Data PreProcessing 
- Explored dataset to understand feature types, missing values, and target distribution
- Checked duplicates and categorized variables into numerical and categorical features
- Handled missing values using median (numerical) and most frequent (categorical)
- Performed feature engineering to create:
     - Credit-to-Income ratio
     - Annuity-to-Income ratio
- Included Occupation Type as a key categorical feature to represent employment profile
- Applied scaling and one-hot encoding using preprocessing pipelines
- Split data into training and testing sets
- Built machine learning pipelines for Logistic Regression, Random Forest, and XGBoost
- Evaluated models using ROC-AUC, confusion matrix, classification report, and threshold tuning
- Deployed the final model using a Streamlit web application for real-time credit risk prediction

### 🤖 Models Implemented
1️⃣ Logistic Regression (Baseline & interpretable model)
2️⃣ Random Forest (Non-linear pattern detection)
3️⃣ XGBoost (Best performing model)

The final selected model: XGBoost

### 📊 Model Evaluation and Optimization

Model performance was evaluated using ROC-AUC, precision, recall, F1-score, and confusion matrix.
The dataset was highly imbalanced, so recall for defaulters was prioritized.
The classification threshold was tuned using the precision-recall curve to achieve a recall of 0.70 for defaulters
This ensured more high-risk applicants were correctly identified, reducing false negatives.
XGBoost achieved the best overall performance and was selected as the final model.

### 🔍 Threshold Optimization

The classification threshold was tuned using the precision-recall curve to achieve:

👉 70% recall for defaulters

This ensures the bank detects the majority of high-risk applicants while managing false positives.

### 🏆 Final Model Performance
## Model	                   ROC-AUC

Logistic Regression  	—      0.7488

Random Forest	        —      0.7373

XGBoost               —	     0.7687

Why XGBoost?
- Highest ROC-AUC
- Best recall for defaulters
- Business-aligned predictions
- Strong handling of feature interactions

### Deployment
- The final trained pipeline was saved using pickle/joblib and deployed using Streamlit.
- The application allows users to input applicant details and receive real-time:
    - Default probability
    - Risk prediction (High/Low risk)
<img width="1101" height="789" alt="Screenshot 2026-04-06 131554" src="https://github.com/user-attachments/assets/f6528cb4-e7d1-468e-8147-c2cf253d35fe" />
<img width="1152" height="482" alt="Screenshot 2026-04-06 131623" src="https://github.com/user-attachments/assets/bcddcaee-e443-42ae-94c4-05f786e650b4" />

### Business Impact

This system helps financial institutions make better lending decisions by identifying high-risk applicants early, reducing loan defaults, and improving overall risk management through data-driven decision-making.
