import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_importance(model, feature_names):
    importances = model.feature_importances_
    indices = sorted(range(len(importances)), key=lambda i: importances[i], reverse=True)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=[importances[i] for i in indices], y=[feature_names[i] for i in indices])
    plt.title("Feature Importances")
    plt.tight_layout()
    plt.show()
