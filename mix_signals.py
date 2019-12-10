import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

my_dpi = 100

def fn(time):
    return 3 * np.sin(3/4*time) * np.cos(2*time)

plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)
time = np.linspace(0,5*2*np.pi,500)
mixed = fn(time)

plt.axis('equal')
plt.plot(time, mixed)
plt.savefig("time_signal.svg")

samples_time = np.linspace(0,50,num=100)
samples = fn(samples_time)
plt.figure()
plt.scatter(samples_time, samples)


plt.figure(3)
fft = np.fft.fft(samples)
freq = np.fft.fftfreq(samples_time.shape[-1])
N = len(samples)
f = np.linspace(0, 100, len(samples))
print(freq)
plt.bar(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N, width=0.2)
plt.savefig("frequencies.svg")
plt.show()

