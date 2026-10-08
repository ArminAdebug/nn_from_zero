import random


class NN:
    def __init__(self, l: int):

        self.layer_count = l

        self.w = [random.random() for _ in range(l)]
        self.b = [random.random() for _ in range(l)]

    def f(self, x, i):
        return self.w[i] * x + self.b[i]

    def forward(self, x):

        for i in range(self.layer_count):
            x = self.f(x, i)

        return x
