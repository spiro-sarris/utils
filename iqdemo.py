import numpy as np
import matplotlib
matplotlib.use("QT4Agg")
import matplotlib.pyplot as plt
import scipy.signal
import mylib

# Settings for time domain voltage signal
fs = 1e6						# sample rate
t_end = 4000e-6					# length of time
nsamples = t_end*fs				# number of samples total
tt = np.arange(0,nsamples)/fs	# time values in seconds
phi0 = 0						# phase initial
freq = 50e3					# frequency

# Settings for frequency domain spectrum
fftsize = 1000					# number of FFT spectrum bins
ff_kHz = (np.linspace(0,fs,fftsize))/1e3

# Generate a complex-valued signal
sig_c = np.exp(1j*(2*np.pi*freq*tt+phi0))

# Generate a real-valued signal
sig_r = np.cos(2*np.pi*freq*tt+phi0)

# Use Hilbert transform to generate complex-valued analytical signal
sig_h = scipy.signal.hilbert(sig_r)

# FFT spectrum of each signal
SIG_C = mylib.fft_maxhold(sig_c, fftsize, window=False)
SIG_R = mylib.fft_maxhold(sig_r, fftsize, window=False)
SIG_H = mylib.fft_maxhold(sig_h, fftsize, window=False)

# FFTSHIFT wrap negative frequencies around to the left
SIG_C_SHIFT = np.fft.fftshift(SIG_C)
SIG_R_SHIFT = np.fft.fftshift(SIG_R)
SIG_H_SHIFT = np.fft.fftshift(SIG_H)

# Generate a unit step function to show magic of Hilbert Transform
unitstep = np.zeros(fftsize)
unitstep[fftsize/2-1:-1]=1

# Settings for graph figure windows
tt_usec = tt*1e6
n_cycles = 3 					# Number of cycles
tt_end = n_cycles/freq*1e6 		# end time in microseconds
n_end = t_end*fs 				# last sample
figure_size = (8, 4)			# Size in pixels / 100

# Plot graphs
fig = plt.figure(1, figsize=figure_size)
ax1 = plt.subplot(111)
plt.title('Complex-Valued Signal. freq = 50 kHz, fs = 1 MHz')
plt.plot(tt_usec,np.real(sig_c),'k--')
plt.plot(tt_usec,np.real(sig_c),'bo', label='I')
plt.plot(tt_usec,np.imag(sig_c),'k--')
plt.plot(tt_usec,np.imag(sig_c),'ro', label='Q')
plt.xlim((0,tt_end))
plt.xlabel('Time (us)')
plt.grid(True)
plt.legend(loc=3)

fig = plt.figure(2, figsize=figure_size)
ax1 = plt.subplot(111)
plt.title('Real-Valued Signal. freq = 50 kHz, fs = 1 MHz')
plt.plot(tt_usec,sig_r,'k--')
plt.plot(tt_usec,sig_r,'bo', label='I')
plt.xlim((0,tt_end))
plt.xlabel('Time (us)')
plt.grid(True)
plt.legend(loc=3)

fig = plt.figure(3, figsize=figure_size)
ax1 = plt.subplot(111)
plt.title('Analytical signal from Hilbert Transform. freq = 50 kHz, fs = 1 MHz')
plt.plot(tt_usec,np.real(sig_h),'k--')
plt.plot(tt_usec,np.real(sig_h),'bo', label='I')
plt.plot(tt_usec,np.imag(sig_h),'k--')
plt.plot(tt_usec,np.imag(sig_h),'ro', label='Q')
plt.xlim((0,tt_end))
plt.xlabel('Time (us)')
plt.grid(True)
plt.legend(loc=3)

fig = plt.figure(4, figsize=figure_size)
ax1 = plt.subplot(111)
plt.title('FFT Spectrum of Complex-Valued Signal')
plt.plot(ff_kHz, SIG_C)
plt.xlabel('frequency(kHz)')
plt.xlim((ff_kHz[0],ff_kHz[-1]))
plt.grid(True)

fig = plt.figure(5, figsize=figure_size)
ax1 = plt.subplot(111)
plt.title('FFT Spectrum of Real-Valued Signal')
plt.plot(ff_kHz, SIG_R)
plt.xlabel('frequency(kHz)')
plt.xlim((ff_kHz[0],ff_kHz[-1]))
plt.grid(True)

fig = plt.figure(6, figsize=figure_size)
ax1 = plt.subplot(111)
plt.title('FFT Spectrum of Hilbert Transformed Real Signal')
plt.plot(ff_kHz, SIG_H)
plt.xlabel('frequency(kHz)')
plt.xlim((ff_kHz[0],ff_kHz[-1]))
plt.grid(True)

fig = plt.figure(7,figsize=figure_size)
ax1 = plt.subplot(111)
plt.title('Step Function for Hilbert Transfor')
plt.plot(ff_kHz,2*unitstep)
plt.xlabel('Frequency(kHz)')
plt.xlim((ff_kHz[0],ff_kHz[-1]))
plt.grid(True)

# Show all plots
plt.show()