# Comparisons
print(True == False)

print(-5 * 15 != 75)

print('pyscript' == 'PyScript')

print(True == 1)

x = -3 * 6
print(x >= -10)

y = "test"
print( 'test' <= y)

print(True > False)

#array comparison
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

print(my_house >= 18)

print(my_house < your_house)

######################################################
# logical_and() , logical_or(), logical_not() in Numpy
######################################################

#basic comparison
my_kitchen = 18.0
your_kitchen = 14.0

print(my_kitchen > 10 and my_kitchen < 18)

print(my_kitchen < 14 or my_kitchen > 17)

print(my_kitchen * 2 < your_kitchen * 3 )

#array comparison with Numpy
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

print(np.logical_or(my_house>18.5, my_house<10))

print(np.logical_and(my_house < 11 , your_house <11))

################################################
# if , elif , else
################################################
#example1 
room = "kit"
area = 14.0

if room == "kit" :
    print("looking around in the kitchen.")

if area > 15 :
   print("big place!")

#example2
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

if area > 15 :
    print("big place!")
else:
    print('pretty small.')

#example3

room = "bed"
area = 14.0

if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice")
else :
    print("pretty small.")

#subset data with logical operator
#example1 
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

dr = cars['drives_right']

# alternative methods: sel=cars[cars['drive_right']]
sel = cars[dr]

print(sel)

#example2

import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac= cars[many_cars]

print(car_maniac)

# example3

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

import numpy as np

cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

print(medium)
