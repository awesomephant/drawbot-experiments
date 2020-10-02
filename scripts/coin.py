import random
def coin(p=.5):
    v = random.random()
    if v < p:
        return True
    return False