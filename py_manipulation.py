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


#example 2 
stmt = select([census])

stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)


##################
#conjunction like and_() , or_(), not_() 
#####################


from sqlalchemy import and_

stmt = select([census])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)


#####################
#order_by()
####################

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

stmt = stmt.order_by(census.columns.state)

results = connection.execute(stmt).fetchall()

print(results[:10])


#######
#desc()
######
# wrapped with desc()

from sqlalchemy import desc

stmt = select([census.columns.state])

rev_stmt = stmt.order_by(desc(census.columns.state))

rev_results = connection.execute(rev_stmt).fetchall()

print(rev_results[:10])




#order_by multiple columns

stmt = select([census.columns.state, census.columns.age])

stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

results = connection.execute(stmt).fetchall()

print(results[:20])


#######################
# count(), sum(), scalar()
#########################

#scalar() for getting just the value of a query that returns only one row and column

# Build a query to count the distinct states values: stmt
stmt = select([func.count(census.columns.state.distinct())])

distinct_state_count = connection.execute(stmt).scalar()

print(distinct_state_count)


# example 2

from sqlalchemy.sql import func

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

stmt = stmt.group_by(census.columns.state)

results = connection.execute(stmt).fetchall()

print(results)

# Print the keys/column names of the results returned

print(results[0].keys())


#

from sqlalchemy.sql import func

pop2008_sum = func.sum(census.columns.pop2008).label('population')

stmt = select([census.columns.state, pop2008_sum])

stmt = stmt.group_by(census.columns.state)

results = connection.execute(stmt).fetchall()

print(results)

print(results[0].keys())



#feed a ResultProxy directly into a pandas DataFrame
import pandas as pd

df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

print(df)



# Import Pyplot as plt from matplotlib
from  matplotlib import pyplot as plt 

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()




####################################
#Advanced SQLAlchemy query
####################################

from sqlalchemy import create_engine

# Create an engine to the census database
# dialect and driver:   mysql+pymysql://   ;   username:password : student:datacamp  ; host and port : @courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/  ; database_name: census
# dialect+driver://username:password@host:port/database_name
 
engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

print(engine.table_names())


# Build query to return state names by population difference from 2008 to 2000: stmt
stmt = select([census.columns.state, (census.columns.pop2008-census.columns.pop2000).label('pop_change')])

stmt = stmt.group_by(census.columns.state)

# Append order by for pop_change descendingly: stmt
stmt = stmt.order_by(desc('pop_change'))

stmt = stmt.limit(5)

results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}-{}'.format(result.state, result.pop_change))



#Determining the Overall Percentage of Females


from sqlalchemy import case, cast, Float

# Build an expression to calculate female population in 2000
female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0))

# Cast an expression to calculate total population in 2000 to Float
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)

# Build a query to calculate the percentage of females in 2000: stmt
stmt = select([female_pop2000 / total_pop2000* 100])

# Execute the query and store the scalar result: percent_female
percent_female = connection.execute(stmt).scalar()

# Print the percentage
print(percent_female)
