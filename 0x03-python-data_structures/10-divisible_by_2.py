#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_b = [a % 2 == 0 for a in my_list]
    return list_b
