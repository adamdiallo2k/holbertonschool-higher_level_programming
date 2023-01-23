#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None, None
    else:
        return sentence[0], len(sentence)
