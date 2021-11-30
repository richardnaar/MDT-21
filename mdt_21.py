# andmetabel
# outlier
# silmaliigutused

from __future__ import absolute_import, division
import math
import vas
# from typing import Dict
# from numpy.lib.function_base import angle

import pandas as pd
import random
# from psychopy.hardware import keyboard
# import sys  # to get file system encoding
import os  # handy system and path functions
import numpy as np  # whole numpy lib is available, prepend 'np.'
from psychopy.constants import (NOT_STARTED)
# STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER
from psychopy import gui, visual, core, data, event, clock  # , logging, sound, colors
import psychopy
import cart_dist as cd
psychopy.useVersion('latest')


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)  # set as a current dir

psychopyVersion = '2021.2.3'
expName = os.path.basename(__file__)
expInfo = {'participant': '', 'error tolerance': 0.06,
           'fb mode': ['type A', 'type B'], 'escape key': 'q'}

dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion


filename = _thisDir + os.sep + \
    u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=__file__,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
aspect = win.size[0]/win.size[1]


expInfo['date'] = data.getDateStr()  # add a simple timestamp

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess


# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# make a color list
col_list = [[230, 25, 75],  # red
            [0, 120, 200]]  # blue

random.shuffle(col_list)
# normalize
for i, k in enumerate(col_list):
    for j, l in enumerate(k):
        col_list[i][j] = (l/255)*2 - 1

