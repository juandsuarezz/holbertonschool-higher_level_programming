#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    new_list = my_list[:]
    new_list.sort()
    return new_list[-1]
