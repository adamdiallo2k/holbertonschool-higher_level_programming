#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return 0, None
    tuple_c = tuple( word for word in sentence)
    return len(tuple_c), tuple_c[0]

