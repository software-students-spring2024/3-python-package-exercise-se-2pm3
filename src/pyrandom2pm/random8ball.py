import random
def random8ball(strn):
    try:
        if '?' in strn:
            ram = random.randint(0, 2)
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

    
