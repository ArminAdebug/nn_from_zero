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


h = 1e-9
# learning rate
w_lr = 1e-6
b_lr = 1e-3

data = generate_train_data(expected_patern, 50000)
for x, label in data:

    y = f(x)

    loss = loss_function(y, label)


    print(f"{y=} | {label=} | {loss=}")

    dL_dy = loss_function_derivative(y, label, h)

    w -= w_lr * dL_dy * x
    b -= b_lr * dL_dy

    w_lr *= 0.99999
    b_lr *= 0.99999

print(w, b)
