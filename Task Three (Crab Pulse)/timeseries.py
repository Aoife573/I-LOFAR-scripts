
#/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

fig1=plt.figure(1)
ax1=fig1.add_subplot(111)


names=["Time", "S/N"]
data=pd.read_csv("finished.tim", sep='\s+', skiprows=0, names=names) 
time=data["Time"].values
SN=data["S/N"].values


pul=ax1.plot(time, SN)
ax1.set_xlabel("Time (s)")
#ax1.set_xlim(0, 5)
#ax1.set_ylim(15000, 22000)
ax1.set_ylabel("S/N)")
ax1.set_title("timeseries")
plt.savefig("time.png")







