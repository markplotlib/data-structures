# https://towardsdatascience.com/10-examples-to-master-args-and-kwargs-in-python-6f1e8cc30749
# left off: ex 8-10 remain

def arg_printer(a, b, *args, option=True, **kwargs):
    print(a, b)
    print(args)
    print(option)
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    arg_printer(1, 2, 5, 'three, sir', param1=5, param2=6)
