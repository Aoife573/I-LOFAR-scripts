#!/usr/bin/python

from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import math

x = []
y = []

  
with open('Mhz.csv','r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        x.append(int(float(row[0])))
      
with open('time-averaged.csv','r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        y.append(int(float(row[0])))
        

graph = plt.scatter(x, y, s = 1, cmap=plt.cm.plasma)    

plt.xlabel("channel frequency (Mhz)")
#plt.xlim(0.0, 700)
plt.ylim (0, .0025)
plt.ylabel("time averaged frequency")
plt.title("Bandpass")
plt.savefig('/mnt/ucc2_data1/data/aoife_brennan_nuig/task3/bandpass.png')
plt.show()

