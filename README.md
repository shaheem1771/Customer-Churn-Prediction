# Customer Churn Prediction

A Machine Learning project that predicts customer churn using customer demographics, subscription information, and service usage patterns.

---

## Project Overview

Customer churn prediction helps businesses identify customers who are likely to discontinue a service. This project applies Machine Learning techniques to analyze customer behavior and predict churn, enabling better customer retention strategies.

---

## Dataset

The dataset contains customer demographic, subscription, and billing information used to predict customer churn.

Target Variable:

- Churn (Yes / No)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab

---

## Machine Learning Model

**Random Forest Classifier**

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

---

## Model Performance

| Metric | Score |
|----------|----------|
| Accuracy | 79.84% |
| Precision (Non-Churn) | 0.83 |
| Recall (Non-Churn) | 0.91 |
| F1-Score (Non-Churn) | 0.87 |
| Precision (Churn) | 0.66 |
| Recall (Churn) | 0.48 |
| F1-Score (Churn) | 0.56 |

---

## Project Structure

```text
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
```

---

## Results

- [Customer Churn Distribution](screenshots/Customer_churn_distribution.PNG)
- [Model Performance Report](screenshots/Model_performance_report.PNG)


---

## Key Findings

- Achieved approximately 80% prediction accuracy.
- Strong performance in identifying non-churn customers.
- Moderate performance in identifying churn customers.
- Demonstrates the application of Machine Learning in customer retention analysis.

---

## Future Improvements

- Hyperparameter Tuning
- Cross Validation
- Feature Engineering
- XGBoost Implementation
- Streamlit Deployment

---

## Author

**Muhammed Shaheem**

B.Tech Computer Science and Engineering

GitHub: https://github.com/shaheem1771
