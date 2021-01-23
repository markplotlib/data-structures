# https://towardsdatascience.com/10-examples-to-master-args-and-kwargs-in-python-6f1e8cc30749
# args and kwargs

def add(*args):
    total = 0
    for i in args:
        total += i
    return total

def arg_printer(a, b, *args):
    print(f'a is {a}')
    print(f'b is {b}')
    print(f'args is {args}')

def addition(a, b, *args, option=True):
    total = 0
    if option:
        for i in args:
            total += i
        return a + b + total
    else:
        return total


if __name__ == '__main__':
    print(add(3, 4))
    print(add(3, 4, 5))
    print(add(3, 4, 5, 6, 7))

    arg_printer('hi', 'lo', 'huey', 'dewey', 'louie')
    arg_printer(9, 1, 4, 5, 6)

    print(addition(3, 5, 7, 8, 9))
