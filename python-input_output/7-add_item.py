#!/usr/bin/python3
""" Module """
import sys
import json

def load_from_json_file(filename):
    """
    Function to load an object from a JSON file.

    Parameters:
    filename (str): The name of the JSON file.

    Returns:
    object: The object represented by the contents of the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

def save_to_json_file(my_obj, filename):
    """
    Function to save an object to a JSON file.

    Parameters:
    my_obj (object): The object to be saved.
    filename (str): The name of the JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

if __name__ == '__main__':
    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []

    for item in sys.argv[1:]:
        items.append(item)

    save_to_json_file(items, 'add_item.json')

