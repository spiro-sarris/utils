import numpy as np
import matplotlib
matplotlib.use("QT4Agg")
import matplotlib.pyplot as plt

fftsize = 1024
nsamples = 1024
fs = 8e6
tt = np.arange(0,nsamples)/fs
ff = np.linspace(-fs/2,fs/2,fftsize)
ftest = 0
phi0 = np.pi/4

sigt = np.exp(1j*(2*np.pi*ftest*tt+phi0))
sigf = np.fft.fft(sigt,fftsize)

fig = plt.figure(1)
ax1 = plt.subplot(211)
plt.title('demo')
plt.plot(tt*1e3,np.real(sigt),'b')
plt.plot(tt*1e3,np.imag(sigt),'r')
plt.xlabel('Time (ms)')
plt.grid(True)

ax2 = plt.subplot(212)
sigfshift = np.fft.fftshift(sigf)
plt.plot(ff/1e6,20*np.log10(np.abs(sigfshift)))
plt.xlabel('Frequency (MHz)')
plt.grid(True)
plt.show()