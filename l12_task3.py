import functools


def check_types(func):
    @functools.wraps(func)
    def wrapper(*args):
        annotations = func.__annotations__
        for name, expected_type in annotations.items():
            actual_value = args[0]
            if not isinstance(actual_value, expected_type):
                return TypeError(
                    f"Arguments must be {expected_type}, "
                    f"not {type(actual_value)}"
                    )
            else:
                result = func(*args)
                print(
                    f"The type of the return value of the result is "
                    f"{type(result)}"
                    )
                return result
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))
