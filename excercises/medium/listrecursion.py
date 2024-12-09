def highest_integer(lst):
    if len(lst) == 1:
        return lst[0]


    max_number_rest = highest_integer(lst[1:])

   
    return lst[0] if lst[0] > max_number_rest else max_number_rest



print(highest_integer([-1, 3, 5, 6, 99, 12, 2]))