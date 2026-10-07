from typing import Callable

from math_utils import differential, derivative

w = 3
b = 5
def f(x : float) -> float:
    return w * x + b





x = 20
h = 0.00000000001
y = f(x)


dx = x + h
dw = w + h
db = b + h

dy = differential(f, x, h)

print(f"{dy=}")

print("#" * 5)

print(f"{x=}")
print(f"{w=}")
print(f"{b=}")
print(f"{y=}")

print("#" * 5)

#print(f"{dy/dw=}")
#print(f"{dy/dx=}")
print(f"{differential(f, b, h)/db=}")
print(derivative(f, b, h))


