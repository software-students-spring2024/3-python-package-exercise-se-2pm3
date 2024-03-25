import random
def randomDice(num_dice, num_sides):
    total = 0
    for i in range(num_dice):
        random_number = random.randint(1, num_sides)
        total += random_number
    return total
