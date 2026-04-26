from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Dataset: Breast Cancer Diagnosis (Malignant vs Benign)
data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree Model
clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X_train, y_train)

print("Decision Tree Accuracy:", clf.score(X_test, y_test))

# Visualize the Tree
plt.figure(figsize=(12,8))
plot_tree(clf, filled=True, feature_names=data.feature_names)
plt.show()
