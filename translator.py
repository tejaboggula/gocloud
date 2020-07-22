def translator(phrase):
    translation = ""

    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "T"
        else:
            translation = translation + letter

    return translation


print(translator(input("Enter a phrase:  ")))