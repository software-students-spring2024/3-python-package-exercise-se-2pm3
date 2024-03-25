import random
def randomCoin(num_flip):
    lst =[]
    for i in range(num_flip):
        head = random.randint(0,1)
        if head == 0:
            lst.append("Tail")
        elif head ==1:
            lst.append("Head")
    ret = " ".join(j for j in lst)
    return ret

