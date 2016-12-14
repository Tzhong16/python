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

file = 'titanic.csv'

d = np.recfromcsv(file)

print(d[:3])





#############################################################
#Pandas  --- import file as data.frame
############################################################


# example 1 
import pandas as pd

file = 'titanic.csv'

df = pd.read_csv(file)

print(df.head())




# example 2

file = 'digits.csv'

data = pd.read_csv(file, nrows = 5, header = None)

# Build a numpy array from the DataFrame: data_array
data_array = data.values

print(type(data_array))


# example 3 

import matplotlib.pyplot as plt

file = 'titanic_corrupt.txt'

# sep arg is a pandas version of delimiter
#comment takes characters that comments occur after in the file, which in this case is '#'
#na_values takes a list of strings to recognize as NA/NaN
data = pd.read_csv(file, sep= '\t', comment='#', na_values= ['Nothing'])

print(data.head())

pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()



##############################################################
#import data from database
##############################################################

# common database: PostgreSQL , MySql, SQLite
# STEP: 
#	1. import package and function
#	2. create engine
#	3. connect to engine
#	4. query to database
#	5. save query as a dataframe
#	6. close connection


from sqlalchemy import create_engine
import pandas as pd
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

table_names = engine.table_names()

print(table_names)

# Open engine connection: con
con = engine.connect()

rs = con.execute('select * from Album')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

con.close()

print(df.head())




#########################
#customize the SQL query
########################

from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')

# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('select LastName, Title from Employee')
    df = pd.DataFrame(rs.fetchmany(size = 3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

print(df.head())


