#!/usr/bin/python3
"""comment the module"""
import json


def save_to_json_file(my_obj, filename):
    """commented function"""
    with open(filename, "w", encoding="utf-8") as f:
       f.write(json.dumps(my_obj))
       f.close