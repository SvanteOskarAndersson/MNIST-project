import numpy as np

def func(number):
    matrix = np.eye(100)
    return number * matrix

print(f'OMG large matrix')
print(func(34))


def func_2(number):
    sqrt = np.sqrt(number)
    return sqrt

    