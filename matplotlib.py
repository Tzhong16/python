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


plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.show()

# Scatter plot
plt.scatter(gdp_cap, life_exp)

plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

tick_val = [1000,10000,100000]
tick_lab = ['1k','10k','100k']

plt.xticks(tick_val, tick_lab)
plt.show()

import numpy as np

np_pop = np.array(pop)

np_pop = np_pop * 2

plt.scatter(gdp_cap, life_exp, s = np_pop)

plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.show()
plt.clf()

plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
plt.grid(True)
plt.show()
plt.clf()
