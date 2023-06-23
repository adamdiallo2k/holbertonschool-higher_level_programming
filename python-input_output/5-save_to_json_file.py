#!/usr/bin/python3
"""comment the module"""
import json


def save_to_json_file(my_obj, filename):
    """commented function"""
    my_obj = list(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
       json.dump(my_obj, f)
