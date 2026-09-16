
# Simple Linear Regression
# A shop records its monthly advertising expenditure and minthly sales.
# Fit a simple linear regression model and predict sales when advertising expenditure is Rs. 7000
# Advertising (X) = {2000, 3000, 4000, 5000, 6000}
#Sales (Y) = {25000, 30000, 34000, 40000, 45000}

import numpy as np
from matplotlib import pyplot as plt

# --------------------------------------------------
# 1. Input the dataset
# --------------------------------------------------

X = np.array([2000, 3000, 4000, 5000, 6000])
Y = np.array([25000, 30000, 34000, 40000, 45000])

# Number of observations
n = len(X)

# --------------------------------------------------
# 2. Calculate the mean of X and Y
# --------------------------------------------------

X_mean = np.mean(X)
Y_mean = np.mean(Y)

# --------------------------------------------------
# 3. Calculate slope (b1)
# --------------------------------------------------

# b1 = np.sum((X - X_mean) * (Y - Y_mean)) /  np.sum((X - X_mean) ** 2)
 
b1 = (n*np.sum(X*Y)-np.sum(X)*np.sum(Y))/(n*np.sum(X*X)-(np.sum(X)*np.sum(X)))

# --------------------------------------------------
# 4. Calculate intercept (b0)
# --------------------------------------------------

b0 = Y_mean - b1 * X_mean

# --------------------------------------------------
# 5. Display the regression equation
# --------------------------------------------------

print("Simple Linear Regression")
print("------------------------")

print("Slope (b1)     =", b1)
print("Intercept (b0) =", b0)


print("\nRegression Equation:")
print("Y =", b0, "+", b1, "X")

# --------------------------------------------------
# 6. Predict sales for Rs. 7000 advertising
# --------------------------------------------------

advertising = 7000

predicted_sales = b0 + b1 * advertising

print("\nAdvertising Expenditure = Rs.", advertising)
print("Predicted Sales = Rs.", predicted_sales)

# --------------------------------------------------
# 7. Calculate predicted values for all observations
# --------------------------------------------------

Y_pred = b0 + b1 * X

print("\nActual Sales vs Predicted Sales")
print("--------------------------------")

for i in range(n):
    print("Advertising:", X[i],
          "Actual Sales:", Y[i],
          "Predicted Sales:", Y_pred[i])

# --------------------------------------------------
# 8. Visualize the data and regression line
# --------------------------------------------------

plt.scatter(X, Y, label="Actual Data")

plt.plot(X, Y_pred, 'g*',label="Regression Line",linestyle='-')

plt.scatter(
    advertising,
    predicted_sales,
    marker="*",
    s=150,
    label="Prediction at Rs. 7000"
)

plt.xlabel("Advertising Expenditure (Rs.)")
plt.ylabel("Sales (Rs.)")
plt.title("Simple Linear Regression: Advertising vs Sales")

plt.legend()
plt.grid(True)
plt.savefig("Figures/pgm2-LinearRegression.png")
plt.show()

#--------------------------------------------------
# Calculate MAE manually
# --------------------------------------------------

# Calculate absolute errors
absolute_errors = np.abs(Y - Y_pred)

# Calculate MAE
MAE = np.sum(absolute_errors) / n

print("\nMean Absolute Error (MAE) =", MAE)


# --------------------------------------------------
# 2. Calculate R-squared and RMSE manually
# --------------------------------------------------

# Calculate mean of actual values
Y_mean = np.mean(Y)

# Residual Sum of Squares (SS_res)
SS_res = np.sum((Y - Y_pred) ** 2)
print("RMSE", np.sqrt(SS_res/n))


# Total Sum of Squares (SS_tot)
SS_tot = np.sum((Y - Y_mean) ** 2)

# R-squared
R2 = 1 - (SS_res / SS_tot)
print("R-squared =", R2)



