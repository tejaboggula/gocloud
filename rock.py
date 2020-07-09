import sys
user1 = input("Name of Player1")
user2 = input("Name of Player2")
player1_choice = input("%s, What would you choose : Rock, paper or scissors: " %user1)
player2_choice = input("%s, What would you choose : Rock, paper or scissors: " %user2)

def compare(u1,u2):
    if u1==u2:
        print("The game is tied")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return ("rock wins")
        else:
            return("scissors wins")

    elif u1 == 'scissors':
        if u2 == 'paper':
            return("scissors wins")
        else:
            return("paper wins")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("paper wins")
        else:
            return("rock wins")
    else:
        return("Invalid  Input")
        sys.exit()

print(compare(player1_choice,player2_choice))
