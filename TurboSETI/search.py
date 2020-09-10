
from turbo_seti.find_doppler.find_doppler import FindDoppler
import os
import glob

filelist = glob.glob('*chop.fil')
out_directory = './'
for file in filelist:

    # Execute turboSETI in the terminal
    console = 'turboSETI ' + file + ' -M 2 -s 6 -o ' + out_directory
    os.system(console)
