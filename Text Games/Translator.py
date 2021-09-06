def translate(phrase):
    translation= ""
    for letter in phrase:
        if letter.lower() in "aeiou": #this translates vowels in phrases to Ks
            if letter.isupper():
                translation= translation+ "K"
            else:
                translation=translation+"k"
        else:
            translation=translation+letter
    return translation
print(translate(input("Type a phrase: ")))