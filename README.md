# Fraud Detection in Credit Card Transactions

This project aims to detect fraudulent credit card transactions using a combination of anomaly detection techniques and machine learning.

---

## 🧠 Objective

The goal is to build a model that can identify fraudulent transactions based on patterns in the data. Since fraud cases are rare and different from regular ones, we use both unsupervised and supervised learning methods to improve accuracy.

---

## 🔧 Tools and Libraries Used

- Python
- Pandas
- Scikit-learn
- XGBoost
- Matplotlib, Seaborn
- Streamlit or Flask for the user interface

---

## 📂 Dataset

We used the [Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) from Kaggle. It contains transactions made by European cardholders in September 2013, with features like V1 to V28 (PCA components), Amount, and Time. The `Class` column indicates whether a transaction is fraudulent (1) or not (0).

---

## ⚙️ How Fraud is Detected

We use two main approaches:

### 1. Anomaly Detection

- **Isolation Forest**: Detects anomalies by randomly partitioning the data. Fraud cases tend to get isolated faster.
- **Local Outlier Factor (LOF)**: Compares the local density of each point with its neighbors. Fraudulent transactions usually have much lower density.

These models help identify transactions that look unusual, even if we don't have labels.

### 2. Supervised Learning

- **XGBoost Classifier**: After preprocessing and balancing the data, we train a model using the known fraud labels. XGBoost is chosen for its performance on imbalanced datasets.

---

## 🔬 Steps Followed

1. **Data Preprocessing**
   - Dropped irrelevant columns
   - Scaled features
   - Handled class imbalance (e.g., undersampling or SMOTE)

2. **Anomaly Detection**
   - Applied Isolation Forest and LOF
   - Evaluated with ROC-AUC score

3. **Model Training**
   - Trained XGBoost classifier on the cleaned dataset
   - Evaluated using confusion matrix, precision, recall, and ROC curve

4. **Dashboard Creation**
   - Built an interface using Streamlit/Flask to input new transaction data and get predictions

---

## 📈 Evaluation

- Confusion Matrix
- ROC Curve
- AUC Score
- Feature Importance from XGBoost


