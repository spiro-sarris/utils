import numpy as np
import matplotlib
matplotlib.use("QT4Agg")
import matplotlib.pyplot as plt

fftsize = 1024
nsamples = 1024
fs = 8e6
tt = np.arange(0,nsamples)/fs
ff = np.linspace(-fs/2,fs/2,fftsize)
ftest = 100

fp = open('demo.iq','rb')
fp.seek(0,0)
dt = np.dtype([('i',np.float32),('q',np.float32)])
data = np.fromfile(fp,dtype=dt,count=nsamples)
sigt = data['i']+1j*data['q']
sigf = np.fft.fft(sigt,fftsize)

fig = plt.figure(1)
ax1 = plt.subplot(211)
plt.plot(tt*1e3,np.real(sigt),'b')
plt.plot(tt*1e3,np.imag(sigt),'r')
plt.xlabel('Time (ms)')

ax2 = plt.subplot(212)
sigfshift = np.fft.fftshift(sigf)
plt.plot(ff/1e6,20*np.log10(np.abs(sigfshift)))
plt.xlabel('Frequency (MHz)')
plt.grid(True)
plt.show()