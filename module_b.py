from module_a import process_data

def analyze_and_process(x):
    result = process_data(x)
    if isinstance(result, str):
        return "Error in A"
    return result + 5