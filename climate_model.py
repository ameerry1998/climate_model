import numpy as np
import matplotlib.pyplot as plt 
import time
import decimal

t = 0
temperature_planet = 200
temperature_atmosphere = 250

epsilon = 0.25
dt = 60*10
heat_capacity = 1E5
insolation = 1370
sigma = 5.67E-8
planet_radius = 6.4E6

circle = np.pi*planet_radius**2.0
sphere = 4*np.pi*planet_radius**2.0


plt.scatter(y=temperature_planet,x=t,s=2, color="red")
plt.ion()
plt.xlabel("Time (S)")
plt.ylabel("Temperature (K)")
plt.legend(loc='upper left')
plt.show()

print(temperature_planet)
while True:
	temp_plan = dt*(circle*insolation + sphere* epsilon*sigma* temperature_atmosphere**4.0) - sphere*sigma*temperature_planet**4.0/heat_capacity*sphere
	t += dt
	'''plt.scatter(y=temp_plan,x=t,s=2, color="red")'''
	print(temp_plan)
	plt.pause(0.005)
	time.sleep(0.05)