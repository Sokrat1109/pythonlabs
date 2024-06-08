import numpy as np
from spicy.stats import multivariate_normal
import time

def task1():
    a = np.genfromtxt("1.txt", delimiter=",")

    max_ = a.max()
    min_ = a.min()
    sum_ = a.sum()


    print(max_, min_, sum_)

def task2():

    b = np.array([1, 1, 1, 2, 2, 2, 4])

    nums = np.empty(0)
    counts = np.empty(0)
    for i in b:
        if not(i in nums):
            nums = np.append(nums, i)

    counter = 0
    for i in nums:
        counter = 0
        for j in b:
            if i == j:
                counter += 1

        counts = np.append(counts, counter)

    print(nums, counts)

def task3():

    a = np.random.normal(size=40)
   # b = a[:5, : : ]
    a.shape = (10, 4)
   # b.shape = (5, 4)
    min_ = a.min()
    max_ = a.max()
    middle_ = a.mean()

    b = a[:5, : : ]

    print('a = ', a)
    print('min = ', min_, 'max = ', max_, 'middle = ', middle_)
    print('b = ', b)

def task4():
    x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

    max_ = 0
    for i in range(1, len(x)):
        if x[i-1] == 0:
            max_ = max(max_, x[i])
    print(max_)

def task5():
    def log_multivariate_normal_density(X, m, C):
        N, D = X.shape
        X_minus_m = X - m
        C_inv = np.linalg.inv(C)
        log_det_C = np.linalg.slogder(C) [1]
        log_density = -0.5 * (np.sum(np.dot(X_minus_m, C_inv) * X_minus_m, axis=1) + D * np.log(2 * np.pi) + log_det_C)
        return log_density

    np.random.seed(0)
    N = 10000
    D = 5
    X = np.random.randn(N, D)
    m = np.random.randn(D)
    C = np.random.randn(D, D)
    C = np.dot(C, C.T)

    start_time = time.time()
    log_density_custom = log_multivariate_normal_density(X, m, C)
    custom_time = time.time()

    start_time = time.time()
    log_density_scipy = multivariate_normal.logpdf(X, mean=m, cov=C)
    scipy_time = time.time() - start_time

    print(f"Custom implementation time: {custom_time:.6f} seconds")
    print(f"Scipy implementation time: {scipy_time:.6f} seconds")
    print(f"Difference in result: {np.max(np.abs(log_density_custom = log_density_scipy)):.6e}")


def task6():
    a = np.arange(16).reshape(4, 4)

    print('a1 = ', a)

    a[[0, 2]] = a[[2, 0]]

    print('a2 = ', a)

def task7():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='object')

    d = {}
    for k in iris:
        #print(k[4])
        if k[4] in d:
            d[k[4]] += 1
        else:
            d[k[4]] = 1

    for i in d.keys():
        print(i, d[i])

def task8():
    x = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
    print(np.nonzero(x)[0])