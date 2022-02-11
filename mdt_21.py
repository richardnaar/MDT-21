# MDT 2021

# %% IMPORT MODULES
# Additional modules will be loaded further into the script in relation
# to the eye-tracking and sound presentation
# meeldetuletus, veendu, et näeksid enda silmi anduri peegelduses

from __future__ import absolute_import, division
import validation as val  # used for calibration and validation
import cart_dist as cd  # this is used to find mouse distance from the closest line
from psychopy import sound, gui, visual, core, data, event, clock
from psychopy.constants import (NOT_STARTED)
import math
# from tkinter import E

from psychopy.platform_specific.win32 import FALSE
import vas  # the visual analog scale

import os  # handy system and path functions
import numpy as np  # whole numpy lib is available, prepend 'np.'
import pandas as pd  # whole pandas lib is available, prepend 'pd.'
import random
import psychopy

from psychopy import locale_setup
from psychopy import prefs

prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'


psychopy.useVersion('latest')

# %% DEFINE VARIABLES AND PREPARE DATA HANDLERS

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)  # set as a current dir

# Get information about this run
psychopyVersion = '2021.2.3'
expName = os.path.basename(__file__)
expInfo = {'participant': 'test', 'error tolerance': 20, 'length tolerance percent': 40,
           'fb mode': ['type A', 'type B'],  'triggers': '1', 'escape key': 'escape', 'disp cond': 0,
           'dif baseline min': -0.1, 'easy baseline min': 0.05, 'point uncertinty': 0.1, 'outlier distance': 0.086,
           'easy lines n': 4, 'diff lines n': 6, 'line length min': 0.15, 'line length max': 0.25, 'tracker': list(['tobii', 'mouse', 'none'])}

dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
expInfo['date'] = data.getDateStr()  # add a simple timestamp

filename = _thisDir + os.sep + \
    u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=__file__,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)

# Initialize mouse position data file
dataDir = _thisDir + '\\data\\'
filename2 = expInfo['participant'] + '-positions' + expInfo['date'] + '.txt'

# Prepare mouse position data file
with open(dataDir+filename2, 'a') as file_object:
    file_object.write('participant' + ';' + 'cond_table_id' + ';' + 'training' + ';' + 'trial_repaet' + ';' + 'difficulty' + ';' + 'outlier' + ';' 'block_n' + ';'
                      'local_trial_n' + ';' + 'start_xy' + ';' + 'end_xy' + ';' + 'mouse_x' + ';' + 'mouse_y' + ';' + 'lengths' + '\n')


# %% SETUP THE WINDOW AND CLOCKS
# Will set size equal to full screen but full screen False for now
# Otherwise will resize the window in the calibration
# After calibration the fullscr will be set to True
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# Aspect ratio - will be used to find horisontal position of the fb points
aspect = win.size[0]/win.size[1]


# Store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameRate = round(expInfo['frameRate'])
else:
    frameRate = 60  # could not measure, so guess

# Clocks
drawClock = core.Clock()
globalClock = core.Clock()

# %% PRAPARE EYE-TRACKING

