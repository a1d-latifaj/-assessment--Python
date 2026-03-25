import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funksioni '{func.__name__}' u ekzekutua per: {end_time - start_time:.2f} sekonda")
        return result
    return wrapper

@log_execution_time
def example_function(*args):
    total = 1
    for num in args:
        total *= num
    return total

print(f"Total: {example_function(2,8,3,2,2)}")
