#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_c = None
        _tuple = (length, first_c)
        return _tuple
    else:
        first_c = sentence[0]
        _tuple = (length, first_c)
        return _tuple
        
