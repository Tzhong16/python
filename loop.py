##############################################
#while loop
#############################################

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
