import random
options=("stone","paper","scissor")
running=True
user_score=0
comp_score=0
while running:
    user_choice=None
    computer= random.choice(options)
    while user_choice not in options:
        user_choice=input("Enter any options[stone,paper,scissor]: ").lower()
        print(f"User's choice: {user_choice}")
        print(f"computers: {computer}")
        if user_choice==computer:
            print("It's a tie!!!!")
        elif (user_choice=="stone" and computer=="scissor" ) or (user_choice=="paper" and computer=="stone") or (user_choice=="scissor" and computer=="paper"):
            print("You win..")
            user_score+=1
        
        else:
            print("You loss")
            comp_score+=1
        again=input("Wanna play again (y/n): ").lower()
        if again=="n" :
            running=False
score=input("Wanna see the scores??? (y/n): ").lower()
if score=="y":
    print(f"User's score: {user_score}")
    print(f"Computer's score: {comp_score}")
if user_score>comp_score:
    print(f"You are the winner :)")
elif user_score<comp_score:
    print("You loss")
else:
    print("Tieeee")

print("THANKS FOR PLAYING!!!!")
