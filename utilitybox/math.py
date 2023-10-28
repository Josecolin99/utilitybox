# This file contains mathematical functionalities.

import math
import operator as op

def prime_number(number: int) -> bool:
    """
    The function checks if a given number is a prime number.
    
    Args:
      number (int): The parameter "number" is an integer that represents the number
    we want to check if it is a prime number or not.
    
    Returns:
      a boolean value indicating whether the given number is a prime number or not.
    """
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
    
def even_number(number: int, reverse=False) -> bool:
    """
    The function checks if a given number is even or not, with an option to reverse
    the result.
    
    Args:
      number (int): An integer representing the number to be checked for evenness.
      reverse: The "reverse" parameter is a boolean flag that determines whether
    the function should check if the number is odd instead of even. If "reverse" is
    set to True, the function will return True if the number is odd, and False if
    it is even. If "reverse" is set to False. Defaults to False
    
    Returns:
      a boolean value. It returns True if the given number is even, and False if it
    is odd.
    """
    comparison = op.ne if reverse else op.eq
    if comparison(number % 2, 0):
        return True
    return False
