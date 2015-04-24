import numpy as np
import math

gamma = 5./3.
G = 6.67259e-9 #cm3 g-1 s-2
k = 1.380658e-16 #ergs K-1
m_H = 1.6605402e-24 #g
A_H = 1.00794
A_He = 2.0

def mu_mass(cloudy_vals):
	A = A_H*(cloudy_vals['HI']*cloudy_vals['hden'])+A_He*0.1*cloudy_vals['hden']*(cloudy_vals['HeI']+cloudy_vals['HeII'])
	B = cloudy_vals['HI']*cloudy_vals['hden'] + 0.1*cloudy_vals['hden']*(cloudy_vals['HeI']+cloudy_vals['HeII']) + cloudy_vals['eden']
	return A/B

def compute_jeans_column(cloudy_vals):
	##should return a column density in cm^-2 because all of the fundamental constans are in CGS
	mu = mu_mass(cloudy_vals)
	A = np.sqrt((math.pi*gamma*k)/(mu*G*m_H**2.))
	B = (1.-0.24)**0.5
	return A*B*np.sqrt(cloudy_vals['hden'])*np.sqrt(cloudy_vals['Te'])



