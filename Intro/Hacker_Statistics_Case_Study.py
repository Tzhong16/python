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


##############################
#random walk
##############################

import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

print(random_walk)

#use max() to insure the step dont below 0
# 
import numpy as np
np.random.seed(123)

random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        ########## use mmax to make sure step can't go below 0################
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

#visualize the walk

import matplotlib.pyplot as plt 

plt.plot(random_walk)

plt.show()



##########################
#simulate multiples walks
##########################

import numpy as np
np.random.seed(123)

all_walks = []

for i in range(10) :

    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

print(all_walks)



#########################
#visualize all walks
########################

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

plt.plot(np_aw)
plt.show()
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

plt.plot(np_aw_t)
plt.show()


#########################
#
##########################

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

########################
#Plot the distribution
#######################

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

for i in range(1000) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

plt.hist(ends)
plt.show()
