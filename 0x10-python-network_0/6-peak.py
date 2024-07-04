#!/usr/bin/python3
"""Technical interview preparation"""

def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    md = int(size / 2)
    peak_list = lidt_of_integers[md]
    if peak_list > list_of_integers[md - 1] and peak_list > list_of_integers[md + 1]:
        return peak_list
    elif peak_list < list_of_integers[md - 1]:
        return find_peak(list_of_integers[:md])
    else:
        return find_peak(list_of_integers[md + 1:])
