import matplotlib.pyplot as plt

import numpy as np

import serial

import time


Fs = 10.0;  # sampling rate

Ts = 1.0/Fs; # sampling interval

 # time vector; create Fs samples between 0 and 1.0 sec.
x = np.zeros(100)
y = np.zeros(100) # signal vector; create Fs samples
z = np.zeros(100)
tilt = np.zeros(100)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)

for i in range(0, 100):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    line=line.split()
    print(line)
    tmp=float(line[0])
    if tmp==500:
        break
    x[i]=float(line[0])
    y[i]=float(line[1])
    z[i]=float(line[2])
    tilt[i]=float(line[3])
if(i!=0):
    t = np.arange(0,10,10/i)
    n=len(t)
else:
    t= np.arange(0,10,0.1)
    n=100

x=x[0:n]
y=y[0:n]

z=z[0:n]
tilt=tilt[0:n]
fig, ax = plt.subplots(2, 1)
ax[0].plot(t,x)
ax[0].plot(t,y)
ax[0].plot(t,z)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].legend(['x','y','z'])
ax[1].stem(t,tilt)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('tilt')
plt.show()

s.close()