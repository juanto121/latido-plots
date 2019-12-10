import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

my_dpi = 100

plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)
time = np.linspace(0,2*np.pi,100)
periodic_signal = np.sin(3*time)
plt.axis('equal')
plt.plot(time, periodic_signal)
plt.axis('off')
plt.savefig("time_signal.svg")

#plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)
x = np.linspace(0,2*np.pi,100)
a = np.cos(x) + 1j * np.sin(x)
#plt.axis('equal')
#plt.scatter(a.real, a.imag)

plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)
gt = periodic_signal * a
plt.axis('equal')
plt.scatter(gt.real, gt.imag)

plt.show()
