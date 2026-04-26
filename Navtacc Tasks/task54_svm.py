from sklearn import svm
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

# Dataset: Generated synthetic points for binary classification
X, y = make_blobs(n_samples=50, centers=2, random_state=6)

# Support Vector Machine (SVM) with Linear Kernel
model = svm.SVC(kernel='linear', C=1000)
model.fit(X, y)

print("SVM Model trained successfully.")

# Visualizing the Margin/Hyperplane
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Create grid to plot boundary
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = model.decision_function(xy).reshape(XX.shape)

ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
plt.title("SVM Classification with Hyperplane")
plt.show()
