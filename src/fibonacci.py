from pow_2x2_matrix import *

def fib1(n):

    if n == 1 or n == 0:
        return 1

    return fib1(n-1) + fib1(n-2)

def fib2(n):

    fn = 1
    f_1, f_2 = 1, 1

    for i in range(n - 1):
        fn = f_1 + f_2

        f_2 = f_1
        f_1 = fn

    return fn


def fib3(n):

    base_matrix = [[0,1], [1,1]]

    n_power_matrix = pow_2x2_matrix(base_matrix, n)

    fn = n_power_matrix[0][0] + n_power_matrix[0][1] 

    return fn