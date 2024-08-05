#for GUI use tkinter
#import numpy library
#if using numpy library first number is inlcusive and last number exclusive
#if using random library first and last number are inclusive

import numpy as np

#roll dice message and random number play

msg = print('Roll the dice!')
number = np.random.randint(1,6)

print(number)

# if statement to display dice result

if number == 3:
    print('You are the winner. Play again!')
else:
    print('You loose, try again!')


