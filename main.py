from typing import Callable
import random

from math_utils import differential, derivative
from loss_function import loss_function, loss_function_derivative
from data_set import generate_train_data

w = 3
b = 5
def f(x : float) -> float:
    return w * x + b


def expected_patern(x):
    return 5 * x + 20


h = 0.0000001
# learning rate
lr = 0.001

data = generate_train_data(expected_patern, 500)
for x, label in data:

    y = f(x)

    loss = loss_function(y, label)


    
    print(f"{y=} | {label=} | {loss=}") 

    dL_dy = loss_function_derivative(y, label, h)

    w -= lr * dL_dy * x
    b -= lr * dL_dy