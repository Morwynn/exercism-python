"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""




EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.
    
    Parameters: 
    elapsed_bake_time(int): Elapsed bake time in minutes.

    Returns:
    int: total baked time
    """
    result = EXPECTED_BAKE_TIME - elapsed_bake_time
    return result

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.
    
    Parameters:
    number_of_layers(int): number of layers

    Returns:
        int: total preparation time in minutes.
    """
    time_for_preparation = number_of_layers * PREPARATION_TIME
    return time_for_preparation

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Total elapsed time.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.
        number_of_layers (int): number of layers

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    total_time_baked = preparation_time_in_minutes(number_of_layers) +        elapsed_bake_time 
    return total_time_baked
    