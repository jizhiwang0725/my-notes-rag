import time
from functools import wraps

def timer(func):
    """A reusable decorator that prints the runtime of a function to the terminal."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        
        # Run the actual function
        result = func(*args, **kwargs) 
        
        end_time = time.perf_counter()
        
        print("")
        print(f"⏱️  [{func.__name__}] finished in {end_time - start_time:.4f} seconds")
        
        return result
    return wrapper