import numpy as np

X = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]).reshape(-1, 1)
y = np.array([5, 9, 15, 21, 29, 35, 39, 43, 51, 59, 65, 69, 75, 79, 85, 91, 95, 101, 105, 111, 115, 119, 125, 129, 135, 139, 145, 151, 155, 161]).reshape(-1, 1)

def simple_linear_regression(X, y):
    # Mean of X and y
    X_mean = np.mean(X)
    y_mean = np.mean(y)

    # Calculate the slope (m) and the intercept (c) of the line
    numerator = np.sum((X - X_mean) * (y - y_mean))
    denominator = np.sum((X - X_mean) ** 2)
    m = numerator / denominator
    c = y_mean - m * X_mean

    return m, c

# Fitting the model
m, c = simple_linear_regression(X, y)

# Predictions
y_pred = m * X + c

# Root Mean Squared Error (RMSE)
rmse = np.sqrt(np.mean((y_pred - y) ** 2))
print("Root Mean Squared Error (RMSE):", rmse)

# Plotting the data and the regression line
import matplotlib.pyplot as plt

plt.scatter(X, y, label='Data')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
