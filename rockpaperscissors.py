#!/usr/bin/env python3

import random

def main():
    print("Let's play rock paper scissors")
    user_input = input("Choose from rock, paper, or scissors: ")
    computer = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou picked {user_input}")
    print(f"I picked {computer}\n")

    if user_input == computer:
        print("It's a tie")

    elif (
        (user_input == "rock" and computer == "scissors") or
        (user_input == "paper" and computer == "rock") or
        (user_input == "scissors" and computer == "paper")
    ):
        print("Congratulations, you win!")
    else:
        print("Better luck next time, I win")
main()
