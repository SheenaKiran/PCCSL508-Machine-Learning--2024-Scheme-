# The following data give the marks obtained by students based on hours studied (X1) and
# attendance percentage (X2). Fit a multiple linear regression model using matrix method and
# predict the marks for a student who studies 5 hours and has 88% attendance.
#  Hours studeied (X1) = {2, 3,4 ,5 6}
# attendance percentage (X2) = {72, 74, 82, 84, 91 }
# Marks(Y) = { 50, 55, 62, 68, 75 }

import numpy as np

# Input data
X1 = np.array([2, 3, 4, 5, 6])
X2 = np.array([72, 74, 82, 84, 91])
Y = np.array([50, 55, 62, 68, 75])
n = len(X1)


# ------------------------------------------------
# Step 1: Construct Design Matrix
# ------------------------------------------------
X = np.column_stack((np.ones(len(X1)), X1, X2))
print("Matrix X:")

# ------------------------------------------------
# Step 2: Matrix Method
# beta = (X^T X)^-1 X^T Y
# ------------------------------------------------

XT = X.T
beta = np.linalg.inv(XT @ X) @ XT @ Y

# Regression coefficients
b0, b1, b2 = beta

print("\nRegression coefficients:")
print("b0 =", b0)
print("b1 =", b1)
print("b2 =", b2)

# Regression equation
print("\nMultiple Linear Regression Equation:")
print(f"Y = {b0:.4f} + ({b1:.4f})X1 + ({b2:.4f})X2")

# ------------------------------------------------
# Step 3: Calculate predicted values
# ------------------------------------------------
# Predict marks for X1 = 5 hours and X2 = 88% attendance
X_new = np.array([1, 5, 88])

predicted_marks = X_new @ beta

print("\nPrediction:")
print("Hours Studied =", X_new[1])
print("Attendance =", X_new[2], "%")
print(f"Predicted Marks = {predicted_marks:.2f}")

# Calculate predicted values for all input values


Y_pred = X @ beta

print("\nActual and Predicted Marks:")
for actual, predicted in zip(Y, Y_pred):
    print(f"Actual = {actual:.2f}, Predicted = {predicted:.2f}")


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
print("Residual Sum of Squares (SS_res) =", round(SS_res, 4))


# Total Sum of Squares (SS_tot)
SS_tot = np.sum((Y - Y_mean) ** 2)

# R-squared
R2 = 1 - (SS_res / SS_tot)
print("R-squared =", R2)



