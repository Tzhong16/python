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

# enumerate()
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



