import numpy as np
import scipy.signal

def todB(linearVal):
	return 10*np.log10(linearVal)

def toLinear(dBVal):
	return 10**(dBVal/10)
	
def fft_maxhold(sigt_1D, fft_size=1024, window=False):
	# Caluclate number of columns to split the long 1-D array.
	nrows = int(np.ceil(float(sigt_1D.size) / fft_size))
	
	# Zero pad the end of the array to prepare for reshape dimensions
	sigt_1D_padded = np.pad(sigt_1D,(0,int(nrows*fft_size-sigt_1D.size)),'constant')
	# Reshape the 1-D array into 2-D array with each column the 
	# same length as FFT sizes
	sigt_2D = np.reshape(sigt_1D_padded, (nrows, fft_size))
	
	# Generate a window function for apodization
	if(window==True):
		w = scipy.signal.windows.blackmanharris(fft_size)
	else:
		w = np.ones(fft_size)

	# Tile the window across all rows and apply window
	w_2D = np.tile(w,(nrows,1))
	sigt_2D_w = w_2D*sigt_2D

	# Calculate FFT of each column
	sigf_2D = np.fft.fft(sigt_2D_w, fft_size, axis=1)
	
	# Calculate magnitude in dB
	sigf_maxhold = np.sum(np.abs(sigf_2D),axis=0)/nrows/fft_size
	sigf_maxhold_mag = 10*np.log10(sigf_maxhold)
	
	return sigf_maxhold_mag