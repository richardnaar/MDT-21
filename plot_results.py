import pandas as pd
import os
import pylab
import matplotlib
import numpy as np
from psychopy import core

matplotlib.use('Qt5Agg')  # change this to control the plotting 'back end'
pylab.figure(figsize=[12, 8])


# get the current directory
dirpath = os.getcwd()
data_dir = dirpath+'\\data'

data_files = list(filter(lambda x: x.endswith('.csv'), os.listdir(data_dir)))


def load_data(data_dir, data_files):
    data = pd.DataFrame()
    for file in data_files:
        csv_file = pd.read_csv(data_dir+'\\'+file)
        csv_file[csv_file.brush_max_dev.isna() == False]
        data = pd.concat([data, csv_file], axis=1)


load_data(data_dir, data_files)
