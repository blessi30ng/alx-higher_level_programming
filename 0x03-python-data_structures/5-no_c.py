#!/usr/bin/python3

def no_c(my_string):
    new_s = ""
    for i in range(len(my_string)):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            continue
        new_s += my_string[i]
    return new_s
