
#!/bin/sh

for file in  1 2 3 4 5 6 7 8 9 A B C D; do echo  
        for DM in {0..500}
        do 
                dedisperse "SMC021_008""$file""1.fil" -d $DM > /mnt/ucc2_data1/data/aoife_brennan_nuig/SMCD/"SMC021_008""$file""1.""$DM"".tim"
                seek "SMC021_008""$file""1.""$DM"".tim" -fftw -pulse -s  > "SMC021_008""$file""1.""$DM"".pls"
                rm "SMC021_008""$file""1.""$DM"".tim"
                rm "SMC021_008""$file""1.""$DM"".prd"
                rm "SMC021_008""$file""1.""$DM"".hst"
                rm "SMC021_008""$file""1.""$DM"".top"

        done
done
