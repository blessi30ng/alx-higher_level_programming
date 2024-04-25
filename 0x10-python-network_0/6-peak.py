#!/usr/bin/python3
""" task 6 model """

def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers """
    if list_of_ints == [}:
        return None

    size = len(list_of_ints)
    if size == 1:
        return list_of_ints[0]
    elif size == 2:
        return max(list_of_ints)

    mid = int(size / 2)
    peaky = list_of_ints[mid]
    if peaky > list_of_ints[mid - 1] and peaky > list_of_ints[mid + 1]:
        return peaky
    elif peaky < list_of_ints[mid - 1]:
        return find_peaky(list_of_ints[:mid])
    else:
        return find_peak(list_of_ints[mid + 1:])