default_text0 = visual.TextStim(win=win, name='text0',
                                text='juku', font='Arial', pos=(0, 0),
                                height=0.04, wrapWidth=1.25, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR', depth=-1.0)

default_text1 = visual.TextStim(win=win, name='text1',
                                text='juku', font='Arial', pos=(0, 0),
                                height=0.04, wrapWidth=1.25, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR', depth=-1.0)

txt_dic = {'def0': default_text0, 'def1': default_text1}

# 'bar_high': (0, 0.43), 'bar_low': (0, -0.43)
text_pos = {'intro': (0.7, -0.35), 'distance': (-0.4, 0.4), 'timer': (-0.2, 0.4),
            'middle': (0, 0), 'bar': (0.06, 0.6), 'bar_high': (-0.40, 0.3), 'bar_low': (-0.40, -0.3),
            'slf_txt': (0, 0.2), 'slf_low': (-0.45, -0.25), 'slf_high': (0.45, -0.25)}

brush = visual.Brush(win=win, name='brush',
                     lineWidth=1.5,
                     lineColor=[1, 1, 1],
                     lineColorSpace='rgb',
                     opacity=None,
                     buttonRequired=True)

click_next = visual.ShapeStim(
    win=win, name='next',
    size=(0.12, 0.12), vertices='triangle',
    ori=90, pos=(0.7, -0.35),
    lineWidth=0,     colorSpace='rgb',  lineColor=[1, 1, 1], fillColor=[1, 1, 1],
    opacity=1, depth=-2.0, interpolate=True)


pic_dir = _thisDir + '\\images'  # folder with the experimental pictures
gauss = visual.ImageStim(win=win, image=pic_dir + '\\' +
                         'gauss5.png', units='height', size=(1.1, 0.67), name='gauss', contrast=0.75)  # , contrast=0.75

gauss.pos, n_bars, ecc, ys = (-0.1, 0), 4, [0.1, 0.3], [0]*4
ys[0:3] = np.random.uniform(low=0, high=0.25, size=3)
ys[3] = float(np.random.uniform(low=-0.25, high=0, size=1))
random.shuffle(ys)

if n_bars == 4:
    # List of box positions
    xys_circles = [[ecc[1]*-1, ys[0]], [ecc[0]*-1, ys[1]],
                   [ecc[0], ys[2]], [ecc[1], ys[3]]]
    xys_rects = [(ecc[1]*-1, 0), (ecc[0]*-1, 0), (ecc[0], 0), (ecc[1], 0)]
    field_pos = (0.1, 0)
elif n_bars == 1:
    xys_circles = [[0, ys[0]], [0, ys[1]], [0, ys[2]], [0, ys[3]]]
    xys_rects, field_pos = (0, 0), (0, 0)

# Array of circles
circles = visual.ElementArrayStim(win, name='rects', fieldPos=field_pos, fieldSize=(1, 1),
                                  fieldShape='square', nElements=4, sizes=(0.1*aspect, 0.03), xys=xys_circles,
                                  colors=([1.0, 1.0, 1.0]), colorSpace='rgb', opacities=1, oris=0,
                                  sfs=0, contrs=[1, 1, 1, 1], phases=0, elementTex='sin',
                                  elementMask='gauss', texRes=48, interpolate=True,
                                  autoLog=None, maskParams=None)

rects = visual.ElementArrayStim(win, name='rects', fieldPos=field_pos, fieldSize=(1, 1),
                                fieldShape='square', nElements=n_bars, sizes=text_pos['bar'], xys=xys_rects,
                                colors=([1.0, 1.0, 1.0]), colorSpace='rgb', opacities=1, oris=0,
                                sfs=0, contrs=1, phases=0, elementTex='sqr',
                                elementMask='gauss', texRes=48, interpolate=True,
                                autoLog=None, maskParams=None)
max_lines = 6
lines = list()
for i in range(max_lines):
    line = visual.Line(win, start=(0, 0), end=(0, 0),
                       lineColor=[0, 0, 0], lineWidth=6)
    line.status = NOT_STARTED
    lines.append(line)


def find_points(dif, outlier):
    y_circles = [0]*4
    # outlier = 1
    # while np.std(y_circles) < 0.025:
    if dif:  # low=-0.15, high=-0.05, size=4
        y_circles[0:4] = np.random.uniform(low=-0.1, high=0, size=4)
        if outlier:
            y_circles[3] = float(np.random.uniform(
                low=0, high=0.1, size=1))
        y_circles = (y_circles[0:4]-np.mean(y_circles))-0.05
    else:
        y_circles[0:4] = np.random.uniform(low=0, high=0.1, size=4)
        if outlier:
            y_circles[3] = float(np.random.uniform(
                low=-0.1, high=0, size=1))
        y_circles = (y_circles[0:4]-np.mean(y_circles))+0.05
    # y_circles = [-0.05]*4
    y_circles = np.flip(np.sort(y_circles))
    return y_circles


def hovering(obj, mouse):
    if obj.contains(mouse):
        gotValidClick = True
        return gotValidClick


def draw_text(text2draw, textElement, click_next):
    mouse = event.Mouse(win=win)
    buttons = [0, 0, 0]
#    textCopy = textElement
    textElement.text = text2draw
    textElement.pos = (0, 0)
    frameCount = 0
    win.flip()
    brush.reset()
    # not buttons or
    while not hovering(click_next, mouse) or not sum(buttons):
        mouse = event.Mouse(win=win)
        if frameCount > 3:
            click_next.draw()
            textElement.draw()
            win.flip()
        buttons = mouse.getPressed()
        theseKeys = event.getKeys(keyList=expInfo['escape key'])
        frameCount += 1
        if len(theseKeys):
            core.quit()


excel_sheets = {'blocks': 'blocks1', 'self_report': 'self_report'}

xlsx_dic = {}
for n, name in enumerate(excel_sheets):
    xls_file = pd.ExcelFile(excel_sheets[name] + '.xlsx')
    xlsx_dic["{0}".format(name)] = xls_file.parse()


# define clock
drawClock = core.Clock()


def check_quit():
    quitKeys = event.getKeys(keyList=expInfo['escape key'])
    if len(quitKeys) > 0:
        win.close()
        core.quit()


def prep_lines(n, col_list, dif, lines):
    # lines = []
    color = col_list[dif]
    # set the number of links based on difficulty
    angle, length, start, end = [0]*n, [0]*n, [[]]*n, [[]]*n
    # make subsequent line segments (as many as needed)
    for i in range(n):
        within, repeatSearch, repsN = 0, False, 0
        while within == 0 or repeatSearch or repsN > 10:
            deg10 = math.pi/180*0  # deg = rad/pi * 180
            angle[i] = np.random.uniform(low=deg10, high=2*math.pi-deg10)
            length[i] = np.random.uniform(low=0.05, high=0.2)

            if i == 0:
                # for the first line, pick a point at random 10% away from the edge
                start[i] = [
                    random.randrange(-15, 10)/100, random.randrange(-15, 10)/100]
            else:
                # for all subsequent lines, start point is the end of the last point
                start[i] = [end[i-1][0], end[i-1][1]]

            # find the endpoint in a similar way
            end[i] = [start[i][0] + length[i] *
                      math.cos(angle[i]), start[i][1] + length[i]*math.sin(angle[i])]

            # check that the lines stay within the screen
            if abs(end[i][0]) < 0.4 and abs(end[i][1]) < 0.4 and abs(start[i][0]) < 0.4 and abs(start[i][1]) < 0.4:
                within = 1

            if i > 1 and cd.doIntersect(cd.Point(start[i][0], start[i][1]), cd.Point(end[i][0], end[i][1]), cd.Point(start[i-2][0], start[i-2][1]), cd.Point(end[i-2][0], end[i-2][1])):
                repeatSearch = True
                repsN += 1
            else:
                repeatSearch = False
                repsN = 0
        # redifine the lines
        lines[i].start, lines[i].end = start[i], end[i]
        lines[i].lineColor, lines[i].status = color, NOT_STARTED
    return lines, angle, start, end


def draw_routine(blockNum, lines):
    frameTolerance = 0.001  # how close to onset before 'same' frame
    trialNumber, trialRepeat = 0, False
    nTrials = xlsx_dic['blocks'].nTrial[blockNum]
    dif = xlsx_dic['blocks'].dif[blockNum]
    points = [[]]*nTrials
    txt_dic['def0'].pos = text_pos['distance']
    txt_dic['def1'].pos = text_pos['timer']
    outlier = xlsx_dic['blocks'].outlier[blockNum]

    # reset timers
    t, waitClickFor, duration = 0, 5, float('inf')

    trialRepeatCount = 0
    while nTrials:
        mouse = event.Mouse(win=win)
        mouse.x, mouse.y = [], []
        # if it is the end of the routine loop
        if trialNumber > nTrials:
            brush.reset()
            brush.status = NOT_STARTED
            break
        # if it is not the end of the routine yet
        elif trialNumber < nTrials:

            dur, current_dist, wait, frameN = 0, 0, True, -1
            dist = list()
            n = [3, 6][dif]
            if not trialRepeat:  # prepare lines
                lines, angle, start, end = prep_lines(n, col_list, dif, lines)
            else:
                for i in range(n):
                    lines[i].setAutoDraw(True)

            brush.status = NOT_STARTED
            brush.reset()

            # get current time
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            drawClock.reset(-_timeToFirstFrame)
            t = drawClock.getTime()
            while t - duration < 0:
                # wait for mouse release
                buttons = mouse.getPressed()
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)

                t = drawClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=drawClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)

                # number of completed frames (so 0 is the first frame)
                frameN = frameN + 1
                # display lines
                for i in range(n):
                    if lines[i].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # # keep track of start time/frame for later
                        lines[i].frameNStart = frameN  # exact frame index
                        # local t and not account for scr refresh
                        lines[i].tStart = t
                        # on global time
                        lines[i].tStartRefresh = tThisFlipGlobal
                        # time at next scr refresh
                        win.timeOnFlip(lines[i], 'tStartRefresh')
                        lines[i].setAutoDraw(True)

                # *brush* updates
                if brush.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    brush.frameNStart = frameN  # exact frame index
                    brush.tStart = t  # local t and not account for scr refresh
                    brush.tStartRefresh = tThisFlipGlobal  # on global time
                    # time at next scr refresh
                    win.timeOnFlip(brush, 'tStartRefresh')
                    brush.setAutoDraw(True)

                if sum(buttons) > 0 or (t > waitClickFor and wait) and frameN > 1:

                    if wait:
                        draw_start = t
                        wait = False
