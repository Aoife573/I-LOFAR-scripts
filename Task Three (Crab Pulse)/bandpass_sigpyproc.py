#bandpass=downsampled_file.bandpass()
#bandpass.toFile("

from sigpyproc.Readers import FilReader
import matplotlib.pyplot as plt
import numpy as np

#compute the bandpass and frequency of each channel
my_bpass = FilReader("100D.32.fil").bandpass()
freqs = np.linspace(my_bpass.header.ftop, my_bpass.header.fbottom, my_bpass.size)

#plot the result
plt.plot(freqs,my_bpass)
plt.title("Bandpass")
plt.xlabel("Observing frequency (MHz)")
plt.ylabel("Power (Arbitrary units)")
plt.show()
plt.savefig("new_bandpass.png")


