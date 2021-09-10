lucky_numbers=[7, 85, 18, 15, 100, 12]
friends=["Eric", "Shiv", "Tyler", "Danny", "Jose"]
friends2=friends.copy()
friends.append("Joe")
friends.insert(1,"Will")
friends.remove("Shiv")
friends.sort()
print(friends)
cousins=["Erin", "Anaya", "Dara", "Zuri"]
lucky_numbers.sort()
lucky_numbers.reverse()
cousins.extend(lucky_numbers)
print(cousins)