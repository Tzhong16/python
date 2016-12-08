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





##############################################################
# SAS file
###############################################################

from sas7bdat import SAS7BDAT

with SAS7BDAT('sales.sas7bdat') as file:
     df_sas = file.to_data_frame()

print(df_sas.head())

pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

################################################################
# Stata file 
###############################################################

import pandas as pd

df = pd.read_stata('disarea.dta')

print(df.head())

pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()


#################################################################
# HDF5 file
##################################################################

# HDF5 Store large amount of numeric data

import numpy as np
import h5py

file = 'LIGO_data.hdf5'

data = h5py.File(file, 'r')

print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)




# Check out keys of group
group = data['strain']
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()


######################################################################
# MATLAP
#####################################################################


import scipy.io

mat = scipy.io.loadmat('albeck_gene_expression.mat')

print(type(mat))


import scipy.io
import matplotlib.pyplot as plt
import numpy as np

print(mat.keys())

print(type(mat['CYratioCyt']))

print(np.shape(mat['CYratioCyt']))

data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()



