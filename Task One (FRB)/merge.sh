#!/bin/sh


for DM in {0..500}; do echo  

                tail -n+2 "SMC021_008D1.""$DM"".pls" >> "SMC021_finished.""$DM"".pls"
                cat "SMC021_finished.""$DM"".pls"  >> "SMC021_008D1_finished.pls"
                #tail +2 "SMC021_00831_finished.pls"
                rm "SMC021_finished.""$DM"".pls"
done
