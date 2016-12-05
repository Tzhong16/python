print(year[-1])
print(pop[-1])

import matplotlib.pyplot as plt

plt.plot(year, pop)
plt.show()

#gdp_cap refer to GDP per capita, life_exp refer to life expectancy
print(gdp_cap[-1])
print(life_exp[-1])

plt.plot(gdp_cap, life_exp)

plt.show()

plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

plt.show()

import matplotlib.pyplot as plt

#pop refer to populations for the countries in 2007
plt.scatter(pop, life_exp)

plt.show()


plt.hist(life_exp)
plt.show()
plt.clf(

plt.hist(life_exp, bins=5)
plt.show()
plt.clf()

plt.hist(life_exp, bins=20)
plt.show()
plt.clf()

