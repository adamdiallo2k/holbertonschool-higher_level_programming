#!/usr/bin/python3
"""module commented"""

def text_indentation(text):
    """function commented"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    symbols = ['.', '?', ':']
    for symbol in symbols:
        text = text.replace(symbol, symbol + '\n\n')

    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    print('\n'.join(lines))
