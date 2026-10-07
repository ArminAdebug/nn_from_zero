from typing import Callable

from math_utils import differential

w = 3

def f(x : float) -> float:
    return w * x





x = 20
h = 0.00000000001

dy = differential(f, x, h)

print(f"{dy=}")
print(f"{x=}")
print(f"{dy/w=}")



