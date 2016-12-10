########################################################
# Connect to  Database 
########################################################
# 1. create a engine connect to the file
# 

from sqlalchemy import create_engine

#the string part consisted of two parts: vendor and path, in this case is sqlite and census.sqlite, respectively
engine = create_engine('sqlite:///census.sqlite')

print(engine.table_names())

#Reflection is a automatic  process of reading the database and building the metadata based on that information

from sqlalchemy import Table

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

print(repr(census))


#example 2

census = Table('census', metadata, autoload = True, autoload_with = engine)

print(census.columns.keys())

#use metadata method to find out more table imformation like column names and type
print(repr(metadata.tables['census']))


#########################
#basic method to send query to database
#########################

stmt = 'SELECT * FROM census'

# fetchall() is use to take the data from table
results = connection.execute(stmt).fetchall()

print(results)


########################
# select methond from sqlalchemy
#######################

from sqlalchemy import select

census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census])

print(stmt)

print(connection.execute(stmt).fetchall())

# Get the first row of the results by using an index: first_row
first_row = results[0]

print(first_row)

print(first_row[0])

print(first_row['state'])


##########################
#connect to postgraSql
##########################


from sqlalchemy import create_engine


engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')


print(engine.table_names())


#################
#filter data 
#################

stmt = select([census])

stmt = stmt.where(census.columns.state == 'New York')

results = connection.execute(stmt).fetchall()

for result in results:
    print(result.age, result.sex, result.pop2008)
