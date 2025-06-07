from module_a import process_data
from module_b import analyze_and_process

def full_pipeline(x):
    a = process_data(x)
    b = analyze_and_process(x)
    if isinstance(a, str) or isinstance(b, str):
        return "Pipeline failed"
    return a + b