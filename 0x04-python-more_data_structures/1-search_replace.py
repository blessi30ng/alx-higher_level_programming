#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_l = []
    for itr in range(len(my_list)):
        if my_list[itr] == search:
            new_l.append(replace)
        else:
            new_l.append(my_list[itr])
    return new_l
