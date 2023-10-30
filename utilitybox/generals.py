import random

def random_number_list(number_elements: int, min=0, max=100):
    """
    The function `random_number_list` generates a list of random numbers within a specified range.
    
    Args:
      number_elements (int): The number of elements you want in the random number list.
      min: The minimum value that can be generated in the random number list. The default value is 0 if
    no value is provided. Defaults to 0
      max: The maximum value that can be generated in the random number list. By default, it is set to
    100. Defaults to 100
    
    Returns:
      a list of random numbers. The number of elements in the list is determined by the
    "number_elements" parameter. The minimum and maximum values for the random numbers can be specified
    using the "min" and "max" parameters, with default values of 0 and 100 respectively.
    """
    return [random.randint(min, max) for _ in range(number_elements)]