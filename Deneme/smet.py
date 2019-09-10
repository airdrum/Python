'''
Created on 26 Tem 2019

@author: samet.yildiz
'''
from numpy import real, imag, arange
from numpy.fft import fft, ifft
from numpy.random import randint
from commpy.modulation import QAMModem
from commpy.impairments import add_frequency_offset
import matplotlib.pyplot as plt

# System Parameters 
# Sampling Frequency (Hz)
Fs = 15.36e6 
# Frequency Offset (Hz)
delta_f = 500
# FFT Size for OFDM 
N = 1024

# Generate message bits
msg_bits = randint(0, 2, 6144)
# 64-QAM Modulation of the message bits
qam64 = QAMModem(64)
tx_sc_symbols = qam64.modulate(msg_bits)
# Add Frequency offset to the modulated symbols
rx_sc_symbols = add_frequency_offset(tx_sc_symbols, Fs, delta_f)

# Ideal 64-QAM constellation
plt.figure(1)
plt.plot(real(tx_sc_symbols), imag(tx_sc_symbols), '.b')
plt.xlabel('I-component')
plt.ylabel('Q-component')
plt.xticks(arange(-10, 12, 2))
plt.yticks(arange(-10, 12, 2))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)

# 64-QAM constellation for Single Carrier with Frequency offset
plt.figure(2)
plt.plot(real(rx_sc_symbols), imag(rx_sc_symbols), '.b', alpha=0.5)
plt.xlabel('I-component')
plt.ylabel('Q-component')
plt.xticks(arange(-10, 12, 2))
plt.yticks(arange(-10, 12, 2))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)

# Generate OFDM signal (single symbol) using modulated symbols
tx_ofdm_waveform = ifft(tx_sc_symbols)
# Add frequency offset to the OFDM signal
rx_ofdm_waveform = add_frequency_offset(tx_ofdm_waveform, Fs, delta_f)
# OFDM Demodulation to extract the 64-QAM symbols
rx_ofdm_symbols = fft(rx_ofdm_waveform)

# 64-QAM Constellation for OFDM with Frequency offset
plt.figure(3)
plt.plot(real(rx_ofdm_symbols), imag(rx_ofdm_symbols), '.b', alpha=0.6)
plt.xlabel('I-component')
plt.ylabel('Q-component')
plt.xticks(arange(-10, 12, 2))
plt.yticks(arange(-10, 12, 2))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)

plt.show()