#                        mouse.x, mouse.y = [start[0][0]], [start[0][1]]
                    for line in lines:
                        line.setAutoDraw(False)
                    # hide lines
                    if sum(buttons) > 0 and not hovering(click_next, mouse):

                        # Cartesian distance from point to line segment
                        j = cd.lineseg_dists(
                            ([[mouse.x[-1], mouse.y[-1]]]), np.asarray(start), np.asarray(end))

                        current_dist = round(min(j), 2)
                        # add the smallest one to the counter
                        dist.append(min(j))
                    elif sum(buttons) > 0 and hovering(click_next, mouse):
                        if len(dist):  # save actual performance
                            points[trialNumber] = round(np.max(dist), 2)
                        break

                if not wait:
                    dur = round(t - draw_start, 1)

                # draw things hereq
                txt_dic['def0'].text,  txt_dic['def1'].text = current_dist, dur
                txt_dic['def0'].draw()
                txt_dic['def1'].draw()

                if frameN > 2:
                    click_next.draw()
                win.flip()
                check_quit()

        # expInfo['error tolerance']
        if not len(dist) or np.max(dist) > float(expInfo['error tolerance']) and trialRepeatCount < 2:
            brush.reset()
            trialNumber = trialNumber
            draw_text('Oops!', default_text0, click_next)
            txt_dic['def0'].pos = text_pos['distance']
            trialRepeat = True
            trialRepeatCount += 1
        else:
            trialNumber += 1
            trialRepeat, trialRepeatCount = False, 0
    y_circles = find_points(dif, outlier)
    if nTrials:
        for yi in range(len(points)):
            if expInfo['fb mode'] == 'type A':
                xys_circles[yi][1] = y_circles[yi]
            else:
                xys_circles[yi][1] = -7*(points[yi]-0.025)  # actual feedback
    return xys_circles


