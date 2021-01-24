
def arg_printer(a, b, option=True, **kwargs):
    print(a, b)
    print(option)
    print(f'kwargs: {kwargs}')

if __name__ == '__main__':
    arg_printer(1, 2, param1=5, param2=6)

