Customer Churn Prediction

A Machine Learning project that predicts customer churn using customer demographics, subscription details, and service usage data. The objective is to identify customers who are likely to discontinue a service, enabling businesses to improve customer retention strategies.

⸻

Overview

Customer churn prediction is a critical business problem in industries such as telecommunications, banking, and subscription-based services. This project applies supervised machine learning techniques to analyze customer behavior and classify customers as either Churn or Non-Churn.

The model was developed using the Telco Customer Churn dataset and implemented in Python using Scikit-learn.

⸻

Key Features

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Categorical feature encoding
* Customer churn visualization
* Random Forest Classification
* Performance evaluation using classification metrics
* Project documentation and result visualization

⸻

Dataset

Dataset: Telco Customer Churn Dataset

Records: 7,043 Customers

Features: 21 Attributes

Target Variable: Churn

The dataset contains customer demographic information, service subscriptions, contract details, billing information, and account tenure.

⸻

Technology Stack

Category	Tools
Programming Language	Python
Data Analysis	Pandas, NumPy
Visualization	Matplotlib
Machine Learning	Scikit-learn
Development Environment	Google Colab
Version Control	Git & GitHub

⸻

Machine Learning Pipeline

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Encoding
5. Train-Test Split (80:20)
6. Model Training
7. Performance Evaluation
8. Result Visualization

⸻

Model

Random Forest Classifier

RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

⸻

Performance

Metric	Score
Accuracy	79.84%
Precision (Non-Churn)	0.83
Recall (Non-Churn)	0.91
F1-Score (Non-Churn)	0.87
Precision (Churn)	0.66
Recall (Churn)	0.48
F1-Score (Churn)	0.56

⸻

Project Structure

Customer-Churn-Prediction
│
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb
│
├── reports/
│   └── Customer_Churn_Project_Report.md
│
├── screenshots/
│   ├── Customer_churn_distribution.PNG
│   └── Model_performance_report.PNG
│
├── requirements.txt
└── README.md

⸻

Results

Customer Churn Distribution

Model Performance Report

⸻

Key Findings

* Achieved approximately 80% classification accuracy.
* Demonstrated strong performance in identifying non-churn customers.
* Highlighted the impact of customer contracts, service subscriptions, and billing patterns on churn behavior.
* Revealed class imbalance as a challenge in churn prediction.

⸻

Future Enhancements

* Hyperparameter tuning using GridSearchCV
* Class balancing using SMOTE
* Model comparison with XGBoost and Gradient Boosting
* Web deployment using Streamlit or Flask
* Real-time customer churn prediction

⸻

Author

Muhammed Shaheem

B.Tech Computer Science and Engineering

Machine Learning Project – 2026
