#!/usr/bin/python3.8
if __name__ == "__main__":
    import hidden_4
    for n  in dir(hidden_4):
        if n[:2] != "_":
            print("{}".format(n))
