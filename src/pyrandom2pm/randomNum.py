import random
def randomNum(num):
    if num<=0:
        raise ValueError
    else:
        ret = random.randint(1, num)
        return ret
