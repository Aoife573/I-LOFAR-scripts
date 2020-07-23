#!/usr/bin/python

import numpy as np 
import matplotlib.pyplot as plt 
import csv
import pandas as pd 
import sys
import os
from matplotlib import colors

fig1=plt.figure(1)
ax1=fig1.add_subplot(111)

names=["DM", "Duration", "time", "S/N", "length"]
data=pd.read_csv("finished.pls", sep='\s+', skiprows=1, names=names)
index=data[data["S/N"] <= 5].index
data=data.drop(index, inplace=False) 
DM=data["DM"].values
time=(data["time"].values)/8000
SN=data["S/N"].values
width=2**(data["Duration"].values)
pul=ax1.scatter(time, DM, s=(width)/100, c=SN, cmap = "plasma") 
#vmin=np.min(SN), vmax=np.max(SN)) 

ax1.set_xlabel("time (s)")
ax1.set_ylabel("DM")
ax1.set_title("png.pls")
#ax1.set_xlim(9,13)
#ax1.set_ylim(0,6)
cbar=fig1.colorbar(pul)
cbar.set_label("S/N")
plt.savefig("pls.final.png")

