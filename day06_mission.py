#9.4

class OopsException(Exception):
    pass

try:
    raise OopsException('Caught an oops')
except OopsException as err:
    print(OopsException)