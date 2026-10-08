from typing import Callable
import random

from math_utils import differential, derivative
from data_set import generate_train_data
from loss_function import LossFunction
from nn import NN

def expected_patern(x):
    return 3 * x + 2


lr = 1e-3
h = 1e-9
model = NN(2)
loss_function = LossFunction(model, lr, h)

max_loss = 0
min_loss = 100000000

data = generate_train_data(expected_patern, 500000)
for x, label in data:

    y = model.forward(x)

    loss = loss_function.loss(y, label)

    min_loss = min(loss, min_loss)
    max_loss = max(loss, min_loss)

    loss_function.backward(x, y, label)
    if random.randint(1, 50) == 1:
        print(f"{y:.2f}|{label:.2f}|{loss=}")

print(model.w)
print(model.b)
print(max_loss)
print(min_loss)

test = 3
print(f"{expected_patern(test)=}")
print(f"{model.forward(test)=}")