def feedback(xys_points, blockNum):
    dif = xlsx_dic['blocks'].dif[blockNum]
    circles.colors = col_list[dif]
    if blockNum == 3:
        circles.opacities, rects.contrs = [1, 0, 0, 0], [1, 0.2, 0.2, 0.2]
    elif blockNum == 4:
        circles.opacities, rects.contrs = 1, 1
    nTrials = xlsx_dic['blocks'].nTrial[blockNum]
    nSelfs = xlsx_dic['blocks'].nSelf[blockNum]
#
    # construct, item, label_low, label_high
    default_text0.pos, default_text1.pos = text_pos['bar_high'], text_pos['bar_low']
    default_text0.text, default_text1.text = '100%', '0%'
    default_text0.contrast, default_text1.contrast = 0.75, 0.75
    circles.xys = xys_points
    mouse = event.Mouse(win=win)
    framesCount = 0
    while nSelfs * nTrials > 0:
        buttons = mouse.getPressed()
        if not sum(buttons):
            default_text0.draw()
            default_text1.draw()
            gauss.draw()
            rects.draw()
            circles.draw()
            win.flip()
            if framesCount > 60*3:
                click_next.draw()
            check_quit()
            framesCount += 1
        elif sum(buttons) and hovering(click_next, mouse) and framesCount > 60*3:
            break

    # this is the start of the experiment loop
    trialNumber = 0
    nTrials = len(xlsx_dic['blocks'])
    runExperiment = True
    theseKeys = event.getKeys(keyList=expInfo['escape key'])
    while runExperiment and (len(theseKeys) < 1):
        mouse = event.Mouse(win=win)
        # if it is the end of the experiment loop
        if trialNumber == nTrials:
                # close and quit
            runExperiment = False
    #        win.close(), core.quit()
        # if it is not the end of the experiment yet
        elif trialNumber < nTrials:
            nSelfs = xlsx_dic['blocks'].nSelf[trialNumber]
            intro_text = xlsx_dic['blocks'].intro_text_content[trialNumber]
            draw_text(intro_text, txt_dic['def0'], click_next)
            xys_points = draw_routine(trialNumber, lines)
            feedback(xys_points, trialNumber)
            brush.reset()
            brush.status = NOT_STARTED
            if nSelfs:
                whichSelfs = xlsx_dic['blocks'].whichSelf[trialNumber]
                starti, endi = int(whichSelfs[0]), int(whichSelfs[2])
                for n, txt in enumerate(xlsx_dic['self_report'].item[starti:endi]):
                    low = xlsx_dic['self_report'].label_high[starti+n]
                    high = xlsx_dic['self_report'].label_low[starti+n]
                    vas.present(win, expInfo['escape key'], clock, visual, event,
                                core, text_pos, txt, high, low)

        # draw things here
        win.flip()

        trialNumber += 1
        theseKeys = event.getKeys(keyList=expInfo['escape key'])


win.close(), core.quit()
