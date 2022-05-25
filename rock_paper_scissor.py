import random

ROCK = 1
PAPER = 2
SCISSOR = 3

choice_names = {ROCK: "Rock", PAPER: "Paper", SCISSOR: "Scissor"}

while True:
    print("Enter choice with number \n 1. Rock \n 2. Paper \n 3. Scissor\n")

    user_choice = int(input("Your turn: ")) #e merr inputin prej userit

    while user_choice > SCISSOR or user_choice < ROCK:
        user_choice = int(input("Enter valid input: "))

    print("Your choice is: " + choice_names[user_choice]) #printon zgjedhjen tuaj

    comp_choice = random.randint(ROCK, SCISSOR) #pc e selekton ne menyre randome zgjidhjen

    while comp_choice == user_choice:
        comp_choice = random.randint(ROCK, SCISSOR)

    print("Computer's choice is: " + choice_names[comp_choice])

    # rezultatin
    if (user_choice == ROCK and comp_choice == PAPER) or (
        user_choice == PAPER and comp_choice == ROCK
    ):
        result = choice_names[PAPER]
    elif (user_choice == ROCK and comp_choice == SCISSOR) or (
        user_choice == SCISSOR and comp_choice == ROCK
    ):
        result = choice_names[ROCK]
    else:
        result = choice_names[SCISSOR]

    # me bo check kush ka fitu
    if result == choice_names[user_choice]:
        print("YOU WONNN!!! ")
    else:
        print("Computer wins :(")

    print("Do you want to play again? (Y/N)")
    answer = input()

    if answer.lower() == "n":
        break

print("\nThanks for playing")

