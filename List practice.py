planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
planets[3]="Red Planet"; print("\nMars is also known as the", planets[3])
Planet_count=len(planets)
print("There are", Planet_count, "planets in this Solar System")
#.pop() removes the last item in a list
#Indexes start at zero and increase, but negative indexes start at the end of the list and work backward.
"""To determine where in a list a value is stored, you use the list's index method. 
This method searches for the value and returns the index of that item in the list.
If it doesn't find a match, it returns -1."""
jupiter_index = planets.index("Jupiter"); print(planets)
print("\nJupiter is", jupiter_index,"planets away from the sun")
#Because indexing starts with 0, I need to add 1 to display the proper number.
planets.append("Pluto"); print("Actually there are ", len(planets),"planets in the Solar System")
print(planets[8],"is the last planet") #planets[-1] would print the same result 
gravity_on_earth = 1.0; gravity_on_the_moon = 0.166
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight=27888 #in pounds, on Earth
print("\nOn Earth, a double decker bus weighs",bus_weight,"Lbs")
print("But on Mercury, a double decker bus weighs", bus_weight*gravity_on_planets[0],"Lbs")
print("The lightest the bus could be in this Solar System is", bus_weight*min(gravity_on_planets),"Lbs on the",planets[3])
print("The heaviest a bus would be is",bus_weight*max(gravity_on_planets),"Lbs on planet Jupiter")
Planets_before_Earth= planets[0:2]; print(Planets_before_Earth)
After_Earth=planets[3:]; print(After_Earth)
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]
regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort() #write sort method before I access the list
print("\nThe regular satellite moons of Jupiter are", regular_satellite_moons)
#.sort() method sorts a list of strings in alphabetical order and a numbers in numeric order
#To sort a list in reverse order, call .sort(reverse=True)
user_Planet=input("\nPlease enter the name of a planet, capitalized: ")
planet_index=planets.index(user_Planet)
print("Here are the planets closer to the sun than " + user_Planet)
print(planets[0:planet_index])
user_Planet=input("Please enter the name of another planet, capitalized: ")
print("Here are the planets further away from the sun than" + user_Planet)
print(planets[planet_index + 1:])
