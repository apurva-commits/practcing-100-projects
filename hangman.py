word_list=['jungkook','rich','success']
import random
word_list.append(input("Any word you want to add?").lower())
print("uupdates",word_list)
hey=random.choice(word_list)
print(hey)
placeholder=""
lenght=len(hey)
for i in range (lenght):
    placeholder += "* "
print(placeholder)
lives = 6
game_over=False

listt=[]
while game_over is not True:
    user=input("Guess the letter").lower()

    if user not in hey:
        lives -= 1
        print("Incorrect guess")
    display = ""
    for he in hey:
        if he==user:
            display+=user
            listt.append(user)
        elif he in listt:
           display+=he
        else:
            display+="*"
    print(display)

    if "*" not  in display:
        game_over=True
        print("yhh, you won")
    if lives==0:
       game_over=True
       print(f"You lose correct word is {hey}")

