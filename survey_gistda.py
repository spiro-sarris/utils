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
	filename_w_ext = os.path.basename(fileinfo[0])
	filename, file_extension = os.path.splitext(filename_w_ext)
	# Make plots
	str_title = "File %s, AZ=%d [deg]" % (filename_w_ext, fileinfo[1])
	figure_size = (10,8)
	xlabel = "Frequency [GHz]"
	ylabel = "Power [dBm] Received at SA using 5 dBi Test Antenna"
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

plt.show()
