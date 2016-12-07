##############################################
#while loop
#############################################
# while condition:
#     expression


#example1 
offset = 8

while offset != 0 :
    print('correcting...')
    offset = offset - 1
    print(offset)

#example2 
offset = -6

while offset != 0 :
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else :
        offset = offset + 1
    print(offset)

############################################
#for loop
############################################

# for var in seq:
#    expression 

#example1

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for iterates in areas:
    print(iterates)


#####################
#for loop over a list
#####################

# use function enumerate() 
#add index and values in the same time  with e

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

for x, y in enumerate(areas) :
    print("room " + str(x) + ": " + str(y))


#fixed the index start from 1 instead of 0 
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))


#prints out "the x is y sqm", where x is the name of the room and y is the area of the room

house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
for x, y in house:
    print("the " + x + " is " + str(y) + " sqm")o


######################
#for loop over a dictionary
######################

#for key, value in data.items() :
#      expression

#use method  items() 

europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
          
for x, y in europe.items():
    print("the capital of " + x + " is " + y ) 


######################
#for loop over Numpy Array
##########################

# for x in np.nditer(array):
#     expression

# use np.nditer() functions


import numpy as np

#np_height is a Numpy array
# end arg in print is to mesmerizing the output size
for x in np_height:
     print( str(x) + " inches", end = " " )

# np_baseball ia 2D Numpy array
for y in np.nditer(np_baseball):
    print(y, end = " ")
