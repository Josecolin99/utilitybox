
import math

def prime_number(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif even_number(number) and number > 2:
        return False
    sqrt_number = math.ceil(math.sqrt(number))
    for i in range(3, (sqrt_number + 1), 2):
        if number % i == 0:
            return False
    return True
    
def even_number(number):
    if number % 2 == 0:
        return True
