# 💳 Creditworthiness Prediction using Random Forest

This project predicts whether a person is creditworthy (i.e., likely to repay a loan) based on their financial and personal attributes using a machine learning algorithm — **Random Forest Classifier**.

> Developed as part of an internship assignment at **Celebal Technologies**.

---

## 📁 Project Overview

Credit risk assessment is a crucial part of financial decision-making. This project uses a supervised classification model to predict whether an individual is a **good** or **bad** credit risk based on historical financial data.

---

## 📊 Dataset Information

- **Source**: [UCI German Credit Dataset](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data)
- **Records**: 1000 individuals
- **Attributes**: 20 financial/personal features (age, employment, savings, etc.)
- **Target**: Credit Risk — `1` (Good) or `2` (Bad) → Converted to binary (`1` and `0`)

---

## 🧠 Machine Learning Workflow

We use the **Random Forest Classifier**, a powerful ensemble learning technique that reduces variance and improves predictive accuracy.

### ✔️ Steps Followed:
1. Convert raw data (`german.data`) to CSV format
2. Preprocess the dataset:
   - Label encode categorical columns
   - Convert target to binary
3. Split into training & testing sets (80/20)
4. Train using `RandomForestClassifier` from scikit-learn
5. Evaluate model performance
6. Visualize feature importances

---

## 🧪 Model Performance

- ✅ **Accuracy**: ~80.5%
- 📊 **Confusion Matrix**:

- 🔍 **Classification Report**:
- Precision for class `1`: 82%
- Precision for class `0`: 74%

📌 **Insight**:  
The model performs well, especially for predicting good credit risk (`1`). It slightly underperforms on class `0` due to class imbalance, which is a common challenge in such datasets.

---

## 🚀 How to Run the Project

### 🛠️ Setup

```bash
# Clone the repository
git clone https://github.com/AayushKulkarni36/Creditworthiness-Prediction-using-Random-Forest.git
cd Creditworthiness-Prediction-using-Random-Forest

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

Project/
│
├── data/
│   ├── german.data               # Raw input data
│   ├── german_credit_data.csv    # Cleaned CSV output
│   └── datacsv.py                # Script to convert raw data
│
├── src/
│   ├── data_preprocessing.py     # Preprocessing functions
│   ├── model.py                  # Model training & evaluation
│   └── utils.py                  # Visualization
│
├── main.py                       # Entry point
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

# 👨‍💻 Author
Ayush Kulkarni

Final Year B.E. (Information Technology)

Intern at Celebal Technologies

GitHub: AayushKulkarni36
