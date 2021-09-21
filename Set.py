mySet=set([1,2,3])
mySet.discard(4) #doesn't return error for unknown element, unlike remove()
for t in mySet: #prints elements vertically 
    print(t)

odds={1,3,5,7,9}
even={0,2,4,6,8}
primes={2,3,5,7}
print(primes.isdisjoint(odds))
u = odds.union(even) #combines set elements without duplication 
print(u)
i=odds.intersection(primes)
print(i)
diff=primes.symmetric_difference(odds) 
print(diff)
even.update(odds) #merges sets together
print(even)