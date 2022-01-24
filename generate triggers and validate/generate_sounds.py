# generate sounds

import itertools
import numpy as np
import wavio
import os

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)  # set as a current dir
snd_dir = _thisDir + '\\output'  #

if not os.path.exists(snd_dir):
    os.makedirs(snd_dir)

frex = [110, 330, 554, 784, 1046]  # frequencies
# sound parameters
rate = 44100    # samples per second
T = 0.5     # sample duration (seconds)
t = np.linspace(0, T, round(T*rate), endpoint=False)  # time


def compute_waveforms(t, subset):
    x_sum = np.zeros(len(t))
    indx = list()
    for f in subset:
        indx.append(frex.index(f))
        # Compute waveforms
        x = np.sin(2*np.pi * f * t)
        x_sum = x_sum+x
    return x_sum, indx


def find_bin_name(indx):
    bin_list = np.zeros(len(frex))
    bin_list[indx] = 1
    bin_n = ''
    for juku in bin_list:
        bin_n += str(int(juku))
    return bin_n

# start_end = ['1', '0'] # start, end
# position = ['1', '0'] # fb, brush
# difficulty = ['1', '0'] # difficult, easy
# outlier = ['01', '11', '10']  # same, greater, less


stuff = frex
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        if frex[-1] in subset or frex[-2] in subset:
            x_sum, indx = compute_waveforms(t, subset)
            bin_name = find_bin_name(indx)
            wavio.write(snd_dir+"\\"+bin_name+'.wav', x_sum, rate, sampwidth=1)
            print(bin_name)
            print(subset)
