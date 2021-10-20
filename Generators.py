#genarators use way less memory than regular functions and list
def myGenerator():
    yield 3
    yield 2
    yield 1

g=myGenerator()
print(sorted(g)) #sorts numbers 1-3
print('')

def countdwn(num):
    print('Starting')
    while num>0:
        yield num
        num-=1

cd=countdwn(4)
val=next(cd)
print(val)

print(next(cd))
print(next(cd))
print(next(cd))
print('')

def fibonacci(limit): #first two numbers are 0 & 1.Following numbers are sum of previous 2 numbers
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
fib=fibonacci(30)
for f in fib:
    print(f)
print('')
    
new_gen= (t for t in range(10) if t%2==0)
print(list(new_gen)) #prints even number up to 10