import random
option = ("rock","scissors","paper")
user_choice = input("choose rock , paper or scissors")
computer_choice = random.choice(option)
print("you chose:",user_choice)
print("computer chose", computer_choice)
if user_choice == computer_choice:
    print('its a tie')
    print('its a tie')
elif user_choice == "rock" and computer_choice == "scissors":
    print('rock smashes scissors u win')
elif user_choice == 'paper' and computer_choice == "rock":
    print('paper covers rock u win')
elif user_choice == 'scissors' and computer_choice == "paper":
    print('scissors cuts paper u win')
else:
    print("you lose (LOSERRRRR)")