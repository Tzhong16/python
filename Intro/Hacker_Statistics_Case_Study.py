#Case study: Hacker Statistics

# random package is a sub-package in numpy


##########################
#random float
##########################

# seed()   rand()

import numpy as np

np.random.seed(123)

print(np.random.rand())


# randint()  :generate integers randomly
# Roll the dice

import numpy as np
np.random.seed(123)

print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))



# Use if -- elif -- else to determine the next moved
import numpy as np
np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

print(dice)
print(step)



