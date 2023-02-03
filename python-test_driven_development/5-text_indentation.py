#!/usr/bin/python3
"""module """
def text_indentation(text):
    """
    This function takes a string as input and adds two new lines after each of the characters '.', '?' and ':'.
    
    Arguments:
    text -- a string to be indented

    Raises:
    TypeError: if the input 'text' is not a string

    Returns:
    None
    """
    # check if the input is a string
    if type(text) != str:
        raise TypeError("text must be a string")
    
    # initialize a new string to store the indented text
    new_text = ""
    
    # iterate over each character in the input text
    for char in text:
        new_text += char
        
        # add two new lines after each of the characters '.', '?' and ':'
        if char in ".?:":
            new_text += "\n\n"
    
    # print the indented text with extra whitespaces stripped at the end
    print(new_text.strip(), end="")

