mylist=["mango","cherry", "apple"]
if "lemon" in mylist:
    print("yes")
else:
    print("no")
mylist.append("Pineapple") #adds item to the end of a list
mylist.insert(1, "cranberry")
print(mylist)
item=mylist.reverse()
print(len(mylist)) #this returns the number of items in my list
for x in mylist:
    print(x)

list_cpy=mylist.copy()
list_cpy.append("grapes")
print(list_cpy)
print("")
NumList=[1,2,3,4,5,6,7,8,9]
a=NumList[1:5] #following print statement returns items between postions 1 & 5 
v=NumList[::-1] #will retrun list in descending order
print(a)
print(v)
b=[i*i for i in NumList] #return numbered list with items all squared 
print(b)