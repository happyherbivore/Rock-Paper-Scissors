rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors] 
import random

user = input("What do you choose? Rock, Paper, or Scissors?\n").lower()
options = ["rock", "paper", "scissors"]

if user not in options:
  print("Invalid term entered.")

else:

  user_choice = options.index(user)
  comp_choice = random.randint(0, 2)
  comp = options[comp_choice]

  # player output
  print(f"You chose {user}:\n{game_images[user_choice]}")
  # comp output
  print(f"Computer chose {comp}:\n{game_images[comp_choice]}")


  # evaluate winner
  user_wins = "Congratulations, you win!"
  if user == comp:
    print("\nYou tie.")

  elif user == "rock":
    if comp == "paper":
      user_wins = "You Lose. Better luck next time."
    print(user_wins)

  elif user == "paper":
    if comp == "scissors":
      user_wins = "You Lose. Better luck next time."
    print(user_wins)

  elif user == "scissors":
    if comp == "rock":
      user_wins = "You Lose. Better luck next time."
    print(user_wins)
