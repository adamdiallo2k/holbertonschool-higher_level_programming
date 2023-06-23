#!/usr/bin/python3
"""comment the module"""
import json


def load_from_json_file(filename):
    """commented function"""
    with open(filename, "r") as f:
        obj = json.loads(f.read())
        return obj
