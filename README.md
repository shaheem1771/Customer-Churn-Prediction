# 📊 Customer Churn Prediction

A Machine Learning project that predicts customer churn using customer demographics, subscription information, and service usage patterns.

🚀 **Live Demo:** [Try the app here](https://customer-churn-prediction-ni.streamlit.app)

-----

## Project Overview

Customer churn prediction helps businesses identify customers who are likely to discontinue a service. This project applies Machine Learning techniques to analyze customer behavior and predict churn, enabling better customer retention strategies.

-----

## Dataset

**IBM Telco Customer Churn Dataset**

- 7,043 customer records
- 20 features including demographics, services, and billing info
- Target Variable: Churn (Yes / No)

-----

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Random Forest Classifier
- Streamlit (Deployment)
- Google Colab

-----

## Machine Learning Model

**Random Forest Classifier**

```
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

-----

## Model Performance

|Metric               |Score |
|---------------------|------|
|Accuracy             |79.84%|
|Precision (Non-Churn)|0.83  |
|Recall (Non-Churn)   |0.91  |
|F1-Score (Non-Churn) |0.87  |
|Precision (Churn)    |0.66  |
|Recall (Churn)       |0.48  |
|F1-Score (Churn)     |0.56  |

-----

## Project Structure

```
Customer-Churn-Prediction
│
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb   # Main notebook
│
├── reports/
│   └── Customer_Churn_Project_Report.md
│
├── screenshots/
│   ├── Customer_churn_distribution.PNG
│   └── Model_performance_report.PNG
│
├── app.py                                # Streamlit web app
├── model.pkl                             # Trained model
├── requirements.txt                      # Dependencies
└── README.md
```

-----

## Live Demo

The project is deployed as an interactive web app using **Streamlit**.

🔗 <https://customer-churn-prediction-ni.streamlit.app>

- Fill in customer details (contract type, tenure, charges, services)
- Click **Predict Churn**
- Instantly see if the customer will **⚠️ Churn** or **✅ Stay** with confidence score

-----

## Key Findings

- Achieved approximately **80% prediction accuracy**.
- Strong performance in identifying non-churn customers.
- Month-to-month contract customers are more likely to churn.
- Higher monthly charges correlate with increased churn risk.

-----

## Future Improvements

- Hyperparameter tuning for better accuracy
- Cross validation
- Feature engineering
- XGBoost implementation for comparison
- Handle class imbalance with SMOTE

-----

## Author

**Muhammed Shaheem**

B.Tech Computer Science and Engineering

GitHub: [shaheem1771](https://github.com/shaheem1771)
