# just python method no using extend-lib
def create_n_arr(n -> int, size -> list, default=0):
    # n = # of dimension
    # size = shape
    # default = default value of n_arr
    # return value is n_arr
    if n is 0:
        return default
    return [create_n_arr(n - 1, size, default) for _ in range(size[-n])]


arr = create_n_arr(2, [4, 2], default=28)
print(arr)
# >>> a = [
# >>>     [28, 28], 
# >>>     [28, 28], 
# >>>     [28, 28], 
# >>>     [28, 28]
# >>>     ]

# more example
# arr = create_n_arr(3, [3, 2, 4], default=0.0)
# arr = create_n_arr(4, [2, 6, 10, 4], default=False)
