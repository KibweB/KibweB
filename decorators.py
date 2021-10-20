import functools
def star_end_Decorator(func): #defualt decorator setup
    @functools.wraps(func)
    def wrapper(*args,**kwargs): #this syntext allows use of as many arguements/key arguments as i want
        print('Start')
        result=func(*args,**kwargs)
        print('End')
        return result
    return wrapper

@star_end_Decorator       #does the same thing as "print_name=star_end_Decorator(print_name)"
def add5(x):
    return x+5
# def print_name():
#     print('Eric')

#print_name=star_end_Decorator(print_name)
result=add5(10)
print(result)
print(add5.__name__)
print('')

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                answer=func(*args, **kwargs)
            return answer
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Shawn')
print('')

class CountCalls:
    def __init__(self, func):
        self.func=func
        self.num_calls=0
    def __call__(self, *args, **kwargs):
        self.num_calls+=1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hi():
    print('Hi')

say_hi()
say_hi()