#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    temp_res = 0
    for x in range(0, list_length):
        try:
            temp_res = my_list_1[x] / my_list_2[x]
        except TypeError:
            temp_res = 0
            print("wrong type")
        except ZeroDivisionError:
            temp_res = 0
            print("division by 0")
        except IndexError:
            temp_res = 0
            print("out of range")
        finally:
            pass
        result.append(temp_res)
    return result
