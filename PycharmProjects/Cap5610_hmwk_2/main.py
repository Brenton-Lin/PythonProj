import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

lin_df = pd.read_csv('HW2_linear_data.csv')

# axis setup
x = lin_df.iloc[:, 0]
y = lin_df.iloc[:, 1]

# linear model init
initial_m = 0
initial_c = 0
initial_coeffs = [initial_m, initial_c]
# Gradient descent options
learning_rate = 0.0001
epochs = 1000
n = float(len(x))


def linear_func(coeffs, x):
    y = coeffs[0] * x + coeffs[1]
    return y


def gradient_calc(coeffs, xs, lr):
    predicted_ys = linear_func(coeffs, xs)

    D_m = (-2 / n) * sum(xs * (y - predicted_ys))  # Partial derivative m
    D_c = (-2 / n) * sum(y - predicted_ys)  # Partial derivative c

    # Update thetas
    m_new = coeffs[0] - lr * D_m
    c_new = coeffs[1] - lr * D_c
    new_coeffs = [m_new, c_new]
    new_ys = linear_func(new_coeffs, xs)

    return new_coeffs, new_ys

# Gradient Descent
def linear_gradient_descent(coeffs, lr):

    # set initial coeffs
    updated_coeffs = coeffs
    for i in range(epochs):
        update = gradient_calc(updated_coeffs, x, lr)
        updated_coeffs = update[0]

    return update


gd = linear_gradient_descent(initial_coeffs, learning_rate)
print(f"Final Coeffs: m = {gd[0][0]} c = {gd[0][1]}")
plot.scatter(x, y, label = "Initial data")
plot.plot(x, gd[1], color = 'red', label = "Final prediction line")
plot.show()

