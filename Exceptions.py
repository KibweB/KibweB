class ValueTooHighError(Exception):
    pass
class ValueTooSmallEroor(Exception):
    def __init__(self, message, value):
        self.message=message
        self.value=value

def test_value(t):
    if t>100:
        raise ValueTooHighError('value is too high')
    if t<5:
        raise ValueTooSmallEroor('value is too small',t)

try:
    test_value(3)
except ValueTooHighError as x:
    print(x)
except ValueTooSmallEroor as x:
    print(x.message, x.value)


""" try:
    a =5/0
    b =a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('all good carry on')
finally:
    print('cleaning up......') """