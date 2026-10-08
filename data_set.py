
import random

def generate_train_data(f, count : int):


    data : list[list[float, float]] = []

    for i in range(count):

        data.append((i / 100, f(i / 100)))

    random.shuffle(data)

    return data
