import os
import numpy as np
import matplotlib
matplotlib.use("QT5Agg")
import matplotlib.pyplot as plt
import fieldfox
#plt.style.use('dark_background')

# List of filenames to process
list_of_files_ant = [("/home/ssarris/Documents/spectrum/f0600M_14000M_az00.csv",0),
				("/home/ssarris/Documents/spectrum/f0600M_14000M_az135.csv",135),
				("/home/ssarris/Documents/spectrum/f0600M_14000M_az180.csv",180),
				("/home/ssarris/Documents/spectrum/f0600M_14000M_az225.csv",225),
				("/home/ssarris/Documents/spectrum/f0600M_14000M_az270.csv",270),
				("/home/ssarris/Documents/spectrum/f0600M_14000M_az315.csv",315),
				("/home/ssarris/Documents/spectrum/f0600M_14000M_az45.csv",45),
				("/home/ssarris/Documents/spectrum/f0600M_14000M_az90.csv",90),
				("/home/ssarris/Documents/spectrum/f0600M_2600M_az0.csv",0),
				("/home/ssarris/Documents/spectrum/f3500M_4500M_az135.csv",135),
				]

list_of_files_50ohm_term = [("/home/ssarris/Documents/spectrum/f0600M_14000M_50ohm.csv",0),
				("/home/ssarris/Documents/spectrum/f0600M_2600M_50ohm.csv",0),
				("/home/ssarris/Documents/spectrum/f3500M_4500M_50ohm.csv",0),
				]


for fileinfo in list_of_files_50ohm_term:
	# Iterate through files and process each one
	# Read data from files
	data = fieldfox.read_sa_csv(fileinfo[0])
	filename_w_ext = os.path.basename(fileinfo[0])
	filename, file_extension = os.path.splitext(filename_w_ext)
	# Make plots
	str_title = "File %s" % (filename_w_ext)
	figure_size = (10,8)
	xlabel = "Frequency [GHz]"
	ylabel = "Power [dBm] Received at SA with 50 ohm Load on Input"
	ymin = -100
	ymax = -10

	fig1 = plt.figure(os.path.basename(fileinfo[0]), figsize=figure_size)
	ax1 = plt.subplot(1,1,1)
	ax1.plot(data['ff_Hz']*1e-9, data['maxhold_dBm'],'b', label='maxhold')
	ax1.plot(data['ff_Hz']*1e-9, data['avg_dBm'],'r', label='average 1000')
	ax1.set_ylim((ymin,ymax))
	ax1.set_title(str_title)
	ax1.set_xlabel(xlabel)
	ax1.set_ylabel(ylabel)
	ax1.grid(True, which='both')
	ax1.legend(loc=1)
	plt.draw()
	plt.savefig("%s.png" % filename, format='png', bbox_inches='tight')

for fileinfo in list_of_files_ant:
	# Iterate through files and process each one
	# Read data from files
	data = fieldfox.read_sa_csv(fileinfo[0])
	
	# Scale measured power [dBm] to power flux in units of dB(W/m^2)
	# Assume antenna gain is constant across all frequency.  In general,
	# The gain vs. frequency data should be used, but for this Aaronia 60180,
	# I will approximate 5 dBi across the range of frequency
	speed_of_light_m_per_sec = 299792458
	W_per_mW = 0.001
	wavelength_m = speed_of_light_m_per_sec/data['ff_Hz']
	rx_antenna_gain_dBi = 5*np.ones(data['ff_Hz'].shape[0])
	rx_antenna_gain_linear = 10**(rx_antenna_gain_dBi/10)
	rx_antenna_effective_area_m2 = rx_antenna_gain_linear*(wavelength_m**2)/(4*np.pi) 

	power_maxhold_W = W_per_mW*(10**(data['maxhold_dBm']/10))
	power_avg_W = W_per_mW*(10**(data['avg_dBm']/10))
	
	power_flux_maxhold_W_per_m2 = power_maxhold_W/rx_antenna_effective_area_m2
	power_flux_avg_W_per_m2 = power_avg_W/rx_antenna_effective_area_m2

	# Power Flux Spectral Density (PFD)
	# Normalize flux to a reference bandwidth dB(W/m^2/REF_Hz)
	# Spectrum analyzer resolution bandwidth was set to fixed 5 MHz for the entire
	# measurement session.  In general, this value should be read from line 15 of the
	# .csv file at parameter "ResolutionBW"
	specA_resolutionBW = 5e6
	reference_bw_Hz = 5e6
	bw_scale = float(reference_bw_Hz)/float(specA_resolutionBW)

	pfd_maxhold_W_per_m2_per_BW = bw_scale*power_flux_maxhold_W_per_m2
	pfd_avg_W_per_m2_per_BW = bw_scale*power_flux_avg_W_per_m2

	pfd_maxhold_dBW_per_m2_per_BW = 10*np.log10(pfd_maxhold_W_per_m2_per_BW)
	pfd_avg_dBW_per_m2_per_BW = 10*np.log10(pfd_avg_W_per_m2_per_BW)
	
	# Prepare file name
	filename_w_ext = os.path.basename(fileinfo[0])
	filename, file_extension = os.path.splitext(filename_w_ext)
	# Make plots
	str_title = "File %s, AZ=%d [deg]" % (filename_w_ext, fileinfo[1])
	figure_size = (10,8)
	xlabel = "Frequency [GHz]"
	ylabel = "Power Flux [dBW/m^2] in %7.3f MHz BW" % (reference_bw_Hz/1e6)
	ymin = -120
	ymax = -10

	fig1 = plt.figure(os.path.basename(fileinfo[0]), figsize=figure_size)
	ax1 = plt.subplot(1,1,1)
	# ax1.plot(data['ff_Hz']*1e-9, 10*np.log10(rx_antenna_effective_area_m2),'k', label='effective area')
	# ax1.plot(data['ff_Hz']*1e-9, data['maxhold_dBm'],'g', label='maxhold specA meas')
	# ax1.plot(data['ff_Hz']*1e-9, data['avg_dBm'],'m', label='average 1000 specA meas')
	ax1.plot(data['ff_Hz']*1e-9, pfd_maxhold_dBW_per_m2_per_BW,'b', label='maxhold')
	ax1.plot(data['ff_Hz']*1e-9, pfd_avg_dBW_per_m2_per_BW,'r', label='average 1000')
	
	ax1.set_ylim((ymin,ymax))
	ax1.set_title(str_title)
	ax1.set_xlabel(xlabel)
	ax1.set_ylabel(ylabel)
	ax1.grid(True, which='both')
	ax1.legend(loc=1)
	plt.draw()
	plt.savefig("%s.png" % filename, format='png', bbox_inches='tight')

plt.show()
