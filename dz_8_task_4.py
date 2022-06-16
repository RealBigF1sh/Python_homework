from functools import wraps


def val_checker(decorator):
    def new_val_checker(func_calculator):
        @wraps(func_calculator)
        def wrapped(x):
            if decorator(x):
                return func_calculator(x)
            else:
                raise ValueError(x)

        return wrapped
    return new_val_checker


@val_checker(lambda x: x > 0)
def calculator(x):
    return x ** 3


ask = calculator(7)
print(ask)
print(calculator.__name__)
print(calculator.__doc__)
