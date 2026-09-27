# A company's monthly sales depend on advertising expenditure 
# (X1). Fit a multiple linear regression model using gradient descent
# method and estimate the sales when advertising expenditure is Rs. 22,000.
# Advertising expenditure(X1) = {10, 15, 20, 25, 30}
# Monthly Sales (Y) = {50, 65, 78, 90, 105}


import numpy as np

# Advertising expenditure (₹'000)
X = np.array([10, 15, 20, 25, 30], dtype=float)

# Sales (₹'000)
Y = np.array([50, 65, 78, 90, 105], dtype=float)
n = len(X)

# Initialize parameters
b0 = 0.0
b1 = 0.0

# Learning rate
alpha = 0.001

# Number of iterations
iterations = 10000

# Number of training examples
m = len(X)

# Gradient Descent
for i in range(iterations):

    # Predicted sales
    Y_pred = b0 + b1 * X

    # Calculate gradients
    db0 = (-2 / m) * np.sum(Y - Y_pred)
    db1 = (-2 / m) * np.sum(X * (Y - Y_pred))

    # Update parameters
    b0 = b0 - alpha * db0
    b1 = b1 - alpha * db1

# Display model parameters
print("Intercept (b0) =", b0)
print("Slope (b1) =", b1)

# Prediction for advertising expenditure = ₹22,000
# Since X is in ₹'000, ₹22,000 = 22
X_new = 22

predicted_sales = b0 + b1 * X_new

print("\nRegression Equation:")
print("Sales =", b0, "+", b1, "* Advertising")

print("\nAdvertising expenditure = ₹22,000")
print("Predicted Sales =", predicted_sales, "₹'000")
print("Predicted Sales = ₹", predicted_sales * 1000)


#--------------------------------------------------
# Calculate MAE manually
# --------------------------------------------------

# Calculate absolute errors
absolute_errors = np.abs(Y - Y_pred)

# Calculate MAE
MAE = np.sum(absolute_errors) / n

print("\nMean Absolute Error (MAE) =", round(MAE, 4))


# --------------------------------------------------
# 2. Calculate R-squared and RMSE manually
# --------------------------------------------------

# Calculate mean of actual values
Y_mean = np.mean(Y)

# Residual Sum of Squares (SS_res)
SS_res = np.sum((Y - Y_pred) ** 2)
print("RMSE =", np.sqrt(SS_res/n))


# Total Sum of Squares (SS_tot)
SS_tot = np.sum((Y - Y_mean) ** 2)

# R-squared
R2 = 1 - (SS_res / SS_tot)
print("R-squared =", R2)



