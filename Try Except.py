try:
    #value=10/0 --uncomment to get Divided by zero output
    number=int(input("Type a number "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Wrong input")