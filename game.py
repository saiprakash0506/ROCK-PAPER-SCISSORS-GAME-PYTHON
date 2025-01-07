import random
l=["rock","paper","scissors"]
computer_choice=random.choice(l)
game=True
while game:
    user_choice=input("CHOOSE: rock, paper,scissors:").lower()
    if computer_choice==user_choice:
        print("Computer choice:",computer_choice)
        print("User choice:",user_choice)
        print("It's a tie")

    elif computer_choice=="rock" and user_choice=="paper":
        print("Computer choice:",computer_choice)
        print("User choice:",user_choice)
        print("You won")

    elif computer_choice=="rock" and user_choice=="scissors":
        print("Computer choice:",computer_choice)
        print("User choice:",user_choice)
        print("Computer won")

    elif computer_choice=="paper" and user_choice=="rock":
        print("Computer choice:",computer_choice)
        print("User choice:",user_choice)
        print("Computer won")

    elif computer_choice=="paper" and user_choice=="scissors":
        print("Computer choice:",computer_choice)
        print("User choice:",user_choice)
        print("You won")

    elif computer_choice=="scissors" and user_choice=="rock":
        print("Computer choice:",computer_choice)
        print("User choice:",user_choice)
        print("You won")

    elif computer_choice=="scissors" and user_choice=="paper":
        print("Computer choice:",computer_choice)
        print("User choice:",user_choice)
        print("Computer won")

    else:
        print("Kindly choose between the given options only..")

    again=input("Do you want to play again(y/n):").lower()
    if not again=="y":
        game=False
print("Thanks for playing")