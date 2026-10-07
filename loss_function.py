
def loss_function(y: float, t :float) -> float:
    return (abs(t - y) ** 2) / 2


def loss_function_derivative(y, t, h):
    return (loss_function(y + h, t) - loss_function(y, t)) / h

# test 
if __name__ == "__main__":

    t = 60
    y = 30
    h = 0.00000001

    d = loss_function_derivative(y, t, h)

    print(f"{d}")