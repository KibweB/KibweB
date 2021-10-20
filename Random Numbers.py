import random, secrets
a=random.randint(1,12) 
print(a)
b=random.randrange(1,10) #doesn't include max range of ints
print(b)
c=random.normalvariate(0,1)
print(c)
print('')

mylist=list('ABCDEFG')
d=random.sample(mylist,3)
print(d)
e=random.choices(mylist,k=3) #can now pick duplicate list elements
print(e)
random.shuffle(mylist)
print(mylist)
print('')

random.seed(1)
print(random.random())
print(random.randint(2,20))
f=secrets.choice(mylist)
print(f)
e=secrets.randbits(4) #4 bits it can have four different binary spots
print(e)