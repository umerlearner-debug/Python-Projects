import random
while True:
    user_action = input("Enter your choice (ROCK/PAPER/SCISSOR): ")

    possible_action = ["ROCK","PAPER","SCISSOR"]
    computer_action = random.choice(possible_action)
    print(f"\n You choose, {user_action}, computer choose {computer_action}. \n")
    if user_action == computer_action:
        print(f"Both player selected {user_action}. It's a tie")
    elif user_action == "ROCK":
        if computer_action == "SCISSOR":
            print("Rock smashes scissor. You win")
        else:
            print("Paper cover rock. you lose.")

    elif user_action == "PAPER":
        if computer_action == "ROCK":
            print("Paper covers rock. you win.")
        else:
            print("Scissor cuts paper you lose.")

    elif user_action == "SCISSOR":
        if computer_action == "PAPER":
            print("Scissor cuts paper. you win.")
        else:
            print("rock smashes scissor. you lose.")

    play_again = input("Play again (Y/N): ")
    if play_again != "Y":
        break
            
