import numpy as np

def func(number):
    matrix = np.eye(100)
    return number * matrix

print(f'OMG large matrix')
print(func(34))