print("Greetings from Smallville")
# ask the candidate a question
activity = input( "How would you like to spend your evening?\n(A) Playing video games\n(B) Attending a party\n" )
print( f"You chose {activity}.") #print out which activity they chose
if activity == "A":
    print( "Nice choice!" )
elif activity == 'a':
    print('Gamers unite')
elif activity == "B":
    print( "Sounds fun!" )
elif activity =='b':
    print('Extrovert aye')
else :
    print('Chosse either A or B next time, for now you like to game')
    activity ='Video Games'
"""When using elif statements,I need an if statement at the beginning 
and an else at the end. I can have as many elif statements as I want in the middle."""

job=input("\nWhat would be your dream job?\n(A)Owning a Game Studio\n(B)Running a successful Youtube channel\n")
print(f'You entererd {job}')
if job == 'A':
    print("You're real serious about this gaming thing")
elif job == 'a':
    print('Game dev union just got another member')
elif job =="b":
    print('YouTuber aye')
elif job =='B':
    print('Hope you win a gold play button')
else:
    print("Pick either A or B next time, but let's just go with the Youtube route")
    job='Famous Youtuber'

value=input("\nWhat is more important to you\n(A)Well-paying Office Job\n(B)Fun part-time job\n")
if value=='A':
    print('Cash rules everything around you')
elif value=='a':
    print('Great to build capital')
elif value=='B':
    print('fun flexabilty is what you want')
elif value =='b':
    print('Whatever makes you feel better')
else:
    print("You must type A or B, let's just say a well paid job is important to you.")
    value ='a Well paid job'

decade=input('\nWhich decade were you born in?\n(A)1990s\n(B)2000s\n')
if decade=='A':
    print("90's baby, aye")
elif decade == 'a':
    print('A child of the early digital Era')
elif decade=='B':
    print('2000s? sounds fun')
elif decade =='b':
    print('Cool beans')
else:
    print("Let's just say you were a 90's baby")
    decade='the 90s'
    
travel = input("\nWhat's your favorite way to travel?\n(A) Driving\n(B) Flying\n" )
if travel == "A":
    print( "Driving, nice choice!" )
elif travel =='a':
    print('So you like to have ultimate control of where you go')
elif travel =="B":
    print( "Flying? Sounds fun!" )
elif travel =='b':
    print('Ever been to the Mile high club')
else:
    print("You must type A or B, let's just say your favorite way to travel is by driving")
    travel = "Driving"

# print out the choices
print( f"\nYou chose {activity}, then {job}, then {value}, then {decade}, then {travel}.")

# create some variables for scoring
sam_like = 0
cam_like = 0
kai_like = 0
zBo_like = 0

# update scoring variables based on the activity choice
if activity == "A":
    sam_like = sam_like + 2
    zBo_like = zBo_like + 2
    kai_like = kai_like + 2
elif activity =='a':
    sam_like = sam_like + 2
    zBo_like = zBo_like + 2
    kai_like = kai_like + 2
else:
    cam_like = cam_like + 1
    zBo_like = zBo_like + 1

# update scoring variables based on the job choice
if job == "A":
    sam_like = sam_like + 2
    zBo_like = zBo_like + 2
    cam_like = cam_like - 1
elif job =='a':
    sam_like = sam_like + 2
    zBo_like = zBo_like + 2
    cam_like = cam_like - 1
else:
    sam_like = sam_like - 1
    kai_like = kai_like + 2
    zBo_like = zBo_like + 1

# update scoring variables based on the value choice
if value == "A":
    sam_like = sam_like - 1
    kai_like = kai_like + 1
elif value =='a':
    sam_like = sam_like - 1
    kai_like = kai_like + 1
else:
    sam_like = sam_like + 2
    cam_like = cam_like + 2
    zBo_like = zBo_like + 1

# update scoring variables based on the decade choice
if decade == "A":
    cam_like = cam_like + 2
    sam_like = sam_like + 2
elif decade =='a':
    cam_like = cam_like + 2
    sam_like = sam_like + 2 
else:
    kai_like = kai_like + 1
    zBo_like = zBo_like + 2

# update scoring variables based on the travel choice
if travel == "A":
    sam_like = sam_like - 2
    kai_like = kai_like + 1
    zBo_like = zBo_like - 1
elif travel =='a':
    sam_like = sam_like - 2
    kai_like = kai_like + 1
    zBo_like = zBo_like - 1
else:
    sam_like = sam_like + 1
    cam_like = cam_like + 1
    kai_like = kai_like - 1

# print the results depending on the score
if sam_like >= 3:
    print( "You're most like Michael Sam!" )
elif cam_like >= 3:
    print( "You're most like Super Cam!" )
elif kai_like >= 3:
    print( "You resemble Kobra Kai!" )
else:
    print( "You're more like Gen Z-BO" )