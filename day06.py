# decorator
def document_info(func):
    def new_function(*args, **kwargs):
        print('실행 중인 함수:', func.__name__)
        print('위치 기반 인수들:', args)
        print('키워드 기반 인수들:', kwargs)
        result = func(*args, **kwargs)
        print('실행 결과:', result)
        return result
    return new_function

@document_info
def sub_int(x, y):
    return x - y

@document_info
def squares(n):
    return n * n

print(sub_int(7,3))
print(squares(5))

