from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time elapsed: {end_time - start_time} seconds")
        return result
    return wrapper

@speed_test
def sum_nums_gen():
    return sum(x for x in range(50000000))

@speed_test
def sum_nums_list():
    return sum([x for x in range(50000000)])

sum_nums_gen()
# Executing sum_nums_gen
# Time elapsed: 2.814161777496338 seconds
sum_nums_list()
# Executing sum_nums_list
# Time elapsed: 8.948267936706543 seconds