secret_word = "teja"
guess = ""
i = 0
while guess != secret_word or i == 3:
    
    guess = input("Enter guess: ")
    i += 1
    

print("You win!")
print("you lost")