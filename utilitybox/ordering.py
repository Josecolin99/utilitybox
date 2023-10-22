import time
import random
import operator

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

def bubble_sort(data: list, reverse=False):
    """
    The `bubble_sort` function sorts a given list of data in ascending order using the bubble sort
    algorithm, and can also sort in descending order if the `reverse` parameter is set to `True`.
    
    Args:
      data (list): The `data` parameter is a list of elements that you want to sort using the bubble
    sort algorithm.
      reverse: The "reverse" parameter is a boolean value that determines whether the sorting should be
    done in ascending order (default) or descending order. If "reverse" is set to True, the sorting will
    be done in descending order. Defaults to False
    
    Returns:
      The function `bubble_sort` returns the sorted list `data`.
    """
    comparison = operator.gt if reverse else operator.lt
    all_cleanded = True
    range_valid = len(data) - 1
    while all_cleanded:
        start, end = 0, 1
        all_cleanded = False
        for _ in range(range_valid):
            first_number, last_number  = data[start], data[end]
            if comparison(last_number, first_number):
                data[start], data[end] = last_number, first_number
                all_cleanded = True
            start, end = start + 1, end + 1
    return data
     
def selection_sort(data: list, reverse=False):
    """
    The `selection_sort` function sorts a given list of numbers in ascending order using the selection
    sort algorithm.
    
    Args:
      data (list): The `data` parameter is a list of elements that you want to sort.
      reverse: The `reverse` parameter is a boolean value that determines whether the sorting should be
    in ascending order (default) or descending order. If `reverse` is set to `True`, the sorting will be
    done in descending order. Defaults to False
    
    Returns:
      the sorted list.
    """

    comparison = operator.gt if reverse else operator.lt
    data_split = 0
    global_index = 0
    while True:
        data_current = data[data_split:]
        focus_number = data_current[0]
        focus_index = data_split
        for index in range(len(data_current)):
            current_number = data_current[index]
            
            if comparison(current_number, focus_number):
                focus_number = current_number
                focus_index = data_split + index
        data_split += 1
        if data_split > len(data)-1: break
        data[global_index], data[focus_index] = data[focus_index], data[global_index]
        global_index += 1
    
    return data
  
def inserion_sort(data:list, reverse=False):
    """
    The `insertion_sort` function sorts a given list of data in ascending order by
    default, or in descending order if the `reverse` parameter is set to `True`.
    
    Args:
      data (list): The "data" parameter is a list of elements that you want to sort
    using the insertion sort algorithm.
      reverse: The "reverse" parameter is a boolean value that determines whether
    the sorting should be in ascending order (False) or descending order (True). By
    default, it is set to False, which means the sorting will be in ascending
    order. Defaults to False
    
    Returns:
      the sorted list.
    """
    comparison = operator.gt if reverse else operator.lt
    for index, dato in enumerate(data):
        reverse_index = index
        while reverse_index > 0 and comparison(dato, data[reverse_index - 1]):
            data[reverse_index] = data[reverse_index - 1]
            reverse_index -= 1
        data[reverse_index] = dato
    return data

def inserion_sort_bad_implement(data:list):
    """
    The function `inserion_sort_bad_implement` is an implementation of the
    insertion sort algorithm in Python, but it has some inefficient and unnecessary
    steps.
    
    Args:
      data (list): The parameter `data` is a list of elements that needs to be
    sorted using the insertion sort algorithm.
    """
    analizated_start_index = 0
    analizated_end_index = 0
    for index, dato in enumerate(data):
        print(f'Indice: {index}, dato: {dato}')
        reverse_index = index
        min_index = 0
        required_move = False
        while reverse_index > 0:
            reverse_index -= 1
            if dato < data[reverse_index]:
                min_index = reverse_index
                required_move = True
        if required_move:
            data.pop(index)
            data.insert(min_index, dato)
        analizated_end_index += 1

if __name__ == '__main__':
    reverse = False
    data = random_number_list(number_elements=20_000, min=0, max=20_00)
    print(data)
    # bubble = bubble_sort(data, reverse=reverse)
    # print(bubble)
    # print()
    # selection = selection_sort(data, reverse=reverse)
    # print(selection)
    insertion = inserion_sort(data, reverse)
    print(insertion)
  

    