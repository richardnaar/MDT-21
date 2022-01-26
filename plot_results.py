import pandas as pd
import os
import glob
import pylab
import matplotlib
import numpy as np
from psychopy import core, gui
import scipy.stats

participant = 'test1'
all_participants = 1


# get the current directory
dirpath = os.getcwd()
data_dir = dirpath+'\\data'

data_names = list(filter(lambda x: x.endswith('.csv'), os.listdir(data_dir)))

# find the latest csv
data_files = glob.glob(data_dir+'\\*.csv')
latest_csv = max(data_files, key=os.path.getctime)

for name in data_names:
    if name in latest_csv:
        latest_name = name
        break

# let user to pick a file

expName = os.path.basename(__file__)
expInfo = {'all files': data_names, 'latest file': latest_name,
           'one participant': 1, 'latest': 1, 'pdf folder name': 'pictures'}

dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel

pic_dir = dirpath + '\\' + expInfo['pdf folder name']
if not os.path.exists(pic_dir):
    os.makedirs(pic_dir)


if expInfo['one participant']:
    if expInfo['latest']:
        data = pd.read_csv(latest_csv)
        pic_name = latest_name[0:-4]
    else:
        data = pd.read_csv(data_dir+'\\'+expInfo['all files'])
        pic_name = expInfo['all files'][0:-4]


# If we want to plot all the participants


def load_data(data_files):
    data = pd.DataFrame()
    for file in data_files:
        print(file)
        csv_file = pd.read_csv(file)
        csv_file = csv_file[csv_file.brush_max_dev.isna() == False]
        csv_file = csv_file[csv_file.training == False]
        data = data.append(csv_file)
        pic_name = 'all_participants'
    return data, pic_name


if not expInfo['one participant']:
    data, pic_name = load_data(data_files)

# Filter
if expInfo['one participant']:
    data = data[data.brush_max_dev.isna() == False]
    data = data[data.training == False]
# data.difficulty.astype(int)
# Do plotting

matplotlib.use('Qt5Agg')  # change this to control the plotting 'back end'
fig, ax = pylab.subplots(1, 2)
fig.set_figwidth(14)
fig.set_figheight(7)
# fig.set_dpi(200)

cols = ['red', 'blue']
var = ['brush_max_dev', 'brush_mean_dev', 'brush_draw_dur']
means = data.pivot_table(index='difficulty', values=var)

for dif in data.difficulty.astype(int).unique():
    data2plot = data[data.difficulty == dif]

    bmd_z = (data2plot.brush_max_dev-data2plot.brush_max_dev.mean()) / \
        data2plot.brush_max_dev.std()
    # bmd_z = (data.brush_mean_dev-data.brush_mean_dev.mean())/data.brush_mean_dev.std()

    bdd_z = (data2plot.brush_draw_dur-data2plot.brush_draw_dur.mean()) / \
        data2plot.brush_draw_dur.std()

    ax[dif].scatter(bmd_z, bdd_z, color=data.line_col.unique()
                    [dif], alpha=0.5)  # label="Trial"
    ax[dif].set_xlabel("Max deviance (standardized)")
    ax[dif].set_ylabel("RT (standardized)")

    leg = str()
    for i, vname in enumerate(means.columns):
        leg = leg + vname + ': ' + str(round(means[vname][dif], 3)) + '\n'
    cor = scipy.stats.spearmanr(bmd_z, bdd_z)
    leg = leg + 'Spearman r: ' + str(round(cor.correlation, 2)) + \
        ', p: ' + str(round(cor.pvalue, 3))

    ax[dif].legend(title=leg, loc='upper right')


pylab.show()

fig.savefig(pic_dir + '\\' + pic_name+".pdf")
