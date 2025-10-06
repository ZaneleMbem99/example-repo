def largest_num(num_integer):
    """
    find the largest number from the list

    Args:
    num_integer: list of integers

    return: 
    the largest number from the given list
    """
    if len(num_integer) == 1:
        return[0]
    else: 
        rest_of_list_largest= largest_num(num_integer[1:])
        if num_integer[0] > rest_of_list_largest:
            return num_integer[0]
        else: 
            return rest_of_list_largest