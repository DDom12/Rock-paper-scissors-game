import random

Choice = input("Pick: \n Rock \n Paper \n Scissors \n")
Choice = Choice.lower()


moves = ["rock", "paper", "scissors"]

randchoice = random.choice(moves)
print(randchoice)

if Choice == "rock" and randchoice == "paper":
    print("You lose")
elif Choice == "paper" and randchoice == "rock":
    print("You win")
elif Choice == "scissors" and randchoice == "paper":
    print("You win")
elif Choice == "paper" and randchoice == "scissors":
    print("You lose")
elif Choice == "rock" and randchoice == "scissors":
    print("You win")
elif Choice == "scissors" and randchoice == "rock":
    print("You lose")
elif Choice == "rock" and randchoice == "rock":
       print("You draw")
elif Choice == "paper" and randchoice == "paper":
    print("You draw")
elif Choice == "scissors" and randchoice == "scissors":
    print("You draw")
else:
    print("INVALID")
    

    


