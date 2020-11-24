yrs = [1923,1931,1943,1952,1959,1960,1981,1982,1986,1986,1989,1992,1994,1997,2005,2009,2014,2017,2018, 2020]
import numpy as np
u = [x + 1 for x in range(len(yrs))]
import matplotlib.pyplot as plt
plt.plot(yrs,u); plt.yticks(range(0,25,5))
plt.xlabel('Year')
plt.ylabel('Cumulative Count Nobel Prizes')
plt.savefig('images/cumulative-analytical-nobels.png')
