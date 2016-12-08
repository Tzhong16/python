#import data to python

# find out the files in your dictionary
# ! is to get the whole system shell access

! ls


#################################################
# plain file
#################################################
# Open a file: file
file = open('moby_dick.txt', mode = 'r')

print(file.read())

#check if the file closed
print(file.closed)

file.close()

print(file.closed)


# use with to read file line by line 

with open('moby_dick.txt') as file:
    print(file.readline())   # read first line
    print(file.readline())   # read sec line 
    print(file.readline())   # read third line


#############################################
# flat file
############################################

# #############
#Numpy package
##############

# 1. Numpy Array is strong in storing numeric data 
# 2. essential for other packages, like  scikit-learn


##########
# loadtxt()
#########
# work with single datatype
# example 1
import numpy as np

file = 'digits.csv'

digits = np.loadtxt(file, delimiter=',')

print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()


# example 2
import numpy as np

file = 'digits_header.txt'

data = np.loadtxt(file, delimiter='\t', skiprows= 1, usecols= [0, 2])

print(data)


#example 3

file = 'seaslug.txt'

data = np.loadtxt(file, delimiter='\t', dtype=str)

print(data[0])

data_float = np.loadtxt(file, delimiter = '\t', dtype=float, skiprows=1)

print(data_float[9])

plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

###############
#genfromtxt()
##############

# work with  mixed datatypes

# with genfromtxt function,have to define the delimiter = , names = , dtype = based on the case
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)  # None in dtype mean import datatype as what they import 

#get the ‘Fare’ column  
data['Fare']


###############
#recfromtxt()
##############
# work with mixed dataypes 
# recfromtxt() have already set the delimiter as ',' ; names = True; dtype = None by Default


