num1=float(input("Enter a number: "))
op=input("Submit an operator: ")
num2=float(input("Enter another number: "))

if op == "+":
    print(str(num1+num2) +" is the answer")
elif op == "-":
    print(str(num1-num2)+" is the answer")
elif op == "/":
    print (str(num1/num2)+" is the answer")
elif op == "*":
    print (str(num1*num2)+" is the answer")
else:
    print ("Invalid operator")