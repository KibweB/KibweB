is_male=True
is_Tall=False

if is_male and is_Tall:
    print("You're a dude and tall, and both")
elif is_male and not(is_Tall):
    print("You're a short dude")
elif not(is_male) and is_Tall:
    print("You're a tall woman")
else:
    print("You are a woman, neither male or tall")