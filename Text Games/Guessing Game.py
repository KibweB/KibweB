secret_Word="falcon"
guess= ""
guess_count=0
attempts=3
out_of_Guesses=False

while guess != secret_Word and not(out_of_Guesses):
    if guess_count<attempts:
        guess=input("Guess the word: ")
        guess_count +=1
    else:
        out_of_Guesses=True
if out_of_Guesses:
    print("You ran out of guesses, sorry")
else:     
    print("You guessed the secret word, Kudos")