
def derivative(f, x, h):
    return (f(x + h) - f(x)) / h



def f(x):
    return 2 * x ** 3





x = 20
h = 0.00000000001
a = 6 * x ** 2
d = derivative(f, x, h)

print(f"{a=}")
print(f"{d=}")
print(abs(a - d))



