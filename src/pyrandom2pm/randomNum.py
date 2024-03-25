import random
def randomNum(num):
    if num<=1:
        raise ValueError
    else:
        ret = random.randint(1, num)
        return ret
