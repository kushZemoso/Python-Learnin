import numpy as np
taxi=np.genfromtxt("nyc_taxis.csv",delimiter=',',skip_header=True)

# mean speed of the cabs
speed=taxi[:,7]/(taxi[:,8]/3600)
mean_speed=speed.mean()
print(mean_speed)

# No of rides taken in the month of feb
rides_feb=taxi[taxi[:,1]==2,1]
print(rides_feb.shape[0])

# No of rides where passengers has tipped more than 50 dollars
tipmorethan50=taxi[taxi[:,-3]>50,-3].shape[0]
print(tipmorethan50)

# No of rides where drop was Jfk airport
dropAirport=taxi[taxi[:,6]==2,6].shape[0]
print(dropAirport)