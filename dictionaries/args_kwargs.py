# https://towardsdatascience.com/10-examples-to-master-args-and-kwargs-in-python-6f1e8cc30749
# args and kwargs

def add(*args):
    total = 0
    for i in args:
        total += i
    return total


if __name__ == '__main__':
    print(add(3, 4))
    print(add(3, 4, 5))
    print(add(3, 4, 5, 6, 7))
