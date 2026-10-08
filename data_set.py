
import random

def generate_train_data(f, count : int):


    data : list[list[float, float]] = []

    for i in range(count):
        x = random.random()
        data.append((x, f(x)))

    random.shuffle(data)

    return data
