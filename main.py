import os
import sys

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

from data_preprocessing import load_and_clean_data
from model import train_model, evaluate_model
from utils import plot_feature_importance

from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    data = load_and_clean_data("data/german_credit_data.csv")
    X = data.drop("Creditability", axis=1)
    y = data["Creditability"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    plot_feature_importance(model, X.columns)
