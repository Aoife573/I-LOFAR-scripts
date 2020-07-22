#!/usr/bin/python

from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

x = []
y = []
z = []
with open('time.csv','r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        x.append(int(float(row[0])))
   
with open('DM.csv','r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        y.append(int(float(row[0])))
    
with open('SN.csv','r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        z.append(int(float(row[0])))
  
      
graph = plt.scatter(x, y, c=z, s = .1, cmap=plt.cm.plasma)    
cb = plt.colorbar(graph)
cb.set_label('SN')
plt.xlim(1.7266e6,1.7268e6)
plt.ylim(200,520)
plt.xlabel("time")
plt.ylabel("DM")
plt.title("SMC021_008D1.fil")
plt.savefig('/mnt/ucc2_data1/data/aoife_brennan_nuig/SMCD/test1/D.png')
plt.show()

