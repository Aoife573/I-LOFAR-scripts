#!/bin/sh
 
for DM in $(seq 0 0.002 30); do echo
      dedisperse "20180921.fil" -d "$DM" > /mnt/ucc2_data1/data/aoife_brennan_nuig/task2/"20180921""$DM"".tim"
      seek "20180921""$DM"".tim" -fftw -pulse -s  > /mnt/ucc2_data1/data/aoife_brennan_nuig/task2/"20180921""$DM"".pls"
      rm "20180921""$DM"".tim"
      rm "20180921""$DM"".hst"
      rm "20180921""$DM"".top"

      done
done

