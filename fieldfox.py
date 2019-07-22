import os
import numpy as np

def read_sa_csv(filename):
	if(os.path.isfile(filename) is not True):
		print('ERROR: File not found')
		print('os.path.isfile(%s) = False' %filename)
		data = None
	else:
		print('Processing file %s: ' % filename)
		# Read data from CSV
		data_csv = np.genfromtxt(filename,delimiter=",",skip_header=32, skip_footer=1)
		# Select relevant values from CSV columns and create a python dictionary
		data = {}
		data['ff_Hz'] = data_csv[:,0]
		data['maxhold_dBm'] = data_csv[:,2]
		data['avg_dBm'] = data_csv[:,3]

	return(data)