Customer Churn Prediction Using Machine Learning

1. Abstract

Customer churn refers to customers discontinuing a company’s services. Predicting churn is important because retaining existing customers is often more cost-effective than acquiring new ones. This project develops a Machine Learning model to predict customer churn using customer demographic information, subscription details, and service usage patterns.

The project uses the Telco Customer Churn dataset and applies data preprocessing, label encoding, train-test splitting, and a Random Forest Classifier to classify customers as churned or non-churned.

⸻

2. Objectives

* Analyze customer behavior and subscription data.
* Identify factors influencing customer churn.
* Build a machine learning model for churn prediction.
* Evaluate model performance using classification metrics.
* Visualize customer churn distribution.

⸻

3. Dataset Information

Dataset: Telco Customer Churn Dataset

Total Records: 7043

Total Features: 21

Target Variable:

* Churn
    * Yes = Customer left the service
    * No = Customer retained the service

Important Features:

* Gender
* SeniorCitizen
* Partner
* Dependents
* Tenure
* PhoneService
* InternetService
* OnlineSecurity
* TechSupport
* Contract
* PaymentMethod
* MonthlyCharges
* TotalCharges

⸻

4. Methodology

Step 1: Data Collection

The dataset was imported using Pandas from a CSV file.

Step 2: Data Exploration

Operations performed:

* Display first five rows
* Check dataset dimensions
* Check missing values
* Analyze churn distribution

Results:

* Number of customers: 7043
* Missing values: 0

Step 3: Data Preprocessing

Performed preprocessing steps:

1. Removed irrelevant data.
2. Encoded categorical features using Label Encoding.
3. Converted data into machine-readable format.
4. Split dataset into training and testing sets.

Training Set:

* 5634 records

Testing Set:

* 1409 records

Train-Test Ratio:

* 80:20

⸻

5. Machine Learning Model

Algorithm Used:

Random Forest Classifier

Parameters:

* n_estimators = 100
* random_state = 42

Reasons for Choosing Random Forest:

* Handles categorical data effectively.
* Reduces overfitting.
* Provides good classification performance.
* Easy to implement and interpret.

⸻

6. Results

Accuracy

Model Accuracy:

79.84%

Approximate Accuracy:

80%

⸻

Classification Report

Class	Precision	Recall	F1-Score
Non-Churn (0)	0.83	0.91	0.87
Churn (1)	0.66	0.48	0.56

Macro Average:

* Precision: 0.74
* Recall: 0.70
* F1-Score: 0.71

Weighted Average:

* Precision: 0.78
* Recall: 0.80
* F1-Score: 0.79

⸻

7. Visualization

Customer Churn Distribution

Observations:

* Majority of customers did not churn.
* Churned customers represent a smaller portion of the dataset.
* Dataset is slightly imbalanced.

Non-Churn Customers:

5174

Churn Customers:

1869

⸻

8. Key Findings

1. The model achieved approximately 80% accuracy.
2. Non-churn customers were predicted effectively.
3. Churn customer prediction remains challenging due to class imbalance.
4. Contract type and service usage significantly influence churn.
5. Customer retention strategies can be developed using these predictions.

⸻

9. Limitations

* Dataset is moderately imbalanced.
* More advanced feature engineering was not performed.
* Hyperparameter tuning was not extensively explored.
* External customer behavior factors were unavailable.

⸻

10. Future Enhancements

* Apply SMOTE for class balancing.
* Perform GridSearchCV hyperparameter tuning.
* Compare multiple algorithms:
    * XGBoost
    * Gradient Boosting
    * Support Vector Machine
    * Logistic Regression
* Deploy as a web application using Flask or Streamlit.
* Integrate real-time churn prediction.

⸻

11. Conclusion

This project successfully developed a Machine Learning-based Customer Churn Prediction system using the Random Forest algorithm. The model achieved approximately 80% prediction accuracy and demonstrated strong performance in identifying non-churn customers. The project highlights the importance of machine learning in customer retention strategies and provides a foundation for future improvements and deployment.

⸻

Developed By

Muhammed Shaheem

B.Tech Computer Science and Engineering

Machine Learning Project

2026
