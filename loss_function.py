

def loss_function(y: float, t:float) -> float:
    return (abs(t - y) ** 2) / 2





# test 
if __name__ == "__main__":
    t = 60
    y = 30

    print(f"{loss_function(y, t)=}")