New_dict={"Name": "Desmond", "Age": 19, "city": "Jersey City"}
print(New_dict)
print("")
Diction= dict(name="Gary", age=25, city="Edison") #dict funtion is a alt-way to create dictionary
print(Diction)
value= Diction["name"]
New_dict["email"]= "superfly@aol.com" #adding email element 
print(New_dict)
Copy_dict=New_dict.copy()#creates a true copy, changes don't affect the OG
print(Copy_dict)
New_dict.popitem() #removes last item in 1st dictionary 
print(New_dict)

if "Name" in New_dict: #only prints the name from New_Dict
    print(New_dict["Name"])

del Diction["name"] #deletes the name from 2nd dictionary 
print(Diction)