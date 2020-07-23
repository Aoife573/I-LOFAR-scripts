#!/usr/bin/python
from sigpyproc.Readers import FilReader 
import sigpyproc.Filterbank
import matplotlib.pyplot as plt
import numpy as np

file=FilReader("new.fil")
file.downsample(tfactor=500, ffactor=1, filename="test500.fil")

