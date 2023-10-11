import random
import sys

choices = ["rock", "paper", "scissors"]

user = input("Rock Paper Or Scissors? ").lower().strip()
comp = random.choice(choices)
choice = f"Player: {user}, Computer: {comp}"
def check(user, comp):
  if user == comp:
    return("Its a tie!")
  if user == "rock" and comp == "paper":
    return("I won!")
  else:
    return("You Won!")
  if user == "paper" and comp == "scissors":
    return("I won!")
  else:
    return("You won!")
  if user == "scissors" and comp == "rock":
    return("I won!")
  else:
    return("You won!")

print(f"{check(user, comp)}, {choice}")
