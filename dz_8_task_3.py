from functools import wraps


def type_logger(func):
    @wraps(func)
    def my_wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return my_wrapper


@type_logger
def calc_cube(*args):
    return list(map(lambda x: x ** 3, args))


ask = calc_cube(5, 3)
print(ask)
print(calc_cube.__name__)
print(calc_cube.__doc__)
