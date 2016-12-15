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


##################################################################
# Scrap the web, extract the structured date from HTML
#################################################################


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


#############################
#BeautifulSoup 
#############################

# parse and extract structured data from HTML

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

print(pretty_soup



##example 2 : Getting the text

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title

print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()

print(guido_text)



#example 3 : getting the hyperlinks

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

for link in a_tags:
    print(link.get('href'))




#########################################################
# API   &    JSONs  
#########################################################


# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
     #access a value in a dictionary using the syntax: dictionary[key]
    print(k + ': ', json_data[k])






###############################
#pulling data from API  
##############################


import requests

url = 'http://www.omdbapi.com/?t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

print(r.text)




#example 2 


import requests

url = 'http://www.omdbapi.com/?t=social+network'

r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])


# example 3 

import requests

url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)



#####################################################
#Mock authentication  credentials  
#####################################################


import tweepy


access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

