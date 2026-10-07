
import random

def generate_train_data(f, count : int):


    data : list[list[float, float]] = []

    for i in range(count):

        data.append((i, f(i)))

    random.shuffle(data)

    return data