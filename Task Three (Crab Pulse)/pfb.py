#adapted code orginally written by Danny Price

#! usr/bin/python3
import numpy as np
import scipy
from scipy.signal import firwin, freqz, lfilter
import matplotlib.pyplot as plt
import os
import sys

def data():
    path="/mnt/ucc4_data2/data/David/crab_extracted_pulses/"

    file0 = open(path+"/crab_giant_pulses0_2020-03-17T19:25:13,_17901936.rawudp", 'rb')
    file1 = open(path+"/crab_giant_pulses1_2020-03-17T19:25:13,_17901936.rawudp", 'rb')
    file2 = open(path+"/crab_giant_pulses2_2020-03-17T19:25:13,_17901936.rawudp", 'rb')
    file3 = open(path+"/crab_giant_pulses3_2020-03-17T19:25:13,_17901936.rawudp", 'rb')

    file0 = np.fromfile(file0, dtype = np.int8)
    file1 = np.fromfile(file1, dtype = np.int8)
    file2 = np.fromfile(file2, dtype = np.int8)
    file3 = np.fromfile(file3, dtype = np.int8)

    x_real = file0.reshape(-1, subbands)
    x_imag = file1.reshape(-1, subbands)
    y_real = file2.reshape(-1, subbands)
    y_imag = file3.reshape(-1, subbands)

    chunksize = 600000
    x_complex = np.empty_like(x_real).astype(np.complex64)
    y_complex = np.empty_like(x_real).astype(np.complex64)
    for i in range(chunks):
        x_complex[i*chunksize: (i+1)*chunksize, :]=x_real[i*chunksize: (i+1)*chunksize, :] + (x_imag[i*chunksize: (i+1)*chunksize, :]*1j)
        y_complex[i*chunksize: (i+1)*chunksize, :]=y_real[i*chunksize: (i+1)*chunksize, :] + (y_imag[i*chunksize: (i+1)*chunksize, :]*1j)

    return x_complex, y_complex

def input(t_start, t_stop, sample_rate, x, y):
    
    samp_start=int(t_start/sample_rate)
    samp_stop = int(t_stop/sample_rate)
    x = x[samp_start : samp_stop, :]
    y = y[samp_start : samp_stop, :]
    return y
    return x

def db(x):
    return 10*np.log10(x)
def generate_win_coeffs(M, P, window_fn="hamming"):
    win_coeffs = scipy.signal.get_window(window_fn, M*P)
    sinc       = scipy.signal.firwin(M * P, cutoff=1.0/P, window="rectangular")
    win_coeffs *= sinc
    return win_coeffs

def pfb_fir_frontend(x, win_coeffs, M, P):
    W = x.shape[0] // M // P
    x_p = x.reshape((W*M, P)).T
    h_p = win_coeffs.reshape((M, P)).T
    x_summed = np.zeros((P, M*W-M + 1)).astype(np.complex64)
    for t in range(0, M*W-M + 1):
        x_weighted = x_p[:, t:t+M] * h_p
        x_summed[:, t] = x_weighted.sum(axis=1).astype(np.complex64)
    return x_summed.T

def fft(x_p, P, axis=1):
    return np.fft.fft(x_p, P, axis=axis)

def pfb_filterbank(x, win_coeffs, M, P):
    x = x[:int(len(x)//(M*P))*M*P] 
    x_fir = pfb_fir_frontend(x, win_coeffs, M, P)
    x_pfb = fft(x_fir, P)
    return x_pfb
def I(x, y):
    x_chan = abs(x)
    y_chan = abs(y)
    I = np.empty_like(x_chan, dtype=np.int32)
    chunksize = 600000
    for i in range(256):
        I[i*chunksize:(i+1)*chunksize] =(
        np.square(y_chan[i * chunksize: (i+1) * chunksize, :].astype(np.int32)) +
        np.square(x_chan[i * chunksize: (i+1) * chunksize, :].astype(np.int32)))

    return I

def pfb_spectrometer(x, n_taps, n_chan, n_int, window_fn="hamming"):

    M = n_taps
    P = n_chan
    win_coeffs = generate_win_coeffs(M, P, window_fn)
    pg = np.sum(np.abs(win_coeffs)**2)
    win_coeffs /= pg**.5 
    x_pfb = pfb_filterbank(x, win_coeffs, M, P)
    x_psd = np.real(x_pfb * np.conj(x_pfb))
    x_psd = x_psd[:np.round(x_psd.shape[0]//n_int)*n_int]
    x_psd = x_psd.reshape(x_psd.shape[0]//n_int, n_int, x_psd.shape[1])
    x_psd = x_psd.mean(axis=1)
    return x_psd

if __name__ == "__main__":
    import pylab as plt
    import seaborn as sns
    sns.set_style("white")
    def plot():
        x, y = data()
        x_data = x_input(1., 2., 5.12*(10**(-6)), x)
        y_data = y_input(1., 2., 5.12*(10**(-6)), y)

        x_psb1 = pfb_spectrometer(x_data[:, 0], n_taps, n_chan, n_int, window_fn="hamming")
        y_psb1 = pfb_spectrometer(y_data[:, 0], n_taps, n_chan, n_int, window_fn="hamming")

        x_array = np.zeros(shape=(x_psb1.shape[0], x_data.shape[1]*n_chan))
        y_array = np.zeros(shape=(y_psb1.shape[0], y_data.shape[1]*n_chan))
        for i in range(x_data.shape[1]):
            x = x_data[:, i]
            y = y_data[:, i]
            x_i = pfb_spectrometer(x, n_taps, n_chan, n_int, window_fn="hamming")
            y_i = pfb_spectrometer(y, n_taps, n_chan, n_int, window_fn="hamming")
            x_i = x_array[:, i*n_chan: (i+1)*n_chan]
            y_i = y_array[:, i*n_chan: (i+1)*n_chan]
        stokes = I(x_array, y_array)
        return stokes  

        plt.imshow(db(stokes), cmap='plasma', aspect='auto')
        plt.colorbar()
        plt.xlabel("Channel")
        plt.ylabel("Time")
        plt.savefig("StokesI.png")
