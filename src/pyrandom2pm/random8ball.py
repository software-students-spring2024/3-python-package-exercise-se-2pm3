import random
def random8ball(str):
    try:
        if '?' in str:
            ram = random.randint(0, 3)
            if ram ==0:
                temp = "No"
                return temp
            elif ram ==1:
                temp = "Yes"
                return temp
            else: 
                return "I don't know."
        else:
            return "That was not a question."
    except TypeError:
        return "I don't understand beyond string."

    
