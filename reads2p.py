import matplotlib.pyplot as plt
import numpy as np

fname = "/home/ssarris/Documents/arr/atten30db_real_imag.csv"
csv = np.genfromtxt(fname,delimiter=",",skip_header=24, skip_footer=1)


ff = csv[:,0]
trace = csv[:,1]+1j*csv[:,2]
trace_dB = 20*np.log10(np.abs(trace))

plt.plot(ff, trace_dB)
plt.xlim((400e6,6e9))
plt.ylim((-35,-25))
plt.xlabel('time (s)')
plt.ylabel('S21r (mV)')
plt.title('')
plt.grid(True)
#plt.savefig("test.png")
plt.show()