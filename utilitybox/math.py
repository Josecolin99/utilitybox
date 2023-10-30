# This file contains mathematical functionalities.

import math
import operator as op
from typing import List, Optional

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

def rule_of_three(a: float, b: float, c: float, reverse=False) -> bool:
    """
    The function calculates the missing value in a proportion using the rule of
    three.
    
    Args:
      a (float): The parameter "a" represents the first value in the rule of three
    equation.
      b (float): The parameter "b" represents the middle value in a set of three
    numbers.
      c (float): The parameter "c" represents the third value in a set of three
    values.
      reverse: A boolean parameter that determines whether to calculate the rule of
    three normally or in reverse. If reverse is set to True, the function will
    calculate (a * b) / c. If reverse is set to False or not provided, the function
    will calculate (b * c) / a. Defaults to False
    
    Returns:
      The function `rule_of_three` returns either the result of `(a * b) / c` or
    `(b * c) / a` depending on the value of the `reverse` parameter.
    """
    if reverse:
        return (a * b) / c
    return (b * c) / a
  
def average(data: List[float]) -> Optional[float]:
    """
    The function calculates the average of a list of numbers and returns it, or
    returns None if the list is empty.
    
    Args:
      data (List[float]): A list of floating-point numbers.
    
    Returns:
      the average of the given data as a float value.
    """
    if not data:
        return None
    return sum(data) / len(data)

def greatest_common_divisor(a: int, b: int):
    """
    The function `greatest_common_divisor` returns the greatest common divisor of
    two integers `a` and `b`.
    
    Args:
      a (int): an integer representing the first number
      b (int): The parameter "b" represents the second integer for which we want to
    find the greatest common divisor.
    
    Returns:
      The greatest common divisor of the two input integers, `a` and `b`.
    """
    return math.gcd(a, b)

def minimum_common_multiple(a: int, b: int):
    """
    The function calculates the minimum common multiple of two given integers.
    
    Args:
      a (int): an integer representing the first number
      b (int): The parameter "b" represents the second number for which we want to
    find the minimum common multiple.
    
    Returns:
      the minimum common multiple of the two input integers, `a` and `b`.
    """
    return abs(a*b) // greatest_common_divisor(a, b)
    
if __name__ == '__main__':
    from generals import random_number_list
    data = random_number_list(5, 0, 5)
    print(data)
    print(average(data))