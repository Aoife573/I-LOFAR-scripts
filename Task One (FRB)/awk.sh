#!/bin/sh

awk '{if (NR>1 && $4>6) print$0}'  SMC021_00811_finished.pls  >>  1.pls
awk '{print $1}' "SMC021_008D1_finished.pls"  >>  DDM.csv 
awk '{print $3}' "SMC021_008D1_finished.pls"  >>  Dtime.csv 
awk '{print $4}' "SMC021_008D1_finished.pls"  >>  DSN.csv 

