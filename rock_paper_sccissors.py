import random
game=['rock','paper','scissors']
user=int(input("type 0 to choose rock , 1 to choose paper, 2 to choose Scissors"))
computer=random.choice(game)

if user in [0,1,2]:
    user_choice=game[user]
else:
    print("Wrong choice")
    exit()
print(f"User chose {user_choice}")
print(f"Computer chose {computer}")
if user_choice=="rock" and computer=="scissors":
    print("you won")
elif user_choice=="scissors" and computer=="paper":
    print("you won")
elif user_choice=="paper" and computer=="rock":
    print("you won")
elif user_choice==computer:
    print("Its a tie")
else:
     print("You lose")


