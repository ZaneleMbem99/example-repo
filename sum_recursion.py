def adding_up_to(interger_list, index):
    """
   calculates the sum of numbers in a list up to and including a specified
   index point

     Args:
      interger_list: list of integers
      index: A single integer represent the index point up to which the sum
      must be calculated

      Returns:
      sum of the integers in the list including the specified index point """
    if index == 0:
        return interger_list[0]

    else:
        return interger_list[index] + adding_up_to(interger_list, index - 1)
