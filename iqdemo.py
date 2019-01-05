import numpy as np
import matplotlib
matplotlib.use("QT4Agg")
import matplotlib.pyplot as plt
import scipy.signal


fs = 1e6
t_end = 40e-6
nsamples = t_end*fs

tt = np.arange(0,nsamples)/fs
phi0 = 0

freq = 50e3

# Generate a complex-valued signal
sigct = np.exp(1j*(2*np.pi*freq*tt+phi0))
fig = plt.figure(1)
ax1 = plt.subplot(111)
plt.title('Complex-Valued Signal. freq = 50 kHz, fs = 1 MHz, ')
plt.plot(tt*1e6,np.real(sigct),'k--')
plt.plot(tt*1e6,np.real(sigct),'bo', label='I')
plt.plot(tt*1e6,np.imag(sigct),'k--')
plt.plot(tt*1e6,np.imag(sigct),'ro', label='Q')
plt.xlabel('Time (us)')
plt.grid(True)
plt.legend(loc=3)

# Generate a real-valued signal
sigrt = np.cos(2*np.pi*freq*tt+phi0)
fig = plt.figure(2)
ax1 = plt.subplot(111)
plt.title('Real-Valued Signal. freq = 50 kHz, fs = 1 MHz, ')
plt.plot(tt*1e6,np.real(sigct),'k--')
plt.plot(tt*1e6,np.real(sigct),'bo', label='I')
plt.xlabel('Time (us)')
plt.grid(True)
plt.legend(loc=3)

# Use Hilbert transform to generate complex-valued analytical signal
sighct = scipy.signal.hilbert(sigrt)
fig = plt.figure(3)
ax1 = plt.subplot(111)
plt.title('Analytical Signal from Hilbert Transform. freq = 50 kHz, fs = 1 MHz, ')
plt.plot(tt*1e6,np.real(sighct),'k--')
plt.plot(tt*1e6,np.real(sighct),'bo', label='I')
plt.plot(tt*1e6,np.imag(sighct),'k--')
plt.plot(tt*1e6,np.imag(sighct),'ro', label='Q')
plt.xlabel('Time (us)')
plt.grid(True)
plt.legend(loc=3)

# Show all plots
plt.show()