import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("gapminder.csv", index_col=0)

life_exp = data["life_exp"]
gdp_cap = data["gdp_cap"]

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# After customizing, display the plot
plt.show()

plt.hist(life_exp, bins=20)
plt.show()
plt.clf()
