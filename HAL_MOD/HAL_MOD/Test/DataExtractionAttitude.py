import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Formation_attitude01.42',delimiter=',',skiprows=1)
time = np.loadtxt('time.42',delimiter=',',skiprows=1)

plt.figure()
plt.plot(time,data[:,0:3])
plt.grid(True)
plt.title('Angular Position Errors')
plt.xlabel('Time [s]')
plt.ylabel('Error [rad]')
plt.legend([r'${\rm \theta}_x$',r'${\rm \theta}_y$',r'${\rm \theta}_z$'],loc='upper right')
plt.tight_layout()

plt.figure()
plt.plot(time,data[:,3:6])
plt.grid(True)
plt.title('Angular Velocity Errors')
plt.xlabel('Time [s]')
plt.ylabel('Error [rad/s]')
plt.legend([r'${\rm \omega}_x$',r'${\rm \omega}_y$',r'${\rm \omega}_z$'],loc='upper right')
plt.tight_layout()

plt.figure()
plt.plot(time,data[:,6:10])
plt.grid(True)
plt.title('Command Torque')
plt.xlabel('Time [s]')
plt.ylabel('Torque [Nm]')
plt.legend([r'${\rm Trq}_x$',r'${\rm Trq}_y$',r'${\rm Trq}_z$'],loc='upper right')
plt.tight_layout()


plt.show()
