
import random

def drink():
    drink = random.randint(0, 5)
    if drink == 0:
        return 'Flamingos turn pink from eating shrimp.'
    elif drink == 1:
        return 'The only food that doesn’t spoil is honey.'
    elif drink == 2:
        return 'Shrimp can only swim backwards.'
    elif drink == 3:
        return 'The lifespan of a taste bud is about 10 days.'
    elif drink == 4:
        return 'It is illegal to sing off-key in North Carolina.'
    else:
        return 'Error'

# Test the function
print(drink())