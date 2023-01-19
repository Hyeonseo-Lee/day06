#9.3

def test(func):
    def new_test(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print(result)
        return('end')
    return new_test

def sum(a, b):
    return (a + b)

print(test(sum)(1, 2))