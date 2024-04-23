# write a rock, paper, scissors game

# import random module
import random


# define choices for game
choices = ["rock", "paper", "scissors"]

# make user type input
# renmae user to user_choice
user_choice = input("Type r, p, or s for rock, paper, or scissors: ")
user_choice = user_choice.lower()
if user_choice == "r" or user_choice == "rock":
    user_choice = "rock"
elif user_choice == "p" or user_choice == "paper":
    user_choice = "paper"
elif user_choice == "s" or user_choice == "scissors":
    user_choice = "scissors"
else:
    print("Invalid input! You have not entered a valid choice. Try again.")
    exit()
# make user_choice lowercase
user_choice = user_choice.lower()
# declare another user which is computer
computer = random.choice(choices)
# write a play_game function to handle all the logic
def play_game(user_choice, computer):
    # if user_choice is equal to computer
    # once game start print choice of two
    print(f"你選擇了 {user_choice}。電腦選擇了 {computer}。")
    if user_choice == computer:
        print(f"兩位玩家都選擇了 {user_choice}。平手！")
    # if user_choice is rock
    elif user_choice == "rock":
        if computer == "scissors":
            print("石頭砸碎剪刀！你贏了！")
        else:
            print("紙包石頭！你輸了。")
    # if user_choice is paper
    elif user_choice == "paper":
        if computer == "rock":
            print("紙包石頭！你贏了！")
        else:
            print("剪刀剪破紙！你輸了。")
    # if user_choice is scissors
    elif user_choice == "scissors":
        if computer == "paper":
            print("剪刀剪破紙！你贏了！")
        else:
            print("石頭砸碎剪刀！你輸了。")
    # if user_choice is not valid
    else:
        print("無效輸入！你沒有輸入石頭、紙或剪刀，請再試一次。")


# call play_game in def __main__:
if __name__ == "__main__":
    play_game(user_choice, computer)
