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
