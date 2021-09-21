my_string="  Goodbye planet    "
my_string=my_string.strip() #strips empty space from string
print(my_string)
print(my_string.upper())
var='Tom'
tom_string="The variable is %s" %var # %s is a helpful place-holder method 
print(tom_string)
num=16
num_string="The variable is %d" %num # %d is a place-holder method for whole numbers
print(num_string)
deci=3.1246328
flo_string="The variable is %f" %deci # %f is place-holder method for floats
print(flo_string)

print("")
print(my_string.replace("Planet", 'world'))
print(my_string.count("o"))
substring= my_string[::2]
print(substring)
if "e" in my_string:
    print('yeah')
else:
    print('nah')

elem=5.7554865
var2= 85
ele_string="the new variables are {:.2f} and {}".format(elem, var2) #alt way for place-holder methods| :.2f specifies I want 2 numbers after decimal  
print(ele_string)
tote=17.482
note=48
oate_string=f"The latest variables are {tote} and {note/2}" #f string is the newest place-holder method
print(oate_string)

print('')
new_string="How are u doing"
list=new_string.split()
print(list)
new_string=" ".join(list) #joins list back to a string, include space for proper sentence 
print(new_string)
sec_list=['k']*7
print(sec_list)
Sec_string=' '.join(sec_list)
print(Sec_string)