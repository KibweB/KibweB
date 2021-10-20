from functools import reduce
from itertools import product
add10= lambda x: x+10
print(add10(5))
mult= lambda x,y: x*y
print(mult(2,7))
print('')

points2D=[(1,2), (15,1), (5,-1), (10,4)]
sort_pts=sorted(points2D, key=lambda x:x[0]+x[1])
print(points2D)
print(sort_pts)
print('')

b=[1,2,3,4,5,6]
c=map(lambda x: x*2, b) #multiplies each b list item by 2
print(list(c))
e =[x*2 for x in b] #simpler way to return b list items times 2
print(e)
f=[x for x in b if x%2==0] #return all even numbers in list b
print(f)
product_a =reduce(lambda x,y: x*y, b) #returns the product of all b list numbers
print(product_a)