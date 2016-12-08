# import Excel, SAS, MATLAP, Stata file, pickled file  etc. 

########################################################
# pickled file
#######################################################

import pickle 

# The second arg 'rb' in open() is refer to 'read only'  and 'binary' 
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

print(d)

print(type(d))




##########################################################
#Excel file
###########################################################

import pandas as pd

file = 'battledeath.xlsx'

xl = pd.ExcelFile(file)

print(xl.sheet_names)

#after get the sheet names, load the sheet into a varible

df1 = xl.parse('2004')

print(df1.head())

# select sheet by index
df2 = xl.parse(0)

print(df2.head())




# example 2, more arg setting when importing file

# skip the first row and giving the new column names
df1 = xl.parse( 0, skiprows= [0], names= ['Country', 'AAM due to War (2002)'])

print(df1.head())

#pase only the fist column with a new name
df2 = xl.parse( 1, parse_cols= [0], skiprows= [0], names= ['Country'])

print(df2.head())


