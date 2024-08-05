#import numpy library

import numpy as np


msg = print('Roll the dice!')
number = np.random.randint(1,6)

print(number)

if number == 3:
    print('You are the winner. Play again!')
else:
    print('You loose, try again!')
