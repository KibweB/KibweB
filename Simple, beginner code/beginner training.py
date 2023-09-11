from datetime import date 
#A date in a program usually means both the calendar date and the time.
print(date.today()) #dates printed in Year-MM-DD format 
print("Today's date is: " + str(date.today()))
sum=3+9; product=sum*6
print(sum); print(product)
#variable reminder
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string
type(distance_to_alpha_centauri) #the function type lets me know the type of variable
w=40; print(w/2)

#Exercise: Use if/else statements to examine an object's size
object_size = 10
if object_size > 5:
    print('We need to keep an eye on this object')
else:
    print('Object poses no threat.')
    
Comet_size=20
proximity=9000
if Comet_size> 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')