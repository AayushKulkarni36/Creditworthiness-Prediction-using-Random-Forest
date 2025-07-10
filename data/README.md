# 💳 Creditworthiness Prediction using Random Forest

This project predicts whether a person is creditworthy (i.e., likely to repay a loan) based on their financial and personal attributes using a machine learning algorithm — Random Forest Classifier.

It was developed as part of an internship assignment at **Celebal Technologies**.

---

## 📁 Project Overview

Credit risk assessment is a crucial part of financial decision-making. This project uses a classification model to predict whether an individual is a **good** or **bad** credit risk based on historical financial data.

---

## 📊 Dataset Information

- **Source**: [UCI Machine Learning Repository – German Credit Data](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data)
- **Size**: 1000 records
- **Attributes**: 20 features related to credit history, income, employment status, savings, age, and more.
- **Target Variable**:
  - `1` → Good Credit Risk
  - `2` → Bad Credit Risk (converted to `0` in the code for binary classification)

  

---

## 🧠 Machine Learning Approach

We use the **Random Forest Classifier**, a robust ensemble learning technique that combines multiple decision trees to improve prediction accuracy and control overfitting.

### Steps Followed:
1. Data preprocessing and encoding
2. Feature-target separation
3. Train-test split (80:20)
4. Model training using Random Forest
5. Evaluation with:
   - Accuracy
   - Confusion Matrix
   - Precision, Recall, F1-score
6. Feature importance visualization

---

## 🧪 Model Performance

✅ **Test Accuracy**: ~80.5%

📌 **Insights**:
- Performs well in identifying good credit risks.
- Confusion matrix and classification report show balanced performance.
- Model may be slightly biased toward class `1` due to class imbalance.

---

## 🚀 How to Run

### 1️⃣ Clone the Repository
```bash
cd your/folder/path
