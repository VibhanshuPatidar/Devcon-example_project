def process_data(x):
    if x < 0:
        return "Invalid"
    return x * 2

# example_project/module_b.py
from module_a import process_data