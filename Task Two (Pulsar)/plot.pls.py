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
cb.set_label('SN'))
plt.xlabel("time")
plt.ylabel("DM")
plt.title("20180921.pls")
plt.savefig('/mnt/ucc2_data1/data/aoife_brennan_nuig/task2/20180921.png')
plt.show()
