# ask user choce from r/p/s
# if not one of them, say
#   invaid choce
# else
# Print user choice and compouter choice
# then determine the winner and ask you if wants to continue
import random

choices = ('r', 'p', 's')
emojies = {'r': '🚀', 'p': '📃', 's': '✂'}

while True:
  user_choice = input(f'Rock, Paper, Scissor? (r/p/s): ').lower()
  if user_choice not in choices:
    print('Invaild choice')
    continue

  computer_choice = random.choice(choices)
  print(f'You chose {emojies[user_choice]}')
  print(f'Computer chose {emojies[computer_choice]}')

  if user_choice == 'p' and computer_choice == 'r' or \
  user_choice == 'r' and computer_choice == 'p' or \
  user_choice == "s" and computer_choice == 'p':
    print('You win!')
    break
  else:
    print('You lose!')
    not_continue = input(f'Do you want to continue? (y/n): ').lower()
    if not_continue == 'n':
      break
