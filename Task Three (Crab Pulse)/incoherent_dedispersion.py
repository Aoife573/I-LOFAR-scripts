#!/usr/bin/python
from sigpyproc.Readers import FilReader 
import sigpyproc.Filterbank
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#compute the bandpass and frequency of each channel
fil = FilReader("test500.fil")
tim = fil.dedisperse(56.75).toFile(filename="test500.tim")
print(tim)
