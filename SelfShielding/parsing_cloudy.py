import numpy as np
import matplotlib.pyplot as plt

def parse_Schaye_values(inputfile):
	Te,hden,eden,dr = [],[],[],[]
	HI,HII,H2 = [],[],[]
	HeI,HeII,HeIII = [],[],[]
	pressure,zone = [],[]

	idx_count = 0

	with open(inputfile) as f:
	    for line in f:
		if line.startswith(" #### "):
        		words = line.split()
        		print words
			zone = np.append(zone,float(words[1]))
        		Te = np.append(Te,float(words[2].split(':')[1]))
        		hden = np.append(hden,float(words[3].split(':')[1]))
        		eden = np.append(eden,float(words[4].split(':')[1]))
        		dr = np.append(dr,float(words[7].split(':')[1]))
        		idx_count = 1
        	elif idx_count == 1:
        		words = line.split()
        		HI = np.append(HI,float(words[1]))
        		HII = np.append(HII,float(words[2]))
        		H2 = np.append(H2,float(words[8]))
        		idx_count = 2
        	elif idx_count == 2:
        		words = line.split()
        		HeI = np.append(HeI,float(words[1]))
        		HeII = np.append(HeII,float(words[2]))
        		HeIII = np.append(HeIII,float(words[3]))
        		idx_count = 3
        	elif idx_count ==3:
        		idx_count = 4
        	elif idx_count == 4:
        		words = line.split()
        		pressure = np.append(pressure,float(words[4]))
        		idx_count = 0
		else:
			pass

	cloudy_vals = {}
	cloudy_vals['Te'] = Te
	cloudy_vals['hden'] = hden
	cloudy_vals['eden'] = eden
	cloudy_vals['dr'] = dr
	cloudy_vals['HI'] = HI
	cloudy_vals['HII'] = HII
	cloudy_vals['H2'] = H2
	cloudy_vals['HeI'] = HeI
	cloudy_vals['HeII'] = HeII
	cloudy_vals['HeIII'] = HeIII
	cloudy_vals['pressure'] = pressure
	cloudy_vals['zone'] = zone

	return cloudy_vals



