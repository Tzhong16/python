###################################################################
#Import data from Internet & API
##################################################################


#########################
# urllib package , request sub-package         
########################


from urllib.request import urlretrieve

import pandas as pd

url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())


#example 2: Read and open the flat  file from web by Pandas

import matplotlib.pyplot as plt
import pandas as pd

url ='https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

df = pd.read_csv(url, sep =';')

print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()


#example 3: pandas could import non-flat file from web

import pandas as pd

url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# sheetname = None : mean reading in all sheets of Excel file
xl = pd.read_excel(url, sheetname = None)

# Print the sheetnames, it will be the keys of dictionary
print(xl.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xl['1700'].head())


###########
# http request 
###########

from urllib.request import urlopen, Request

url = "http://www.datacamp.com/teach/documentation"

request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

print(type(response))

response.close()


# example 2 : use read() method to extract the 'http.client.HTTPResponse' file
from urllib.request import urlopen, Request

# Specify the url
url = "http://docs.datacamp.com/teach/"

# This packages the request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Extract the response: html
html = response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()



#############################
####requests package#########
############################

import requests

url = 'http://docs.datacamp.com/teach/'

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text, text is an attribute of r 
text = r.text

print(text)



