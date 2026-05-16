# I have number of 20
# user will guess the correct with max 10 tries
# if user enter not a number say please enter a valid num
# if the user num if greater the my number say Too high!
# if lesser then say Too low!
# if near to my number then say almost ther, guess again

import re

tries = 10
num = 20

while True:
  user_input = input(f'Guess the number between 1 to 100: ')
  try:
    user_num = int(user_input)
    
    gap = num - user_num

    if user_num == num:
      print('Congratulation!, You guessed the number')
      break
    elif user_num == num + 1:
      print('You are almost there, guess again')
    elif user_num >= num + 2:
      print('Too high!')
    elif user_num == num - 1:
      print('You\'re almost there. Guess again')
    elif user_num <= num - 2:
      print('Too low!')
  except:
    print('Please enter a valid number')
