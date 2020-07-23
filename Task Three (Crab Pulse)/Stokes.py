#! usr/bin/python3
####

import numpy as np
import matplotlib.pyplot as plt
import os
import sys


path ="/mnt/ucc4_data2/data/David/crab_extracted_pulses"
file0 = open(path+"/crab_giant_pulses0_2020-03-17T19:14:20,_17901920.rawudp", 'rb')
file1 = open(path+"/crab_giant_pulses1_2020-03-17T19:14:20,_17901920.rawudp", 'rb')
file2 = open(path+"/crab_giant_pulses2_2020-03-17T19:14:20,_17901920.rawudp", 'rb')
file3 = open(path+"/crab_giant_pulses3_2020-03-17T19:14:20,_17901920.rawudp", 'rb')
#stokesI=(file0**2)+(file1**2)+(file2**2)+(file3**2)
file0 = np.fromfile(file0, dtype = np.int8)
file1 = np.fromfile(file1, dtype = np.int8)
file2 = np.fromfile(file2, dtype = np.int8)
file3 = np.fromfile(file3, dtype = np.int8)

#header "file0"
file0 = file0.reshape(8203104, 488)
file1 = file1.reshape(8203104, 488)
file2 = file2.reshape(8203104, 488)
file3 = file3.reshape(8203104, 488)

#I = np.empty[(2050776, 488)]
I = np.empty_like(file0, dtype = np.int32)
U = np.empty_like(file0, dtype = np.int32)
V = np.empty_like(file0, dtype = np.int32)
Q = np.empty_like(file0, dtype = np.int32)


#f =  np.arange(start=0, stop=197.558593875, step=.1953125)

#def  time_delay(f):
 #  DM = 56.77118
#   time = ((4149)*(DM))/(f)^2

#for i in I(range(2050776), size = 1000000):
 #  I = (np.square(file0).astype(np.int32)) + (np.square(file1).astype(np.int32)) + (np.square(file2).astype(np.int32)) + (np.square(file3).astype(np.int32))
    
#for c in chunked_iterable(range(14), size=4):
chunksize=250000
for i in range(32):
   I[i*chunksize:(i+1)*chunksize,:] =(
   np.square(file0 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)) +
   np.square(file1 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)) +
   np.square(file2 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)) +
   np.square(file3 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)))
#chunksize=250000

#chunksize=250000
#for i in range(32):
  # U[i*chunksize:(i+1)*chunksize,:] = 2*(
  # (np.square(file0 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)))*
  # (np.square(file1 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)))*
  # (np.square(file2 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)))*
 #  (np.square(file3 [i * chunksize: (i+1) * chunksize, :].astype(np.int32))))
#chunksize=250000
#for i in range(32):
 #  V[i*chunksize:(i+1)*chunksize,:] =(
  # (np.square(file0 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)))*
   #(np.square(file3 [i * chunksize: (i+1) * chunksize, :].astype(np.int32))) +
   #(np.square(file2 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)))*
   #(np.square(file1 [i * chunksize: (i+1) * chunksize, :].astype(np.int32))))
#chunksize=250000
#for i in range(32):
 #  Q[i*chunksize:(i+1)*chunksize,:] =(
  # (np.square(file0 [i * chunksize: (i+1) * chunksize, :].astype(np.int32))) +
  # (np.square(file1 [i * chunksize: (i+1) * chunksize, :].astype(np.int32))) -
   #(np.square(file2 [i * chunksize: (i+1) * chunksize, :].astype(np.int32))) -
   #(np.square(file3 [i * chunksize: (i+1) * chunksize, :].astype(np.int32))))

#graph = plt.imshow(I, cmap="plasma", aspect = "auto")
#cbar = plt.colorbar(graph)
#plt.savefig("1test.png")
#np.save("U.file", U)
graph1 = plt.imshow(U, cmap="plasma", aspect = "auto")
cbar=plt.colorbar(graph1)
plt.xlabel("Freqeuncy Channel")
plt.title("Stokes I")
plt.savefig("I.png")

#graph3 = plt.imshow(V, cmap="plasma", aspect = "auto")
#cbar=plt.colorbar(graph3)
#plt.savefig("3test.png")

#graph4 = plt.imshow(Q, cmap="plasma", aspect = "auto")
#cbar=plt.colorbar(graph4)
#plt.savefig("4test.png")




