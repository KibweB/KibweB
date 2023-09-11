"""A while loop performs an operation while a certain condition is true. Use a while loop to:
Check for another line in a file.
Check if a flag has been set.
Check if a user has finished entering values.
Check if something else has changed to indicate that the code can stop performing the operation
-Ensure the condition changes, if it's always true Python will run the code until the program crashes
"""
new_Planet=" "; planets=[]
while new_Planet.lower()!= 'done':#.lower() accounts for case insensitive inputs
    if new_Planet:
        planets.append(new_Planet)
    new_Planet=input('Enter a new planet, or done when finished: ')
        
print(planets)

from time import sleep    
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")

for planet in planets:
    print(planet)