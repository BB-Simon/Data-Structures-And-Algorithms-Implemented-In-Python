# ask user to roll the dice, only 2 options, yes or no,
# if no then say thanks for playing
# if user give any other options say Invalid choice
# If user say yes then show a 2 random numbers
import random

max_play = 3

while True:
  user_input = input('Roll the dice (y/n): ' )
  lower_case_user_input = user_input.lower()

  if lower_case_user_input == "n":
    print("Thanks for playing")
    break
  elif lower_case_user_input == "y":
    dice_num_1 = random.randint(1, 10) 
    dice_num_2 = random.randint(11, 100)

    print(f'({dice_num_1}, {dice_num_2})')
    max_play -=1
    print(f'You can roll the dice {max_play} times')

    if max_play == 0:
      print('Thanks for playing')
      break
  else:
    print('Invalid choice:(')
    break
