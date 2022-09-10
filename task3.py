from datetime import datetime


def path_decorator(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(path, 'a') as f:
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
    return decorator


@path_decorator('task3_log.txt')
def list1_to_list(list1, my_list):
    if isinstance(list1, list):
        for list2 in list1:
            list1_to_list(list2, my_list)
    else:
        my_list.append(list1)


class FlatIterator:
    def __init__(self, list1):
        self.list1 = []
        list1_to_list(list1, self.list1)
        # for list2 in list1:
        #     self.list1 += list2
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i >= len(self.list1):
            raise StopIteration
        return self.list1[self.i]


nested_list = [
    ['a', 'b', 'c', ],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]

print(flat_list)

print('=*'*40)


@path_decorator('task3_log.txt')
def flat_generator(list1):
    my_list = []
    list1_to_list(list1, my_list)
    # for list2 in list1:
    #     my_list += list2
    i = 0
    while i < len(my_list):
        yield my_list[i]
        i += 1


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None, ],
]
for item in flat_generator(nested_list):
    print(item)
