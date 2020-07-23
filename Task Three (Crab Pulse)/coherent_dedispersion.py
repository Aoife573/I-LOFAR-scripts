#! usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt



path="/mnt/ucc4_data2/data/David/crab_extracted_pulses/"
file0 = open(path+"/crab_giant_pulses0_2020-03-17T19:14:20,_17901920.rawudp", 'rb')
file1 = open(path+"/crab_giant_pulses1_2020-03-17T19:14:20,_17901920.rawudp", 'rb')
file2 = open(path+"/crab_giant_pulses2_2020-03-17T19:14:20,_17901920.rawudp", 'rb')
file3 = open(path+"/crab_giant_pulses3_2020-03-17T19:14:20,_17901920.rawudp", 'rb')

file0 = np.fromfile(file0, dtype=np.int8)
file1 = np.fromfile(file1, dtype=np.int8)
file2 = np.fromfile(file2, dtype=np.int8)
file3 = np.fromfile(file3, dtype=np.int8)
I = np.empty_like(file0, dtype=np.int32)

#chunksize=16000000
#for i in range(256):
 #   I[i*chunksize:(i+1)*chunksize] =(np.square(file0[i * chunksize: (i+1) * chunksize].astype(np.int32)) + np.square(file1[i * chunksize: (i+1) * chunksize].astype(np.int32)) + np.square(file2[i * chun$
  #  np.square(file3[i * chunksize: (i+1) * chunksize].astype(np.int32)))

chunksize=250000
for i in range(32):
   I[i*chunksize:(i+1)*chunksize,:] =(
   np.square(file0 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)) +
   np.square(file1 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)) +
   np.square(file2 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)) +
   np.square(file3 [i * chunksize: (i+1) * chunksize, :].astype(np.int32)))


I.tofile("I.fil", format="%f")
f = np.linspace(197.55859375, 102.44140625, 488) 
#f =  np.arange(start=0, stop=197.558593875, step=.1953125)

def  time_delay(f):
   DM = 56.77118
   time = ((4149)*(DM))*(1.0/(np.square(f[0])-1.0/(np.square(f)))
   return time
for i in range(1, 488):
    file0[:, i] = (file0[:, i]+time(f[i])).astype(np.int32)
    file1[:, i] = (file0[:, i]-time(f[i])).astype(np.int32)
    file2[:, i] = (file0[:, i]-time(f[i])).astype(np.int32)
    file3[:, i] = (file0[:, i]-time(f[i])).astype(np.int32)



graph = plt.imshow(I, cmap="plasma", aspect="auto")
plt.title("Incoherent Dedispersion")
cbar=plt.colorbar(graph)
cbar.set_label("Stokes_I")
plt.xlabel("Frequency")
plt.ylabel("Time")
plt.savefig("Incoherent_dedisp_I.png")
