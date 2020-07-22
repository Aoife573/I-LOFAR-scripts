#!/usr/bin/python

from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import math

x = []
y = []
z = []


  
with open('period.csv','r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        x.append(int(float(row[0])))
      
with open('DM.prd.csv','r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        y.append(int(float(row[0])))
       
with open('SN.prd.csv','r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        z.append(int(float(row[0])))
       

x = np.array(x, dtype=np.float32)
y = np.array(y, dtype=np.float32)
z = np.array(z, dtype=np.float32)

graph = plt.scatter(x1, y, c=z, s = 1, cmap=plt.cm.plasma)    
cb = plt.colorbar(graph)
cb.set_label('S/N')
plt.xlabel("period (ms)")
plt.ylabel("DM")
plt.title("20180921.prd")
plt.savefig('/mnt/ucc2_data1/data/aoife_brennan_nuig/SIGtest/prd_final.png')
plt.show()
