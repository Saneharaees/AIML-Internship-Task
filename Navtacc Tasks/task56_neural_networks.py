from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

# Dataset: Handwritten Digits (Mini-MNIST)
digits = load_digits()
X, y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Neural Network (Multi-layer Perceptron)
# 2 hidden layers with 10 neurons each
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=500)
mlp.fit(X_train, y_train)

print("Neural Network Accuracy:", mlp.score(X_test, y_test))
