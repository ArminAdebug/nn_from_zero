from typing import Callable

def derivative(f : Callable[[float], float], x : float, h : float):
    return (f(x + h) - f(x)) / h

def differential(f : Callable[[float], float], x : float, h : float):
    dy = derivative(f, x, h) * (x + h)

    return dy