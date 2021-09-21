from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
LV = "aaaaaaaaaabbbbbbbbbbcccccccc"
my_counter =Counter(LV)
print(my_counter.items()) #return item with number amount next to it
print(my_counter.most_common(2)) #return 2nd most common item
print(list(my_counter.elements())) #return items in list form 
print('')

point= namedtuple('point', 'x,y')
pt=point(1,-4)
print(pt.x,pt.y)
print('')

ord_dict= OrderedDict()
ord_dict['a']=1
ord_dict['b']=2
ord_dict['c']=3
ord_dict['d']=4
print(ord_dict)
print('')

rick=defaultdict(float)
rick['a']=1
rick['b']=2
print(rick['b'])

d=deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.extendleft([4,5,6])
d.rotate(1)
print(d)