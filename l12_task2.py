def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f'A {type(e).__name__} has occurred: {e}')
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})

some_function_with_risky_operation({'key': 'bar'})
