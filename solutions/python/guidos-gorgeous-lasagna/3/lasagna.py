EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.
    
    Parameters: 
    elapsed_bake_time(int): Elapsed bake time in minutes.

    Returns:
    int: Remaining bake time in minutes.
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
        elapsed_bake_time (int): Elapsed bake time in minutes.
        number_of_layers (int): number of layers

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    total_time_baked = preparation_time_in_minutes(number_of_layers) +        elapsed_bake_time 
    return total_time_baked
    