import numpy as np
import matplotlib
matplotlib.use("QT4Agg")
import matplotlib.pyplot as plt

baseband_fs=1000.0
fftsize =1024
recordsize=8
readoffset_sec=20

result_fs=baseband_fs/fftsize
seconds_record = 90
nsamples = int((seconds_record-readoffset_sec)*result_fs)-1
print(nsamples)
print(result_fs)
print(recordsize*np.ceil(readoffset_sec*result_fs))

tt = readoffset_sec+np.arange(0,nsamples)/result_fs

fp = open('/home/ssarris/stability/f100M_fs1K_fft1024.iq','rb')
fp.seek(recordsize*np.ceil(readoffset_sec*result_fs),0)
dt = np.dtype([('i',np.float32),('q',np.float32)])
data = np.fromfile(fp,dtype=dt,count=nsamples)
sigt = data['i']+1j*data['q']
sigt_mag = 20*np.log10(np.abs(sigt));
sigt_phs = np.angle(sigt,deg=True);
std_mag = np.std(sigt_mag)
std_phs = np.std(sigt_phs)
print(std_mag)
print(std_phs)

fig = plt.figure(1)
ax1 = plt.subplot(211)
plt.title('RF Freq  = 100 MHz, fs = 1 kHz, FFT size = 1024')
plt.plot(sigt_mag,'r.')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude Difference (dB)')
plt.grid(True)
ax2 = plt.subplot(212)
plt.plot(sigt_phs,'g.')
plt.xlabel('Time (s)')
plt.ylabel('Phase Difference (deg)')
plt.grid(True)
plt.show()