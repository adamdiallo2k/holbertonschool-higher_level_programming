#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    symbols = ['.', '?', ':']
    for symbol in symbols:
        text = text.replace(symbol, symbol + '\n\n')

    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    print('\n'.join(lines))
