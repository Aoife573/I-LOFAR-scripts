import numpy as np 
import matplotlib.pyplot as plt 
import csv
import pandas as pd 
import sys
import os
from matplotlib import colors

mean=7824.43
rms=210400

folded_data=sys.argv[1]
data=pd.read_csv('20180921.ascii', sep='\s+', skiprows=1)

plt.figure(num=1)
i=data.iloc[:,1].values
bins=np.arange(0, intens.shape[0], 1)
phase=bins/np.max(bins)
i=(i-mean)/rms
plt.xlabel('Phase')
plt.ylabel('Intensity')
plt.title('Pulse Profile')
plt.plot(phase, i
plt.savefig('fold.png')
