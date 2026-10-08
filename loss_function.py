from nn import NN

class LossFunction:
    def __init__(self, nn : NN, lr : float, h : float):
        self.nn = nn
        self.w_lr = lr
        self.b_lr = lr * 10

        self.h = h

    def loss(self, y : float, t : float) -> float:
        return (abs(t - y) ** 2) / 2

    def _derivative(self, y, t, h : float):
        return (self.loss(y + h, t) - self.loss(y, t)) / h

    def backward(self, x, model_out, label):
        for i in range(self.nn.layer_count):

            mul_flag = 1
            for w in self.nn.w[i+1:self.nn.layer_count]:
                mul_flag *= w

            self.nn.w[i] -= self.w_lr * self._derivative(model_out, label, self.h) * mul_flag * x
            self.nn.b[i] -= self.b_lr * self._derivative(model_out, label, self.h) * mul_flag

            x = self.nn.f(x, i)

        return x
# test
if __name__ == "__main__":

    t = 60
    x = 30
    h = 1e-9
    lr = 1e-5
    nn = NN(5)

    loss_function = LossFunction(nn, lr, h)

    y = nn.forward(x)

    loss = loss_function.loss(y, t)

    loss_function.backward(x, y, t)

    print(f"{y}")
    print(f"{loss}")
