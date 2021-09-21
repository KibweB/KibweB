myTupple="Max", 28, "Boston"
print(myTupple)
item =myTupple[-1] #negative numbers refers to the last item in tuple
print(item)
for y in myTupple: #print the tuple vertically
    print(y)

New_Tuple="a","b", "c","e","d","c"
print(len(New_Tuple))
print(New_Tuple.count("c")) #new_tuple.index return the number at which a tuple item lies

num_tuple=(1,2,3,4,5,6)
j=num_tuple[::5]
print(j)