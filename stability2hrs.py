import numpy as np
import matplotlib
matplotlib.use("QT4Agg")
import matplotlib.pyplot as plt

baseband_fs=1000.0

# Read all files
dt = np.dtype([('i',np.float32),('q',np.float32)])

fp = open('/home/ssarris/sdreval/f70M_fs1K_fft128.iq','rb')
data128 = np.fromfile(fp,dtype=dt,count=-1)
fp.close()

sig128 = data128['i']+1j*data128['q']

amp128 = 20*np.log10(np.abs(sig128))

phs128 = np.angle(sig128,deg=True)

tt128 = 128*np.arange(0,sig128.size)/baseband_fs

#find sample range that represents  time 12 to 40 seconds for each trace
tmin=15
tmax=7200

rng128 = np.where((tmin <= tt128) & (tt128 <= tmax))
std_amp128 = np.std(amp128[rng128[0]])
std_phs128 = np.std(phs128[rng128[0]])
print(rng128[0].size)
print(std_amp128)
print(std_phs128)

fig = plt.figure(1)
ax1 = plt.subplot(211)
plt.title('RF Freq  = 70 MHz, fs = 1 kHz, FFT size in Legend')
plt.plot(tt128,amp128,'.',label='128')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude Difference (dB)')
plt.grid(True)
plt.ylim((5.64,5.67))
plt.xlim((tmin,tmax))

ax2 = plt.subplot(212)
plt.plot(tt128,phs128,'.',label='128')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Phase Difference (deg)')
plt.grid(True)
plt.ylim((-118.65,-118.35))
plt.xlim((tmin,tmax))
plt.show()