import numpy as np
import matplotlib
matplotlib.use("QT4Agg")
import matplotlib.pyplot as plt

baseband_fs=1000.0

# Read all files
dt = np.dtype([('i',np.float32),('q',np.float32)])

fp = open('f100M_fs1K_fft32.iq','rb')
data32 = np.fromfile(fp,dtype=dt,count=-1)
fp.close()

fp = open('f100M_fs1K_fft64.iq','rb')
data64 = np.fromfile(fp,dtype=dt,count=-1)
fp.close()

fp = open('f100M_fs1K_fft128.iq','rb')
data128 = np.fromfile(fp,dtype=dt,count=-1)
fp.close()

fp = open('f100M_fs1K_fft256.iq','rb')
data256 = np.fromfile(fp,dtype=dt,count=-1)
fp.close()

fp = open('f100M_fs1K_fft512.iq','rb')
data512 = np.fromfile(fp,dtype=dt,count=-1)
fp.close()

fp = open('f100M_fs1K_fft1024.iq','rb')
data1024 = np.fromfile(fp,dtype=dt,count=-1)
fp.close()

sig32 = data32['i']+1j*data32['q']
sig64 = data64['i']+1j*data64['q']
sig128 = data128['i']+1j*data128['q']
sig256 = data256['i']+1j*data256['q']
sig512 = data512['i']+1j*data512['q']
sig1024 = data1024['i']+1j*data1024['q']

amp32 = 20*np.log10(np.abs(sig32))
amp64 = 20*np.log10(np.abs(sig64))
amp128 = 20*np.log10(np.abs(sig128))
amp256 = 20*np.log10(np.abs(sig256))
amp512 = 20*np.log10(np.abs(sig512))
amp1024 = 20*np.log10(np.abs(sig1024))

phs32 = np.angle(sig32,deg=True)
phs64 = np.angle(sig64,deg=True)
phs128 = np.angle(sig128,deg=True)
phs256 = np.angle(sig256,deg=True)
phs512 = np.angle(sig512,deg=True)
phs1024 = np.angle(sig1024,deg=True)

tt32 = 32*np.arange(0,sig32.size)/baseband_fs
tt64 = 64*np.arange(0,sig64.size)/baseband_fs
tt128 = 128*np.arange(0,sig128.size)/baseband_fs
tt256 = 256*np.arange(0,sig256.size)/baseband_fs
tt512 = 512*np.arange(0,sig512.size)/baseband_fs
tt1024 = 1024*np.arange(0,sig1024.size)/baseband_fs

#find sample range that represents  time 12 to 40 seconds for each trace
tmin=12
tmax=40
rng32 = np.where((tmin <= tt32) & (tt32 <= tmax))
rng64 = np.where((tmin <= tt64) & (tt64 <= tmax))
rng128 = np.where((tmin <= tt128) & (tt128 <= tmax))
rng256 = np.where((tmin <= tt256) & (tt256 <= tmax))
rng512 = np.where((tmin <= tt512) & (tt512 <= tmax))
rng1024 = np.where((tmin <= tt1024) & (tt1024 <= tmax))

std_amp32 = np.std(amp32[rng32[0]])
std_phs32 = np.std(phs32[rng32[0]])
print(rng32[0].size)
print(std_amp32)
print(std_phs32)

std_amp64 = np.std(amp64[rng64[0]])
std_phs64 = np.std(phs64[rng64[0]])
print(rng64[0].size)
print(std_amp64)
print(std_phs64)

std_amp128 = np.std(amp128[rng128[0]])
std_phs128 = np.std(phs128[rng128[0]])
print(rng128[0].size)
print(std_amp128)
print(std_phs128)

std_amp256 = np.std(amp256[rng256[0]])
std_phs256 = np.std(phs256[rng256[0]])
print(rng256[0].size)
print(std_amp256)
print(std_phs256)

std_amp512 = np.std(amp512[rng512[0]])
std_phs512 = np.std(phs512[rng512[0]])
print(rng512[0].size)
print(std_amp512)
print(std_phs512)

std_amp1024 = np.std(amp1024[rng1024[0]])
std_phs1024 = np.std(phs1024[rng1024[0]])
print(rng1024[0].size)
print(std_amp1024)
print(std_phs1024)

fig = plt.figure(1)
ax1 = plt.subplot(211)
amp_plot_offset =0.02
plt.title('RF Freq  = 100 MHz, fs = 1 kHz, FFT size in Legend')
plt.plot(tt32,amp32-1,'.',label='32')
plt.plot(tt64,amp64-1-2*amp_plot_offset,'.',label='64')
plt.plot(tt128,amp128-1-2*amp_plot_offset,'.',label='128')
plt.plot(tt256,amp256-1-3*amp_plot_offset,'.',label='256')
plt.plot(tt512,amp512-1-4*amp_plot_offset,'.',label='512')
plt.plot(tt1024,amp1024-1-5*amp_plot_offset,'.',label='1024')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude Difference (dB)')
plt.grid(True)
plt.ylim((1.35,1.55))
plt.xlim((tmin,tmax))

ax2 = plt.subplot(212)
phs_offset=0.08
plt.plot(tt32,phs32-0.1,'.',label='32')
plt.plot(tt64,phs64-0.1-2*phs_offset,'.',label='64')
plt.plot(tt128,phs128-0.05-3*phs_offset,'.',label='128')
plt.plot(tt256,phs256-0.1-4*phs_offset,'.',label='256')
plt.plot(tt512,phs512-1.37-0.1-5*phs_offset,'.',label='512')
plt.plot(tt1024,phs1024-0.1-6*phs_offset,'.',label='1024')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Phase Difference (deg)')
plt.grid(True)
plt.ylim((-154.2,-153.6))
plt.xlim((tmin,tmax))
plt.show()