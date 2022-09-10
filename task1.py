from datetime import datetime


def decorator(func):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as f:
            f.write(f'Datetime: {datetime.now()}\n')
            f.write(f'Name of function: {func.__name__}\n')
            if args:
                f.write(f'Args of function: {args}\n')
            if kwargs:
                f.write(f'Kwargs of function: {kwargs}\n')
            result = func(*args, **kwargs)
            f.write(f'Return of function: {result}\n\n')
        return result
    return wrapper


@decorator
def hello(word1, word2=''):
    return " ".join(('Hello, ', word1, word2))


print(hello('My', word2='World'))