# Calibration routine and start recording
if not expInfo['tracker'] == 'none':
    # Eye tracker to use ('mouse', 'eyelink', 'gazepoint', or 'tobii')
    results = val.calibrate(win, expInfo['tracker'])

    thisExp.addData('eye_passed', results['passed'])
    thisExp.addData('failed_pos_count',
                    results['positions_failed_processing'])
    thisExp.addData('eye_units', results['reporting_unit_type'])
    thisExp.addData('eye_min_error', results['min_error'])
    thisExp.addData('eye_max_error', results['max_error'])
    thisExp.addData('eye_mean_error', results['mean_error'])

    if expInfo['tracker'] == 'tobii':
        # Import needed modules
        import tobii_research as tr

        import time
        import csv

        # Find eye trackers
        found_eyetrackers = tr.find_all_eyetrackers()
        # Select first eye tracker
        my_eyetracker = found_eyetrackers[0]

        gaze_list = []

        # Create call back to get gaze data
        def gaze_data_callback(gaze_data):
            gaze_list.append([gaze_data['system_time_stamp'],
                              gaze_data['device_time_stamp'],
                              gaze_data['left_gaze_point_on_display_area'],
                              gaze_data['left_gaze_point_validity'],
                              gaze_data['left_pupil_diameter'],
                              gaze_data['left_pupil_validity'],
                              gaze_data['right_gaze_point_on_display_area'],
                              gaze_data['right_gaze_point_validity'],
                              gaze_data['right_pupil_diameter'],
                              gaze_data['right_pupil_validity']])

        # Start getting gaze data
        my_eyetracker.subscribe_to(
            tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

# Will be used to save the eye data


def save_eyeData():
    if expInfo['tracker'] == 'tobii':
        # stop getting gaze data
        my_eyetracker.unsubscribe_from(
            tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

        # load csv module and write gaze data to disk
        with open(filename+'_et.csv', 'w', newline='') as f:
            w = csv.writer(f, delimiter=",")
            # add header for data selected in callback
            w.writerow(['system_time', 'tracker_time',
                        'left_gaze_pos', 'left_gaze_validity', 'left_pupil_diameter', 'left_pupil_validity',
                        'right_gaze_pos', 'right_gaze_validity', 'right_pupil_diameter', 'right_pupil_validity'])

            # iterate all items
            for row in gaze_list:
                # write row in csv
                w.writerow(row)


def save_timeStamps(event_name):
    if expInfo['tracker'] == 'tobii':
        thisExp.addData(event_name+'_in_sys_time_at_tracker',
                        tr.get_system_time_stamp())
        thisExp.addData(event_name+'_in_py_time',
                        globalClock.getTime())


# PREPARE TEXTS
txt_dic = {}
for txtStim in range(4):
    txt_dic['def'+str(txtStim)] = visual.TextStim(win=win, name='text'+str(txtStim),
                                                  text='juku', font='Arial', pos=(0, 0),
                                                  height=0.04, wrapWidth=1.25, ori=0,
                                                  color='white', colorSpace='rgb', opacity=.75,
                                                  languageStyle='LTR', depth=-1.0)

# Additional text to blocks table
end_text = 'Suurt tänu osalemast! Eksperiment on läbi.'
odd_text = 'Kui miski tundus sulle selle katse juures imelik, pane see siia kirja \n (Jätkamiseks vajuta paremat hiireklahvi...)'

reminder_text = '\n\nPea meeles, et oluline on nii täpsus kui kiirus.'

# Used to draw text in the draw and main loops


def draw_text(text2draw, textElement, click_next, isTraining):
    mouse = event.Mouse(win=win)
    buttons = [0, 0, 0]
    textElement.text = text2draw
    textElement.pos = (0, 0)
    frameCount = 0
    # win.flip()
    flip_on_screen()
    brush.reset()
    brush.status = NOT_STARTED

    theseKeysBreak = event.getKeys('space')
    break_out = False
    while not break_out:
        theseKeysBreak = event.getKeys('space')
        if isTraining and len(theseKeysBreak):
            break_out = True
        elif not isTraining and hovering(click_next, mouse) and sum(buttons):
            break_out = True
        mouse = event.Mouse(win=win)
        if frameCount > 3:
            if not isTraining:
                click_next.draw()
            textElement.draw()
        # win.flip()
        flip_on_screen()
        buttons = mouse.getPressed()
        theseKeys = event.getKeys(keyList=expInfo['escape key'])
        frameCount += 1
        if len(theseKeys):
            core.quit()


# Dictionary of text positions
text_pos = {'intro': (0.7, -0.35), 'distance': (-0.5, 0.42), 'timer': (-0.5, 0.38),
            'middle': (0, 0), 'middle_high':  (0, 0.42), 'bar_high': (-0.65, 0.35), 'bar_mid': (-0.65, 0), 'bar_low': (-0.65, -0.35),
            'slf_txt': (0, 0.2), 'slf_low': (-0.45, -0.25), 'slf_high': (0.45, -0.25)}


# %% TRIGGERS

if expInfo['triggers'] == '1':
    from pygame import mixer
    mixer.init()

    snd_dir = _thisDir + '\\sounds\\'  # folder with the experimental pictures

    start_end = ['1', '0']  # start, end
    position = ['1', '0']  # fb, brush
    difficulty = ['1', '0']  # difficult, easy
    outlier_str = ['01', '11', '10']  # same, greater, less

    mixer.init()
    snd_dic = {}
    for s in start_end:
        for p in position:
            for d in difficulty:
                for o in outlier_str:
                    snd_dic[s+p+d+o] = sound.Sound(
                        snd_dir+s+p+d+o+'.wav', secs=-1, stereo=False, hamming=True, name=s+p+d+o)
                    snd_dic[s+p+d+o].setVolume(1.0)


def sound_trigger(event_name):
    if expInfo['triggers'] == '1':
        snd_dic[event_name].play()


# %% COLOURS
# Pepare line colours
col_list = ['red', 'blue']
random.shuffle(col_list)
col_dict = {'red': [230, 25, 75], 'blue':  [0, 120, 200]}

# Convert 255 RGB to normalized units
for i in col_list:
    for j, k in enumerate(col_dict[i]):
        col_dict[i][j] = round((k/255)*2 - 1, 2)


# %% RANDOMIZATION HAPPENS HERE

excel_sheets = {'blocks': 'blocks', 'self_report': 'self_report'}

xlsx_dic = {}
for n, name in enumerate(excel_sheets):
    xls_file = pd.ExcelFile(excel_sheets[name] + '.xlsx')
    xlsx_dic["{0}".format(name)] = xls_file.parse()

rando_idx = [0]*len(xlsx_dic['blocks'])
for i in range(len(xlsx_dic['blocks'])-1):  # Not including last (self report)
    if not xlsx_dic['blocks'].training[i]:
        rando_idx[i] = 1

start_idx = rando_idx.index(1)
n_rnd_trials = sum(rando_idx)
end_idx = start_idx+n_rnd_trials

rando_idx = list(range(len(rando_idx)))
rando_idx[start_idx:end_idx] = np.random.choice(
    range(start_idx, end_idx), n_rnd_trials, replace=False)

# Will be used to check escape key


def check_quit():
    quitKeys = event.getKeys(keyList=expInfo['escape key'])
    if len(quitKeys) > 0:
        win.close()
        core.quit()


# %% ELEMENTS RELATED TO THE DRAW ROUTINE

# Prepare brush
brush = visual.Brush(win=win, name='brush',
                     lineWidth=1.5,
                     lineColor=[1, 1, 1],
                     lineColorSpace='rgb',
                     opacity=None,
                     buttonRequired=True)


# Prepare lines
line_list = list([expInfo['easy lines n'], expInfo['diff lines n']])
max_lines = line_list[1]
lines = list()
for i in range(max_lines):
    line = visual.Line(win, start=(0, 0), end=(0, 0),
                       lineColor=[0, 0, 0], lineWidth=6)
    line.status = NOT_STARTED
    lines.append(line)


def prep_lines(n, dif, lines):

    color = col_dict[col_list[dif]]
    # set the number of links based on difficulty
    angle, length, start, end = [0]*n, [0]*n, [[]]*n, [[]]*n
    # make subsequent line segments (as many as needed)
    for i in range(n):
        within, repeatSearch, repsN = 0, False, 0
        while within == 0 or repeatSearch and not repsN > 10:
            angle[i] = np.random.uniform(low=0, high=2*math.pi)
            length[i] = np.random.uniform(
                low=expInfo['line length min'], high=expInfo['line length max'])

            if i == 0:
                # for the first line, pick a point at random 10% away from the edge
                start[i] = [
                    random.randrange(-15, 10)/100, random.randrange(-15, 10)/100]
            else:
                # for all subsequent lines, start point is the end of the last point
                start[i] = [end[i-1][0], end[i-1][1]]

            # find the endpoint in a similar way
            end[i] = [round(start[i][0] + length[i] *
                            math.cos(angle[i]), 2), round(start[i][1] + length[i]*math.sin(angle[i]), 2)]

            # check that the lines stay within the screen
            if abs(end[i][0]) < 0.4 and abs(end[i][1]) < 0.4 and abs(start[i][0]) < 0.4 and abs(start[i][1]) < 0.4:
                within = 1
            repsN += 1

        # redifine the lines
        lines[i].start, lines[i].end = start[i], end[i]
        lines[i].lineColor, lines[i].status = color, NOT_STARTED

    return lines, angle, start, end, length

# Will save the trial data


def draw_save_data(block, nTrials, trialNumberInDraw, trialRepeat, dif, outlier, start, end, x, y, length, dist, brush_draw_dur, brush_start_time, isTraining, trialId, nSelfs):

    thisExp.addData('local_trial_n', trialNumberInDraw)
    thisExp.addData('trial_repaet', trialRepeat)
    thisExp.addData('block_n', block)
    thisExp.addData('difficulty', dif)
    thisExp.addData('line_col', col_list[dif])  # list(lines[1].color)
    thisExp.addData('outlier', outlier)
    thisExp.addData('brush_start_time', brush_start_time)
    thisExp.addData('brush_draw_dur', brush_draw_dur)
    thisExp.addData('training', isTraining)
    thisExp.addData('cond_table_id', trialId)
    if len(dist):
        thisExp.addData('brush_max_dev', np.max(dist))
        thisExp.addData('brush_mean_dev', np.mean(dist))

    if trialNumberInDraw < nTrials-1 or trialRepeat or not nSelfs:
        thisExp.nextEntry()

    with open(dataDir+filename2, 'a') as file_object:
        file_object.write(expInfo['participant'] + ';' + str(trialId) + ';' + str(isTraining) + ';' + str(trialRepeat) + ';' + str(dif) + ';' + str(outlier) + ';' +
                          str(block) + ';' + str(trialNumberInDraw) + ';' + str(start) + ';' + str(end) + ';' + str(x) + ';' + str(y) + ';' + str(length) + '\n')

# Extract trial data for draw routine


def extract_data_for_draw_routine(blockNum):
    nTrials = xlsx_dic['blocks'].nTrial[blockNum]
    dif = xlsx_dic['blocks'].dif[blockNum]
    points = [[]]*nTrials
    outlier = xlsx_dic['blocks'].outlier[blockNum]
    trialId = xlsx_dic['blocks'].id[blockNum]
    return nTrials, dif, points, outlier, trialId

# Initializes some values for lines and the brush in the draw routine


# tThisFlip, frameTolerance
def prepare_elements_for_drawing(elementName, n):
    if n:
        for i in range(n):
            # and tThisFlip >= 0.0-frameTolerance
            if elementName[i].status == NOT_STARTED:
                elementName[i].setAutoDraw(True)
    else:
        if elementName.status == NOT_STARTED:  # and tThisFlip >= 0.0-frameTolerance
            elementName.setAutoDraw(True)

# This monstrum will be used to run the draw routine


def flip_on_screen():
    try:
        win.flip()
    except:
        pass


def draw_routine(blockNum, lines, global_n, isTraining, nSelfs):
    nTrials, dif, points, outlier, trialId = extract_data_for_draw_routine(
        blockNum)
    dist_travelled, block = 0, 0
    # frameTolerance = 0.001  # how close to onset before 'same' frame
    trialNumberInDraw, trialRepeat = 0, False

    txt_dic['def0'].pos = text_pos['distance']
    txt_dic['def1'].pos = text_pos['timer']

    # reset timers
    t, waitClickFor, duration = 0, 5, float('inf')
    trialRepeatCount = 0
    while nTrials:
        timeStamp2BSend, trigger2BSend = True, True
        mouse = event.Mouse(win=win)
        # kui jookseb kokku, siis list([0]) *kuigi selle häda on selles, et siis läheb hiiretrajektoori pikkuse arvutamine sassi
        mouse.x, mouse.y = list([0]), list([0])
        # if it is the end of the routine loop
        if trialNumberInDraw >= nTrials:
            brush.reset()
            brush.status = NOT_STARTED
            flip_on_screen()
            # win.flip()
            break
        # if it is not the end of the routine yet
        elif trialNumberInDraw < nTrials:
            dur, current_dist, wait, frameN = 0, 0, True, -1
            button_pressed = False
            dist = list()
            n = line_list[dif]
            if not trialRepeat:  # prepare lines
                lines, angle, start, end, length = prep_lines(
                    n, dif, lines)
            else:
                for i in range(n):
                    lines[i].setAutoDraw(True)

            brush.reset()
            brush.status = NOT_STARTED

            # get current time
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            drawClock.reset(-_timeToFirstFrame)
            t = drawClock.getTime()

            while t - duration < 0:
                buttons = mouse.getPressed()  # wait for mouse release
                t = drawClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=drawClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)

                # number of completed frames (so 0 is the first frame)
                frameN = frameN + 1
                prepare_elements_for_drawing(
                    lines, frameN, t, tThisFlipGlobal,  n)  # tThisFlip, frameTolerance,

                # *brush* updates
                if brush.status == NOT_STARTED:  # and tThisFlip >= 0.0-frameTolerance:
                    prepare_elements_for_drawing(
                        brush, frameN, t, tThisFlipGlobal,  0)  # tThisFlip, frameTolerance,

                if buttons[0] > 0 or (t > waitClickFor and wait):  # and frameN > 1

                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    if wait:
                        draw_start = drawClock.getTime()
                        wait = False
                        for line in lines:
                            line.setAutoDraw(False)

                    # hide lines
                    if buttons[0] > 0:  # and not hovering(click_next, mouse)
                        if not button_pressed:
                            draw_start2 = drawClock.getTime()
                        button_pressed = True
                        # Cartesian distance from point to line segment
                        if len(mouse.x):
                            j = cd.lineseg_dists(
                                ([[mouse.x[-1], mouse.y[-1]]]), np.asarray(start), np.asarray(end))
                            current_dist = min(j)*100
                            # add the smallest one to the counter
                            dist.append(min(j))

                        if len(mouse.x) > 2:
                            dist_travelled = dist_travelled + np.sqrt(
                                (mouse.x[-2]-mouse.x[-1]) ** 2 + (mouse.y[-2]-mouse.y[-1]) ** 2)
                        else:
                            dist_travelled = 0
                    # and hovering(click_next, mouse):
                else:
                    for line in lines:
                        line.contrast = (waitClickFor-t)/waitClickFor
                if not buttons[0] and button_pressed:  #
                    if len(dist):  # save actual performance
                        points[trialNumberInDraw] = round(np.max(dist), 2)
                    brush.reset()
                    brush.status = NOT_STARTED
                    # win.flip()
                    flip_on_screen()
                    save_timeStamps('brush_offset_')
                    brush_offset_t = drawClock.getTime()
                    # brush_draw_dur = brush_offset_t-draw_start  # or - draw_start2?
                    # brush_start_time = draw_start-line_fliped_on_screen_t
                    brush_draw_dur = brush_offset_t-draw_start2
                    brush_start_time = draw_start2-line_fliped_on_screen_t
                    break

                if not wait:
                    dur = t - draw_start

                txt_dic['def0'].text = 'täpsus: ' + "%.2f" % current_dist
                txt_dic['def1'].text = 'kestus: ' + "%.2f" % dur
                txt_dic['def0'].draw()
                txt_dic['def1'].draw()

                # win.flip()
                flip_on_screen()
                if timeStamp2BSend:
                    save_timeStamps('brush_onset')
                    timeStamp2BSend = False
                    line_fliped_on_screen_t = drawClock.getTime()

                if trialNumberInDraw <= nTrials:  # NB väiksem kui
                    block = global_n-start_idx+1
                    if block < 0:
                        block = 0  # training blocks

                if trigger2BSend and block > 0:
                    event_name = '1'+'0' + str(dif) + outlier_str[outlier]
                    sound_trigger(event_name)
                    thisExp.addData('brush_start_trig', 't-'+event_name)
                    trigger2BSend = False

                check_quit()

        line_len_tol = 1-float(expInfo['length tolerance percent'])/100
        if (np.max(dist)*100 > float(expInfo['error tolerance']) or dist_travelled < sum(length)*line_len_tol or dur > 8) and trialRepeatCount < 2:
            brush.reset()
            brush.status = NOT_STARTED
            draw_text('Saad uue katse!',
                      txt_dic['def0'], click_next, isTraining)
            txt_dic['def0'].pos = text_pos['distance']
            trialRepeat = True
            draw_save_data(block, nTrials, trialNumberInDraw, trialRepeat,
                           dif, outlier, start, end, mouse.x, mouse.y, length, dist, brush_draw_dur, brush_start_time, isTraining, trialId, nSelfs)
            trialRepeatCount += 1
        else:
            if trialNumberInDraw < nTrials:
                trialRepeat, trialRepeatCount = False, 0
                draw_save_data(block, nTrials, trialNumberInDraw, trialRepeat,
                               dif, outlier, start, end, mouse.x, mouse.y, length, dist, brush_draw_dur, brush_start_time, isTraining, trialId, nSelfs)
            trialNumberInDraw += 1

    y_circles = find_points(dif, outlier)
    if nTrials:
        points = np.sort(points)
        for yi in range(len(points)):
            if expInfo['fb mode'] == 'type A':
                xys_circles[yi][1] = y_circles[yi]
            else:
                # actual feedback
                xys_circles[yi][1] = round(-7*(points[yi]-0.035), 2)
    return xys_circles, y_circles, block

# %% FEEDBACK RELATED ELEMENTS

# Will be used to calculate random points from a uniform distribution


def find_points(dif, outlier):
    y_circles = [0]*4

    unc = expInfo['point uncertinty']
    outlier_dist = expInfo['outlier distance']
    b1_1 = expInfo['dif baseline min']
    b1_2 = expInfo['dif baseline min'] + unc

    b2_1 = expInfo['easy baseline min']
    b2_2 = expInfo['easy baseline min'] + unc

    b1_2_out_low = b1_1 - outlier_dist  # difficult low max
    b1_1_out_low = b1_2_out_low - unc  # difficult low min

    b2_2_out_low = b2_1 - outlier_dist  # easy low max
    b2_1_out_low = b2_2_out_low - unc  # easy low min

    b1_1_out_high = b1_2 + outlier_dist  # difficult high min
    b1_2_out_high = b1_1_out_high + unc  # difficult high max

    b2_1_out_high = b2_2 + outlier_dist  # difficult high min
    b2_2_out_high = b2_1_out_high + unc  # difficult high max

    if dif:  # if difficult
        y_circles[0:4] = np.random.uniform(
            low=b1_1, high=b1_2, size=4)
        if outlier == 1:  # outlier between b1_1_out_high to b1_2_out_high which is outlier_dist points higher than max in baseline
            y_circles[3] = float(np.random.uniform(
                low=b1_1_out_high, high=b1_2_out_high, size=1))
        elif outlier == -1:  # outlier between b1_1_out_high to b1_2_out_high which is outlier_dist points lower than min in baseline
            y_circles[3] = float(np.random.uniform(
                low=b1_1_out_low, high=b1_2_out_low, size=1))
        # force mean to be -outlier_dist which will have minimal effect in the baseline condition (outlier == 0) and
        # will rise or lower all the points proportionally to the size of the deviating point in outlier == -1 and
        # outlier == 1 condition respectively.
        y_circles = (y_circles[0:4]-np.mean(y_circles)) + (b1_1+b1_2)/2
    else:
        y_circles[0:4] = np.random.uniform(low=b2_1, high=b2_2, size=4)
        if outlier == 1:
            y_circles[3] = float(np.random.uniform(
                low=b2_1_out_high, high=b2_2_out_high, size=1))
        elif outlier == -1:
            y_circles[3] = float(np.random.uniform(
                low=b2_1_out_low, high=b2_2_out_low, size=1))
        y_circles = (y_circles[0:4]-np.mean(y_circles)) + (b2_1+b2_2)/2
    # round and sort for plotting
    y_circles = [round(i, 2) for i in y_circles]
    y_circles = np.flip(np.sort(y_circles))
    return y_circles


# Prepare "next" button
click_next = visual.ShapeStim(
    win=win, name='next',
    size=(0.12, 0.12), vertices='triangle',
    ori=90, pos=(0.7, -0.35),
    lineWidth=0,     colorSpace='rgb',  lineColor=[1, 1, 1], fillColor=[1, 1, 1],
    opacity=1, depth=-2.0, interpolate=True)

# This will be used to check if mouse is on "click_next" object


def hovering(obj, mouse):
    if obj.contains(mouse):
        gotValidClick = True
        return gotValidClick


# The background horizontal lines in fb routine
pic_dir = _thisDir + '\\images'  # folder with the images
gauss = visual.ImageStim(win=win, image=pic_dir + '\\' +
                         'gauss7.png', units='height', size=(1.1, 0.77), name='gauss', contrast=0.2)  # , contrast=0.75 size 1, 0.67


# Positions
gauss.pos, n_bars, ecc, ys = (-0.01, 0), 4, [0.15, 0.45], [0]*4  # -0.1
ys[0:3] = np.random.uniform(low=0, high=0.25, size=3)
ys[3] = float(np.random.uniform(low=-0.25, high=0, size=1))
ys = [round(i, 2) for i in ys]
random.shuffle(ys)
field_pos = (0, 0)

if n_bars == 4:
    # List of box positions
    xys_circles = [[ecc[1]*-1, ys[0]], [ecc[0]*-1, ys[1]],
                   [ecc[0], ys[2]], [ecc[1], ys[3]]]
    xys_rects = [(ecc[1]*-1, 0), (ecc[0]*-1, 0), (ecc[0], 0), (ecc[1], 0)]

elif n_bars == 1:
    xys_circles = [[0, ys[0]], [0, ys[1]], [0, ys[2]], [0, ys[3]]]
    xys_rects = (0, 0)

# Array of circles
circles = visual.ElementArrayStim(win, name='rects', fieldPos=field_pos, fieldSize=(1, 1),
                                  fieldShape='square', nElements=4, sizes=(0.1*aspect, 0.03), xys=xys_circles,
                                  colors=([1.0, 1.0, 1.0]), colorSpace='rgb', opacities=1, oris=0,
                                  sfs=0, contrs=[1, 1, 1, 1], phases=0, elementTex='sin',
                                  elementMask='gauss', texRes=48, interpolate=True,
                                  autoLog=None, maskParams=None)

# White vertical lines
rects = visual.ElementArrayStim(win, name='rects', fieldPos=(0, -0.35), fieldSize=(1, 1),  # field_pos
                                # (0.06, 0.6)
                                # (0.02, 0.6)
                                fieldShape='square', nElements=n_bars, sizes=(0.01, 0.02), xys=xys_rects,
                                colors=([1.0, 1.0, 1.0]), colorSpace='rgb', opacities=1, oris=0,
                                sfs=0, contrs=1, phases=0, elementTex='sqr',
                                elementMask='none', texRes=48, interpolate=True,
                                autoLog=None, maskParams=None)

# Arrows shown in the training fb
arrow1 = visual.ImageStim(win=win, image=pic_dir + '\\' +
                          'arrow1.png', units='height', size=(0.358, 0.15), pos=(-0.28, 0.4), name='arrow1', contrast=0.75)

arrow2 = visual.ImageStim(win=win, image=pic_dir + '\\' +
                          'arrow2.png', units='height', size=(0.392, 0.165), pos=(0.28, -0.425), name='arrow2', contrast=0.75)

# Extract trial data for fb


def extract_data_for_fb(blockNum):
    nTrials = xlsx_dic['blocks'].nTrial[blockNum]
    fb = xlsx_dic['blocks'].fb[blockNum]
    dif = xlsx_dic['blocks'].dif[blockNum]
    out = xlsx_dic['blocks'].outlier[blockNum]
    txt = xlsx_dic['blocks'].intro_text_content[blockNum]
    nSelfs = xlsx_dic['blocks'].nSelf[blockNum]
    return dif, out, nTrials, nSelfs, txt, fb

# Prepares opacities, texts, positions for points and texts for fb


def prepare_aesthetics_for_fb(dif, out, xys_points, txt):
    circles.colors = col_dict[col_list[dif]]
    if 'Pärast tagasiside nägemist küsitakse' in txt:
        circles.opacities, rects.contrs = [1, 0, 0, 0], [0.5, 0.2, 0.2, 0.2]
    else:
        circles.opacities, rects.contrs = 1, 0.5
    # Change the positions
    txt_dic['def0'].pos, txt_dic['def1'].pos, txt_dic['def2'].pos = text_pos['bar_high'], text_pos['bar_mid'], text_pos['bar_low']
    if expInfo['disp cond']:
        txt_dic['def3'].pos = text_pos['middle_high']
    # Text values and other cosmetics
    txt_dic['def0'].text, txt_dic['def1'].text, txt_dic['def2'].text = '100%', '50%', '0%'
    txt_dic['def0'].opacity, txt_dic['def1'].opacity, txt_dic['def2'].opacity = 0.75, 0.75, 0.75
    txt_dic['def3'].text = 'diff: ' + str(dif) + ' out: ' + str(out)
    circles.xys = xys_points


# Will be used to present the fb


def feedback(xys_points, y_circles,  blockNum, block_n, isTraining):
    timeStamp2BSend, trigger2BSend = True, True
    dif, out, nTrials, nSelfs, txt, fb = extract_data_for_fb(blockNum)
    prepare_aesthetics_for_fb(dif, out, xys_points, txt)
    brush.reset()
    brush.status = NOT_STARTED

    mouse = event.Mouse(win=win)
    framesCount, t, fb_satrt = 0, 0, 0
    while nSelfs * fb > 0:  # * nTrials
        brush.reset()
        brush.status = NOT_STARTED
        theseKeys = event.getKeys('space')
        # space_lisada isTraining
        if isTraining and len(theseKeys):
            save_timeStamps('fb_offset_')
            thisExp.addData('fb_RT', t-fb_satrt)
            thisExp.addData('points', y_circles)
            break
        buttons = mouse.getPressed()
        if 'harjutuspl' in txt and framesCount > frameRate:
            arrow1.draw()
            arrow2.draw()
        if not sum(buttons) or framesCount < frameRate*3:
            gauss.draw()
            txt_dic['def0'].draw()
            txt_dic['def1'].draw()
            txt_dic['def2'].draw()
            if expInfo['disp cond']:
                txt_dic['def3'].draw()
            rects.draw()
            if framesCount > frameRate/3:
                circles.draw()
            # win.flip()
            flip_on_screen()
            t = drawClock.getTime()
            if timeStamp2BSend:
                save_timeStamps('fb_onset_')
                fb_satrt = drawClock.getTime()
                timeStamp2BSend = False
            if trigger2BSend and block_n > 0:
                event_name = '1'+'1' + str(dif) + outlier_str[out]
                sound_trigger(event_name)
                trigger2BSend = False
                thisExp.addData('fb_start_trig', 't-'+event_name)
            if framesCount > frameRate*3 and not isTraining:
                click_next.draw()
            check_quit()
            framesCount += 1
        elif not isTraining and sum(buttons) and hovering(click_next, mouse) and framesCount > frameRate*3:
            save_timeStamps('fb_offset_')
            thisExp.addData('fb_RT', t-fb_satrt)
            thisExp.addData('points', y_circles)
            if block_n > 0:
                event_name = '0'+'1' + str(dif) + outlier_str[out]
                sound_trigger(event_name)
                thisExp.addData('fb_end_trig', 't-'+event_name)
            break

# %% ELEMENTS DIRECTLY RELATED TO THE MAIN LOOP


def extract_data_for_main(trialNumber):
    isTraining = xlsx_dic['blocks'].training[rando_idx[trialNumber]]
    nSelfs = xlsx_dic['blocks'].nSelf[rando_idx[trialNumber]]
    intro_text = xlsx_dic['blocks'].intro_text_content[rando_idx[trialNumber]]
    if 'Kognitiivse efektiivsuse mõõtmise plokk:' in intro_text:
        intro_text = intro_text + ' ' + \
            str(trialNumber-start_idx+1) + reminder_text
    return isTraining, nSelfs, intro_text


def self_report_wrapper(nSelfs, trialNumber):
    if nSelfs:
        whichSelfs = xlsx_dic['blocks'].whichSelf[rando_idx[trialNumber]]
        starti, endi = int(whichSelfs[0]), int(whichSelfs[2])
        for n, txt in enumerate(xlsx_dic['self_report'].item[starti:endi]):
            low = xlsx_dic['self_report'].label_high[starti+n]
            high = xlsx_dic['self_report'].label_low[starti+n]
            vas.present(win, thisExp, expInfo['escape key'], clock, visual, event,
                        core, text_pos, txt, high, low)
            construct = xlsx_dic['self_report'].construct[starti+n]
            thisExp.addData('construct', construct)
            thisExp.nextEntry()


# Prepare text box
box_text = visual.TextBox2(
    win, text='Sisesta tekst siia...', font='Open Sans',
    pos=(0, 0),     letterHeight=0.05, size=(None, None), borderWidth=2.0,
    color='white', colorSpace='rgb', opacity=None, bold=False, italic=False,
    lineSpacing=1.0, padding=0.0, anchor='center', fillColor=None, borderColor=None,
    flipHoriz=False, flipVert=False, editable=True, name='text2', autoLog=False,
)


def insert_text(txt):
    txt_dic['def0'].pos = text_pos['slf_txt']
    txt_dic['def0'].text = txt
    box_text.text = 'Sisesta tekst siia...'
    buttons = mouse.getPressed()
    while not buttons[2]:
        brush.reset()
        brush.status = NOT_STARTED
        buttons = mouse.getPressed()
        txt_dic['def0'].draw()
        box_text.draw()
        # win.flip()
        flip_on_screen()
    thisExp.addData('odd', box_text.text)


# THIS IS WHERE THE EXPERIMENT STARTS
# Set win to fullscreen
win.fullscr = True

# Inisialize some variables
trialNumber = 0  # will keep track on how many blocks
nTrials = len(xlsx_dic['blocks'])
theseKeys = event.getKeys(keyList=expInfo['escape key'])

runExperiment = True
while runExperiment and (len(theseKeys) < 1):
    mouse = event.Mouse(win=win)
    buttons = mouse.getPressed()

    # Experiment over?
    if trialNumber == nTrials:
        # Close and quit
        insert_text(odd_text)  # present text box
        txt_dic['def0'].text = end_text  # goodbye
        txt_dic['def0'].draw()
        # win.flip()
        flip_on_screen()
        core.wait(2)
        runExperiment = False  # Yep, over!
    # Not the end of the experiment yet
    elif trialNumber < nTrials:
        isTraining, nSelfs, intro_text = extract_data_for_main(trialNumber)

        # Filip before next trial
        # win.flip()
        flip_on_screen()
        draw_text(intro_text, txt_dic['def0'],
                  click_next, isTraining)
        # Run draw routine
        xys_points, y_circles, block_n = draw_routine(
            rando_idx[trialNumber], lines, trialNumber, isTraining, nSelfs)
        # Give feedback
        feedback(xys_points, y_circles,
                 rando_idx[trialNumber], block_n, isTraining)
        brush.reset()
        brush.status = NOT_STARTED
        # Run assessment routine
        self_report_wrapper(nSelfs, trialNumber)

    trialNumber += 1
    theseKeys = event.getKeys(keyList=expInfo['escape key'])

# Save eyetracking data
save_eyeData()
# Close window and quit
win.close(), core.quit()
