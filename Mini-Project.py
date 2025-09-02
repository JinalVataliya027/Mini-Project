# Rock Paper Scissors
import random

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper, or scissors: ").lower()
comp = random.choice(choices)

print("Computer chose:", comp)

if user == comp:
    print("It's a tie!")
elif (user == "rock" and comp == "scissors") or \
     (user == "paper" and comp == "rock") or \
     (user == "scissors" and comp == "paper"):
    print("🎉 You win!")
else:
    print("❌ You lose!")
