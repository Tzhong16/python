#basic index 
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

ind_ger = countries.index('germany')
print(capitals[ind_ger])

#dictionaries way
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}
print(europe) 
print(europe.keys())
print(europe['norway'])

# Add italy to europe
europe['italy'] = 'rome'

print('italy' in europe)
europe['poland'] = 'warsaw'
print(europe)

#edit europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 
          'australia':'vienna' }

europe['germany'] = 'berlin'

del(europe['australia'])

print(europe)

#the value is a dictionaries

europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
           
           
# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = { 'capital':'rome', 'population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

print(europe)

#create DataFrame with Pandas

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

import pandas as pd 

my_dict = {'country': names, 'drives_right':dr, 'cars_per_cap':cpc}

cars = pd.DataFrame(my_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

cars.index = row_labels

print(cars)

#import csv with pandas

import pandas as pd 


cars = pd.read_csv('cars.csv')

print(cars)

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars)

#subset from pandas with loc and iloc
# loc is label_based iloc is index_based

print(cars['country'])

print(cars[['country']])

print(cars[['country', 'drives_right']])

print(cars[0:3])

print(cars[3:6])

print(cars.loc['JAP'])
print(cars.iloc[2])

print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1, 6]])

print(cars.loc['MOR', 'drives_right'])

print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']]

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

print(cars.loc[:, ['cars_per_cap', 'drives_right']])
)
