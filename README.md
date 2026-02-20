# Credit-Risk-Loan-Default-Prediction

### 🚀 Project Overview

This project presents an end-to-end Credit Risk Prediction System designed to identify loan applicants who are likely to default.

The solution simulates a real-world banking risk assessment workflow by applying:
- Data set Overview
- Exploratory Data Analysis
- Data preprocessing
- Feature engineering
- Model comparison
- Threshold optimization
- Business-aligned evaluation
- Deployment using Streamlit

The final system enables financial institutions to make data-driven loan approval decisions while minimizing default risk.

### 🎯 Problem Statement

Loan defaults significantly impact financial institutions.

The objective of this project is to:

Predict whether a loan applicant will default

Maximize detection of high-risk applicants (defaulters)

Align model performance with business risk priorities

### 📂 Dataset Description

Dataset Source: Kaggle – Home Credit Default Risk

Number of Records: 307,511 loan applications

Number of Features: 122 (mix of numerical and categorical)

Target Variable: TARGET
    - 0 = 2,82,686 → No default
    - 1 = 24,825 → Default
     
Data Type: Structured, tabular data

##### Process Followed:
- Explored the dataset to understand feature types, missing values, and target distribution.
- Checked for duplicates and categorized features into numerical and categorical for preprocessing.
- Handled missing values using median for numerical and most frequent for categorical.
- Performed feature engineering to create ratio and derived features, and applied scaling & one-hot encoding. 
- Split data into training and testing sets.
- Built machine learning pipelines for Logistic Regression, Random Forest, and XGBoost.
- Evaluated models using ROC-AUC, precision, recall, and threshold tuning for business objectives.
- Deployed the final model using a Streamlit web app for real-time risk prediction.

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


##### 3. Loan Amount vs Default
- Larger loan amounts increase default risk, especially when not supported by proportional income.
- Highlighted the need for credit burden features.

<img width="989" height="499" alt="image" src="https://github.com/user-attachments/assets/682a4795-f017-4287-b5fd-3d01339ad6ea" />

##### 4. Employment Duration vs Default
- Customers with shorter employment history default more often. 
- Longer employment indicates stability and lower risk.
- Used to engineer: Employment Years.

<img width="989" height="499" alt="image" src="https://github.com/user-attachments/assets/5bdf2259-3b22-4521-845b-0e06e982a11e" />

##### 5. Education Level vs Default
- Applicants with lower education have slightly higher default rates.
- Higher education correlates with lower risk of default.

<img width="989" height="499" alt="image" src="https://github.com/user-attachments/assets/08378e09-0251-4485-bd87-6594ba18925d" />
 
##### 6. Family Status vs Default                                                                                                
- Individuals in civil marriages and those who are single have a higher probability of default compared to married or widowed applicants.
- Widows have lowest defaults; unknown status may indicate missing data.

<img width="989" height="499" alt="image" src="https://github.com/user-attachments/assets/ba28792f-56e5-46f4-ae6a-0b178063af56" />

### 🛠️ Data Preprocessing
✔ Median imputation for numerical features

✔ Most-frequent imputation for categorical features

✔ One-hot encoding

✔ Feature scaling

✔ Structured preprocessing pipeline for reproducibility

### 🤖 Models Implemented
1️⃣ Logistic Regression (Baseline & interpretable model)
2️⃣ Random Forest (Non-linear pattern detection)
3️⃣ XGBoost (Best performing model)

The final selected model: XGBoost

### 📊 Model Evaluation

Models were evaluated using:
- ROC-AUC
- Confusion Matrix
- Precision
- Recall
- F1-score

Special business focus:
- Maximizing Recall for defaulters
- Reducing approval of high-risk applicants

### 🔍 Threshold Optimization

The classification threshold was tuned using the precision-recall curve to achieve:

👉 75% recall for defaulters

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

### 📈 Model Explainability
- Permutation Importance was used
- Key risk-driving features identified
- Improved transparency for business stakeholders

### 🚀 Deployment

The final pipeline was:
- Saved using joblib
- Tested using inference validation
- Deployed using Streamlit

  <img width="989" height="499" alt="image" src="https://github.com/user-attachments/assets/be25786e-d987-4dc9-901f-e29a91acb5c0" />


Users can:
- Upload applicant data
- Receive real-time risk prediction
- View default probability

<img width="989" height="499" alt="image" src="https://github.com/user-attachments/assets/7009e87e-4cb4-4268-94f0-6dcabbe3b630" />

<img width="989" height="499" alt="image" src="https://github.com/user-attachments/assets/0d0be858-f576-45a1-9fad-c3d3004b060d" />

