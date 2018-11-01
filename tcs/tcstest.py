import numpy as np
import matplotlib
matplotlib.use("QT5Agg")
import matplotlib.pyplot as plt

# Define limit values for accerleration, velocity, position
amin_az = -1
amax_az = 1
vmin_az = -3
vmax_az = 3
pmin_az = -90
pmax_az = 450

# Set parameters of simulation
end_time =10
dt = 0.2
xview_increment = 2

# Create simulated data
tt = np.arange(0,end_time,dt) 
acc = np.linspace(-2,2,tt.size)
vel = np.linspace(-5,5,tt.size)
pos = np.linspace(-30,90,tt.size)


# Create graph figure window
fig = plt.figure(figsize=(20,9))
ax1 = plt.subplot(1,2,1)
ax2 = ax1.twinx()
ax3 = plt.subplot(1,2,2, projection = "polar")
# Enable interactive mode of graph window to allow updates
plt.ion()
plt.show()

plt.title('Azimuth Motion')
ax1.set_ylim((vmin_az-1,vmax_az+1))
ax2.set_ylim((pmin_az-1,pmax_az+1))

xview = (0,xview_increment)
ax1.set_xlim(xview)

ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Velocity / Accel [deg/s], [deg^2/s]')
ax2.set_ylabel('Position [deg]')

# Plot first data point to set legend labels
ax1.plot(tt[0], acc[0],'.g',label='acceleration')
ax1.plot(tt[0], vel[0],'.b',label='velocity')
ax2.plot(tt[0], pos[0],'.r',label='position')
ax1.legend(loc=2)
ax2.legend(loc=1)

ax1.grid(True, which="both")
for k in range(tt.size):
    xlim_old = ax1.get_xlim()
    if tt[k] >= xlim_old[1]:
    	xmax_new =  xlim_old[1] + xview_increment
    	ax1.set_xlim((0,xmax_new))
    ax1.plot(tt[k], acc[k],'+g',label='acceleration')
    ax1.plot(tt[k], vel[k],'db',label='velocity')
    ax2.plot(tt[k], pos[k],'or',label='position')
    ax3.plot(pos[k]*np.pi/180,1,'ro')
    plt.draw()
    plt.pause(dt)

# Disable interactive mode so the last show() is a blocking function call
# so we can zoom and save the figure to .png file before closing.
plt.ioff()
plt.show()