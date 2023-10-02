import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

cubic_df = pd.read_csv('HW2_nonlinear_data.csv')

initial_coeffs = [1, -1, 1, 1]
x = cubic_df.iloc[:, 0]
y = cubic_df.iloc[:, 1]

def cubic_func(coeffs, x):
    """Coeffs defines the function, returns the value at the x value"""
    a = coeffs[0] * (x**3)
    b = coeffs[1] * (x**2)
    c = coeffs[2] * x
    d = coeffs[3]
    y = a + b + c + d
    return y

def cubic_gradient_calc(init_coefficients, xs, ys, lr):
    """Calculates updated gradient from partial derivatives"""
    a = []
    b = []
    c = []
    n = len(xs)

    predicted_ys = cubic_func(init_coefficients, xs)

    # calculate gradients with respect to each coefficient
    d_a = (-2/n) * sum((x**3) * (y - predicted_ys))
    d_b = (-2/n) * sum((x**2) * (y - predicted_ys))
    d_c = (-2/n) * sum(x*(y - predicted_ys))
    d_d = (-2/n) * sum(y - predicted_ys)

    a_new = init_coefficients[0] - lr * d_a
    b_new = init_coefficients[1] - lr * d_b
    c_new = init_coefficients[2] - lr * d_c
    d_new = init_coefficients[3] - lr * d_d

    new_coeffs = (a_new, b_new, c_new, d_new)
    new_y_predictions = cubic_func(new_coeffs, x)

    return new_coeffs, new_y_predictions

def gradient_descent(epochs, lr):

    updated_coeffs = initial_coeffs
    for i in range(epochs):
        update = cubic_gradient_calc(updated_coeffs, x, y, lr)
        updated_coeffs = update[0]

    return update[0], update[1]

grad_descent = gradient_descent(10000, .000001)
plot.figure(figsize=(20,10))
plot.plot(x, y, 'g+', label = 'original data')
plot.plot(x, grad_descent[1], 'b.', label = 'final_prediction')
plot.title('Original vs Final prediction after Gradient Descent')
plot.legend(loc="lower right")
plot.show()


# plot.figure(figsize=(20,10))
# plot.title("Test cubic grad")
# plot.plot(x, y, 'g+', label = 'original data')
# plot.plot(x, y_bar, 'ro', label = 'naive initial coeffs')
# plot.plot(x, new_y_bar, 'b.', label = 'updated gradient coeffs')
# plot.title('Original model, initial coeffs then updated prediction with lower loss')
# plot.legend(loc="lower right")
# plot.show()
