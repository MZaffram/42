import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Formation_position01.42',delimiter=',',skiprows=1)
time = np.loadtxt('time.42',delimiter=',',skiprows=1)

plt.figure()
plt.plot(time,data[:,0:3])
plt.grid(True)
plt.title('Translational Position Errors')
plt.xlabel('Time [s]')
plt.ylabel('Error [m]')
plt.legend([r'${\rm r}_x$',r'${\rm r}_y$',r'${\rm r}_z$'],loc='upper right')
plt.tight_layout()

plt.figure()
plt.plot(time,data[:,3:6])
plt.grid(True)
plt.title('Translational Velocity Errors')
plt.xlabel('Time [s]')
plt.ylabel('Error [m/s]')
plt.legend([r'${\rm v}_x$',r'${\rm v}_y$',r'${\rm v}_z$'],loc='upper right')
plt.tight_layout()

plt.figure()
plt.plot(time,data[:,6:10])
plt.grid(True)
plt.title('Command Force')
plt.xlabel('Time [s]')
plt.ylabel('Force [N]')
plt.legend([r'${\rm Frc}_x$',r'${\rm Frc}_y$',r'${\rm Frc}_z$'],loc='upper right')
plt.tight_layout()


plt.show()
