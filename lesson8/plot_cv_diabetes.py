"""
====================================
Plotting Cross-Validated Predictions
====================================

This example shows how to use `cross_val_predict` with 
Lasso (least absolute shrinkage and selection operator)
to visualize prediction errors.

"""
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()
X = diabetes.data[:150]
y = diabetes.target[:150]
lasso = linear_model.Lasso()

print('Number of instances: %d' % (diabetes.data.shape[0]))

# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validated:
y_pred = cross_val_predict(lasso, X, y, cv=3)

fig, ax = plt.subplots()
ax.scatter(y, y_pred)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k-', lw=2)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
