import numpy as np
import math


def correlation(vector_1, vector_2):
    var_1 = np.array(vector_1)
    var_2 = np.array(vector_2)
    # Calculate the mean (average) of each vector
    mean_1 = np.mean(var_1)
    mean_2 = np.mean(var_2)

    # Calculate the covariance, assuming our vectors are samples
    covariance = np.cov(var_1, var_2, ddof=1)[0, 1]

    # Calculate the standard deviation, assuming our vectors are samples
    std_dev_1 = np.std(var_1, ddof=1)
    std_dev_2 = np.std(var_2, ddof=1)

    # Calculate the correlation coefficient
    cor = covariance / (std_dev_1 * std_dev_2)

    return cor


def cosine_similarity(vector_1, vector_2):
    var_1 = np.array(vector_1)
    var_2 = np.array(vector_2)

    dot = np.dot(var_1, var_2)

    mag_1 = math.sqrt(sum(pow(var, 2) for var in var_1))
    mag_2 = math.sqrt(sum(pow(var, 2) for var in var_2))

    cos_sim = dot / (mag_1 * mag_2)

    return cos_sim


def euclidean_distance(vector_1, vector_2):
    var_1 = np.array(vector_1)
    var_2 = np.array(vector_2)
    difference = var_1 - var_2
    squared = difference ** 2
    sum_squares = sum(squared)
    distance = math.sqrt(sum_squares)
    return distance


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

print(correlation(a, b))
print(cosine_similarity(a, b))
print(euclidean_distance(a, b))
