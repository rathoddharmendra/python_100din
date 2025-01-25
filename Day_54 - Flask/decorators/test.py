def logger(debug_level):
    def repeat_decorator(func):
        def wrapper(times):
            print(f'{debug_level} - {func.__name__}')
            for _ in range(times):
                func(times)
            print(f'{debug_level} - {func.__name__} completed')
        return wrapper
    return repeat_decorator

@logger('DEBUG')
def greet(times: int):
    print('Hello, World!')


greet(3)