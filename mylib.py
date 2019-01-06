import numpy as np

def todB(linearVal):
	return 10*np.log10(linearVal)

def toLinear(dBVal):
	return 10**(dBVal/10)
	