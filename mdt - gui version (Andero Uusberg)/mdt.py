#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on December 08, 2021, at 20:22
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'mdt'  # from the Builder filename that created this script
expInfo = {'participant': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Richard Naar\\Documents\\dok\\TARU\\MDT 21\\Andero mdt\\mdt.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
# enter 1 for test monkey
test = 0

import random
import math
aspect = win.size[0]/win.size[1]

# make a color list
col_list = [[230, 25, 75], # red
            [0, 120, 200]] # blue
#            [0, 120, 0]] # green
#            [230, 190, 255], # levander
#            [170, 110, 40], # brown
#            [245, 130, 48]] # orange
# counterbalance color mapping
random.shuffle(col_list)
# normalize
for i,k in enumerate(col_list): 
    for j,l in enumerate(k): 
        col_list[i][j] = (l/255)*2 - 1

# 10% steps would be -0.32 -0.24 -0.16 -0.08  0.00  0.08  0.16  0.24  0.32  0.40
# at 40% and 70%
base_avg_list = [0.16, -0.08]

# the value that is added to generate variabilities
base_var_list = [0.01, 0.06]

# make condition counterbalancer
cond_list = [[0, 0],
             [0, 1],
             [1, 0],
             [1, 1]]
random.shuffle(cond_list)

point_counter = 0
res = "free"
total_err = []
block_err = []
color = [0,0,0]
intro_text = visual.TextStim(win=win, name='intro_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.25, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
intro_next = visual.ShapeStim(
    win=win, name='intro_next',
    size=[1.0, 1.0], vertices='triangle',
    ori=90, pos=(0.7, -0.35),
    lineWidth=0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
intro_mouse = event.Mouse(win=win)
x, y = [None, None]
intro_mouse.mouseClock = core.Clock()

# Initialize components for Routine "draw"
drawClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
brush = visual.Brush(win=win, name='brush',
   lineWidth=1.5,
   lineColor=[1,1,1],
   lineColorSpace='rgb',
   opacity=None,
   buttonRequired=True)
timer = visual.TextStim(win=win, name='timer',
    text='',
    font='Arial',
    pos=(-0.4, 0.4), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
distance = visual.TextStim(win=win, name='distance',
    text='',
    font='Arial',
    pos=(-0.2, 0.4), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
next = visual.ShapeStim(
    win=win, name='next',
    size=[1.0, 1.0], vertices='triangle',
    ori=90, pos=(0.7, -0.35),
    lineWidth=0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "fb"
fbClock = core.Clock()
bar_text = visual.TextStim(win=win, name='bar_text',
    text=None,
    font='Arial',
    pos=(-0.5, 0.25), height=0.04, wrapWidth=0.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
bar_label_high = visual.TextStim(win=win, name='bar_label_high',
    text='kõrge täpsus',
    font='Arial',
    pos=(0, 0.43), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
bar_bar = visual.Rect(
    win=win, name='bar_bar',
    width=(0.05, 0.8)[0], height=(0.05, 0.8)[1],
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
bar_label_low = visual.TextStim(win=win, name='bar_label_low',
    text='madal täpsus',
    font='Arial',
    pos=(0, -0.43), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
bar_next = visual.ShapeStim(
    win=win, name='bar_next',
    size=[1.0, 1.0], vertices='triangle',
    ori=90, pos=(0.7, -0.35),
    lineWidth=0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-5.0, interpolate=True)
bar_mouse = event.Mouse(win=win)
x, y = [None, None]
bar_mouse.mouseClock = core.Clock()
bar_p1 = visual.ShapeStim(
    win=win, name='bar_p1',
    size=[0.01,0.01], vertices='circle',
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor=[1, 1, 1],
    opacity=0.5, depth=-7.0, interpolate=True)
bar_p2 = visual.ShapeStim(
    win=win, name='bar_p2',
    size=[0.01,0.01], vertices='circle',
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor=[1, 1, 1],
    opacity=0.5, depth=-8.0, interpolate=True)
bar_p3 = visual.ShapeStim(
    win=win, name='bar_p3',
    size=[0.01,0.01], vertices='circle',
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.5, depth=-9.0, interpolate=True)

# Initialize components for Routine "assess"
assessClock = core.Clock()
slf_text = visual.TextStim(win=win, name='slf_text',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
scale_low = visual.TextStim(win=win, name='scale_low',
    text='',
    font='Arial',
    pos=(-0.65, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
scale_high = visual.TextStim(win=win, name='scale_high',
    text='',
    font='Arial',
    pos=(0.65, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
slf_scale = visual.Rect(
    win=win, name='slf_scale',
    width=(1, 0.05)[0], height=(1, 0.05)[1],
    ori=0, pos=(0, -0.1),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)
slf_set = visual.Rect(
    win=win, name='slf_set',
    width=(0.01, 0.05)[0], height=(0.01, 0.05)[1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=1, depth=-5.0, interpolate=True)
slf_mouse = event.Mouse(win=win)
x, y = [None, None]
slf_mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
block_loop = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks.xlsx'),
    seed=None, name='block_loop')
thisExp.addLoop(block_loop)  # add the loop to the experiment
thisBlock_loop = block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
if thisBlock_loop != None:
    for paramName in thisBlock_loop:
        exec('{} = thisBlock_loop[paramName]'.format(paramName))

for thisBlock_loop in block_loop:
    currentLoop = block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
    if thisBlock_loop != None:
        for paramName in thisBlock_loop:
            exec('{} = thisBlock_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intro"-------
    continueRoutine = True
    # update component parameters for each repeat
    if nTrial > 0:
        # set the counterbalanced color based on difficulty
        color = col_list[dif]   
    
    # FEEDBACK BAR
    
    # get a fixed base result value and add a jitter
    avg = base_avg_list[dif] + randint(0,5)/100
    # generate result values that would be at 10% to 15% distance from the goal.
    perf_pos = [
    (0, (avg - 2*base_var_list[var] + randint(0,5)/100)),
    (0, (avg - base_var_list[var] + randint(0,5)/100)),
    (0, (avg + base_var_list[var] + randint(0,5)/100)),
    (0, (avg + 2*base_var_list[var] + randint(0,5)/100)),
    ]
    
    # show feedback
    if id == 35:
        intro_text_content += "\n\nSu skooriks kujunes " + str(round(point_counter)) + " punkti!" 
        if point_counter > 20:
            intro_text_content += "\n\nPalju õnne, sellega oled võitnud tahvli šokolaadi!"
        else: 
            intro_text_content += "\n\nSellega oled tahvli šokolaadi siiski auga välja teeninud!"
    
    elif id == 36:
        intro_text_content += " " + str(100 - round(100*(sum(total_err)/len(total_err)))) + " protsenti."
        #  {:.0f} protsenti".format(err) 
        
    point_counter += (avg * 200) + 2
    bar_instruction = "\n\nSul on nüüd " + str(round(point_counter)) + " punkti."
    intro_text.setText(intro_text_content)
    intro_next.setSize((0.12, 0.12))
    # setup some python lists for storing info about the intro_mouse
    intro_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    introComponents = [intro_text, intro_next, intro_mouse]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "intro"-------
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro_text* updates
        if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_text.frameNStart = frameN  # exact frame index
            intro_text.tStart = t  # local t and not account for scr refresh
            intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
            intro_text.setAutoDraw(True)
        
        # *intro_next* updates
        if intro_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_next.frameNStart = frameN  # exact frame index
            intro_next.tStart = t  # local t and not account for scr refresh
            intro_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_next, 'tStartRefresh')  # time at next scr refresh
            intro_next.setAutoDraw(True)
        # *intro_mouse* updates
        if intro_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_mouse.frameNStart = frameN  # exact frame index
            intro_mouse.tStart = t  # local t and not account for scr refresh
            intro_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_mouse, 'tStartRefresh')  # time at next scr refresh
            intro_mouse.status = STARTED
            intro_mouse.mouseClock.reset()
            prevButtonState = intro_mouse.getPressed()  # if button is down already this ISN'T a new click
        if intro_mouse.status == STARTED:  # only update if started and not finished!
            buttons = intro_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(intro_next)
                        clickableList = intro_next
                    except:
                        clickableList = [intro_next]
                    for obj in clickableList:
                        if obj.contains(intro_mouse):
                            gotValidClick = True
                            intro_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intro"-------
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    currentLoop.addData('difficulty', dif)
    currentLoop.addData('variance', var)
    currentLoop.addData('point_mean', avg)
    currentLoop.addData('points', perf_pos)
    currentLoop.addData('color', color)
    block_loop.addData('intro_text.started', intro_text.tStartRefresh)
    block_loop.addData('intro_text.stopped', intro_text.tStopRefresh)
    block_loop.addData('intro_next.started', intro_next.tStartRefresh)
    block_loop.addData('intro_next.stopped', intro_next.tStopRefresh)
    # store data for block_loop (TrialHandler)
    block_loop.addData('intro_mouse.started', intro_mouse.tStart)
    block_loop.addData('intro_mouse.stopped', intro_mouse.tStop)
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=nTrial, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "draw"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        brush.setButtonRequired(True)
        brush.reset()
        dur = 0
        wait = 0
        dist = []
        lines = []
        current_dist = 0
        
        # set the number of links based on difficulty
        n = [3,6][dif]
        angle = [0]*n
        length = [0]*n
        start = [[]]*n
        end = [[]]*n
        
        # make subsequent line segments (as many as needed)
        for i in range(n):
            within = 0
            while within == 0:
                angle[i] = random.randrange(360)
                length[i] = random.randrange(20,50)/100
                
                if i == 0:
                    # for the first line, pick a point at random 10% away from the edge
                    start[i] = [random.randrange(-40, 40)/100, random.randrange(-40, 40)/100]
                else:   
                    # for all subsequent lines, start point is the end of the last point
                    start[i] = [end[i-1][0], end[i-1][1]]
                
                # find the endpoint in a similar way
                end[i] = [start[i][0] + length[i]*math.cos(math.radians(angle[i])), start[i][1] + length[i]*math.sin(math.radians(angle[i]))]
                
                # check that the lines stay within the screen
                if abs(end[i][0]) < 0.4 and abs(end[i][1]) < 0.4 and abs(start[i][0]) < 0.4 and abs(start[i][1]) < 0.4:
                    within = 1
        
                # make the line
                line = visual.Line(win, start=(start[i]), end=(end[i]), lineColor=color, lineWidth = 6)
        
                # check that the lines don't cross a previous line?
                #if i > 0:
                #    for prev_line in lines:
                #        if line.overlaps(prev_line):
                #            within = 0
            
            # make the line object
            lines.append(line)
            
        
        next.setSize((0.12, 0.12))
        # keep track of which components have finished
        drawComponents = [mouse, brush, timer, distance, next]
        for thisComponent in drawComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        drawClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "draw"-------
        while continueRoutine:
            # get current time
            t = drawClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=drawClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(next)
                            clickableList = next
                        except:
                            clickableList = [next]
                        for obj in clickableList:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *brush* updates
            if brush.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                brush.frameNStart = frameN  # exact frame index
                brush.tStart = t  # local t and not account for scr refresh
                brush.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(brush, 'tStartRefresh')  # time at next scr refresh
                brush.setAutoDraw(True)
            
            # *timer* updates
            if timer.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                timer.frameNStart = frameN  # exact frame index
                timer.tStart = t  # local t and not account for scr refresh
                timer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer, 'tStartRefresh')  # time at next scr refresh
                timer.setAutoDraw(True)
            if timer.status == STARTED:  # only update if drawing
                timer.setText(dur, log=False)
            
            # *distance* updates
            if distance.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                distance.frameNStart = frameN  # exact frame index
                distance.tStart = t  # local t and not account for scr refresh
                distance.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(distance, 'tStartRefresh')  # time at next scr refresh
                distance.setAutoDraw(True)
            if distance.status == STARTED:  # only update if drawing
                distance.setText(current_dist, log=False)
            # display lines
            for line in lines:
                if line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    line.frameNStart = frameN  # exact frame index
                    line.tStart = t  # local t and not account for scr refresh
                    line.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(line, 'tStartRefresh')  # time at next scr refresh
                    line.setAutoDraw(True)
            
            # wait for mouse release
            if wait == 0 and sum(buttons) == 0:
                wait = 1
                draw_start = t
            
            elif wait > 0 and sum(buttons) > 0:
                wait = 2
                dur = round(t - draw_start,2)
                # hide lines
                for line in lines:
                    line.setAutoDraw(False)
                
                # loop over all line segments
                j = [0 for i in range(n)]
                for i in range(n):
                    j[i] = abs(math.cos(math.radians(angle[i]))*(mouse.x[-1] - start[i][0]) - math.sin(math.radians(angle[i]))*(mouse.y[-1] - start[i][1]))
                
                current_dist = round(min(j),2)
                # add the smallest one to the counter
                dist.append(min(j))
                
            elif wait == 2 and sum(buttons) == 0:
                wait = 3
            
            # *next* updates
            if next.status == NOT_STARTED and wait == 3:
                # keep track of start time/frame for later
                next.frameNStart = frameN  # exact frame index
                next.tStart = t  # local t and not account for scr refresh
                next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
                next.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in drawComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "draw"-------
        for thisComponent in drawComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials (TrialHandler)
        trials.addData('mouse.x', mouse.x)
        trials.addData('mouse.y', mouse.y)
        trials.addData('mouse.leftButton', mouse.leftButton)
        trials.addData('mouse.midButton', mouse.midButton)
        trials.addData('mouse.rightButton', mouse.rightButton)
        trials.addData('mouse.time', mouse.time)
        trials.addData('mouse.clicked_name', mouse.clicked_name)
        trials.addData('mouse.started', mouse.tStart)
        trials.addData('mouse.stopped', mouse.tStop)
        trials.addData('brush.started', brush.tStartRefresh)
        trials.addData('brush.stopped', brush.tStopRefresh)
        trials.addData('timer.started', timer.tStartRefresh)
        trials.addData('timer.stopped', timer.tStopRefresh)
        trials.addData('distance.started', distance.tStartRefresh)
        trials.addData('distance.stopped', distance.tStopRefresh)
        mean_dist = round(sum(dist)/len(dist),2)
        brush.reset()
        trials.addData('next.started', next.tStartRefresh)
        trials.addData('next.stopped', next.tStopRefresh)
        # the Routine "draw" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nTrial repeats of 'trials'
    
    
    # ------Prepare to start Routine "fb"-------
    continueRoutine = True
    # update component parameters for each repeat
    if nSelf == 0 or nTrial == 0:
        continueRoutine = False
    bar_next.setSize((0.12, 0.12))
    # setup some python lists for storing info about the bar_mouse
    bar_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    bar_p1.setLineColor(color)
    bar_p2.setLineColor(color)
    bar_p3.setFillColor([1,1,1])
    bar_p3.setLineColor(color)
    # keep track of which components have finished
    fbComponents = [bar_text, bar_label_high, bar_bar, bar_label_low, bar_next, bar_mouse, bar_p1, bar_p2, bar_p3]
    for thisComponent in fbComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fb"-------
    while continueRoutine:
        # get current time
        t = fbClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fbClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *bar_text* updates
        if bar_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bar_text.frameNStart = frameN  # exact frame index
            bar_text.tStart = t  # local t and not account for scr refresh
            bar_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bar_text, 'tStartRefresh')  # time at next scr refresh
            bar_text.setAutoDraw(True)
        if bar_text.status == STARTED:  # only update if drawing
            bar_text.setText('', log=False)
        
        # *bar_label_high* updates
        if bar_label_high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bar_label_high.frameNStart = frameN  # exact frame index
            bar_label_high.tStart = t  # local t and not account for scr refresh
            bar_label_high.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bar_label_high, 'tStartRefresh')  # time at next scr refresh
            bar_label_high.setAutoDraw(True)
        
        # *bar_bar* updates
        if bar_bar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bar_bar.frameNStart = frameN  # exact frame index
            bar_bar.tStart = t  # local t and not account for scr refresh
            bar_bar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bar_bar, 'tStartRefresh')  # time at next scr refresh
            bar_bar.setAutoDraw(True)
        
        # *bar_label_low* updates
        if bar_label_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bar_label_low.frameNStart = frameN  # exact frame index
            bar_label_low.tStart = t  # local t and not account for scr refresh
            bar_label_low.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bar_label_low, 'tStartRefresh')  # time at next scr refresh
            bar_label_low.setAutoDraw(True)
        
        # *bar_next* updates
        if bar_next.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            bar_next.frameNStart = frameN  # exact frame index
            bar_next.tStart = t  # local t and not account for scr refresh
            bar_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bar_next, 'tStartRefresh')  # time at next scr refresh
            bar_next.setAutoDraw(True)
        # *bar_mouse* updates
        if bar_mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            bar_mouse.frameNStart = frameN  # exact frame index
            bar_mouse.tStart = t  # local t and not account for scr refresh
            bar_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bar_mouse, 'tStartRefresh')  # time at next scr refresh
            bar_mouse.status = STARTED
            bar_mouse.mouseClock.reset()
            prevButtonState = bar_mouse.getPressed()  # if button is down already this ISN'T a new click
        if bar_mouse.status == STARTED:  # only update if started and not finished!
            buttons = bar_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(bar_next)
                        clickableList = bar_next
                    except:
                        clickableList = [bar_next]
                    for obj in clickableList:
                        if obj.contains(bar_mouse):
                            gotValidClick = True
                            bar_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *bar_p1* updates
        if bar_p1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bar_p1.frameNStart = frameN  # exact frame index
            bar_p1.tStart = t  # local t and not account for scr refresh
            bar_p1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bar_p1, 'tStartRefresh')  # time at next scr refresh
            bar_p1.setAutoDraw(True)
        if bar_p1.status == STARTED:  # only update if drawing
            bar_p1.setPos(perf_pos[0], log=False)
        
        # *bar_p2* updates
        if bar_p2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bar_p2.frameNStart = frameN  # exact frame index
            bar_p2.tStart = t  # local t and not account for scr refresh
            bar_p2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bar_p2, 'tStartRefresh')  # time at next scr refresh
            bar_p2.setAutoDraw(True)
        if bar_p2.status == STARTED:  # only update if drawing
            bar_p2.setPos(perf_pos[1], log=False)
        
        # *bar_p3* updates
        if bar_p3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bar_p3.frameNStart = frameN  # exact frame index
            bar_p3.tStart = t  # local t and not account for scr refresh
            bar_p3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bar_p3, 'tStartRefresh')  # time at next scr refresh
            bar_p3.setAutoDraw(True)
        if bar_p3.status == STARTED:  # only update if drawing
            bar_p3.setPos(perf_pos[2], log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fbComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fb"-------
    for thisComponent in fbComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_loop.addData('bar_text.started', bar_text.tStartRefresh)
    block_loop.addData('bar_text.stopped', bar_text.tStopRefresh)
    block_loop.addData('bar_label_high.started', bar_label_high.tStartRefresh)
    block_loop.addData('bar_label_high.stopped', bar_label_high.tStopRefresh)
    block_loop.addData('bar_bar.started', bar_bar.tStartRefresh)
    block_loop.addData('bar_bar.stopped', bar_bar.tStopRefresh)
    block_loop.addData('bar_label_low.started', bar_label_low.tStartRefresh)
    block_loop.addData('bar_label_low.stopped', bar_label_low.tStopRefresh)
    block_loop.addData('bar_next.started', bar_next.tStartRefresh)
    block_loop.addData('bar_next.stopped', bar_next.tStopRefresh)
    # store data for block_loop (TrialHandler)
    block_loop.addData('bar_mouse.started', bar_mouse.tStart)
    block_loop.addData('bar_mouse.stopped', bar_mouse.tStop)
    block_loop.addData('bar_p1.started', bar_p1.tStartRefresh)
    block_loop.addData('bar_p1.stopped', bar_p1.tStopRefresh)
    block_loop.addData('bar_p2.started', bar_p2.tStartRefresh)
    block_loop.addData('bar_p2.stopped', bar_p2.tStopRefresh)
    block_loop.addData('bar_p3.started', bar_p3.tStartRefresh)
    block_loop.addData('bar_p3.stopped', bar_p3.tStopRefresh)
    # the Routine "fb" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    assess_emotion = data.TrialHandler(nReps=nSelf, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('self_report.xlsx', selection=whichSelf),
        seed=None, name='assess_emotion')
    thisExp.addLoop(assess_emotion)  # add the loop to the experiment
    thisAssess_emotion = assess_emotion.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAssess_emotion.rgb)
    if thisAssess_emotion != None:
        for paramName in thisAssess_emotion:
            exec('{} = thisAssess_emotion[paramName]'.format(paramName))
    
    for thisAssess_emotion in assess_emotion:
        currentLoop = assess_emotion
        # abbreviate parameter names if possible (e.g. rgb = thisAssess_emotion.rgb)
        if thisAssess_emotion != None:
            for paramName in thisAssess_emotion:
                exec('{} = thisAssess_emotion[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "assess"-------
        continueRoutine = True
        # update component parameters for each repeat
        on_scale = 0
        slf_mouse.setPos([0,-0.2])
        slf_text.setText(item)
        scale_low.setText(label_low)
        scale_high.setText(label_high)
        # setup some python lists for storing info about the slf_mouse
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        assessComponents = [slf_text, scale_low, scale_high, slf_scale, slf_set, slf_mouse]
        for thisComponent in assessComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        assessClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "assess"-------
        while continueRoutine:
            # get current time
            t = assessClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=assessClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            mx = slf_mouse.getPos()
            if mx[1] > -0.125 and mx[1] < -0.075:
                on_scale = 1
            mx[1] = -0.1
            if mx[0] <= -0.5:
                mx[0] = -0.5
            elif mx[0] >= 0.5:
                mx[0] = 0.5
            
            # *slf_text* updates
            if slf_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slf_text.frameNStart = frameN  # exact frame index
                slf_text.tStart = t  # local t and not account for scr refresh
                slf_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slf_text, 'tStartRefresh')  # time at next scr refresh
                slf_text.setAutoDraw(True)
            
            # *scale_low* updates
            if scale_low.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                scale_low.frameNStart = frameN  # exact frame index
                scale_low.tStart = t  # local t and not account for scr refresh
                scale_low.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(scale_low, 'tStartRefresh')  # time at next scr refresh
                scale_low.setAutoDraw(True)
            
            # *scale_high* updates
            if scale_high.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                scale_high.frameNStart = frameN  # exact frame index
                scale_high.tStart = t  # local t and not account for scr refresh
                scale_high.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(scale_high, 'tStartRefresh')  # time at next scr refresh
                scale_high.setAutoDraw(True)
            
            # *slf_scale* updates
            if slf_scale.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                slf_scale.frameNStart = frameN  # exact frame index
                slf_scale.tStart = t  # local t and not account for scr refresh
                slf_scale.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slf_scale, 'tStartRefresh')  # time at next scr refresh
                slf_scale.setAutoDraw(True)
            
            # *slf_set* updates
            if slf_set.status == NOT_STARTED and on_scale == 1:
                # keep track of start time/frame for later
                slf_set.frameNStart = frameN  # exact frame index
                slf_set.tStart = t  # local t and not account for scr refresh
                slf_set.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slf_set, 'tStartRefresh')  # time at next scr refresh
                slf_set.setAutoDraw(True)
            if slf_set.status == STARTED:  # only update if drawing
                slf_set.setPos(mx, log=False)
            # *slf_mouse* updates
            if slf_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slf_mouse.frameNStart = frameN  # exact frame index
                slf_mouse.tStart = t  # local t and not account for scr refresh
                slf_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slf_mouse, 'tStartRefresh')  # time at next scr refresh
                slf_mouse.status = STARTED
                slf_mouse.mouseClock.reset()
                prevButtonState = slf_mouse.getPressed()  # if button is down already this ISN'T a new click
            if slf_mouse.status == STARTED:  # only update if started and not finished!
                buttons = slf_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # abort routine on response
                        continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in assessComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "assess"-------
        for thisComponent in assessComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if nSelf == 1:
            currentLoop.addData('slf_question', item)
            currentLoop.addData('slf_response', mx[0] + 0.5)
        
        assess_emotion.addData('slf_text.started', slf_text.tStartRefresh)
        assess_emotion.addData('slf_text.stopped', slf_text.tStopRefresh)
        assess_emotion.addData('scale_low.started', scale_low.tStartRefresh)
        assess_emotion.addData('scale_low.stopped', scale_low.tStopRefresh)
        assess_emotion.addData('scale_high.started', scale_high.tStartRefresh)
        assess_emotion.addData('scale_high.stopped', scale_high.tStopRefresh)
        assess_emotion.addData('slf_scale.started', slf_scale.tStartRefresh)
        assess_emotion.addData('slf_scale.stopped', slf_scale.tStopRefresh)
        assess_emotion.addData('slf_set.started', slf_set.tStartRefresh)
        assess_emotion.addData('slf_set.stopped', slf_set.tStopRefresh)
        # store data for assess_emotion (TrialHandler)
        x, y = slf_mouse.getPos()
        buttons = slf_mouse.getPressed()
        assess_emotion.addData('slf_mouse.x', x)
        assess_emotion.addData('slf_mouse.y', y)
        assess_emotion.addData('slf_mouse.leftButton', buttons[0])
        assess_emotion.addData('slf_mouse.midButton', buttons[1])
        assess_emotion.addData('slf_mouse.rightButton', buttons[2])
        assess_emotion.addData('slf_mouse.started', slf_mouse.tStart)
        assess_emotion.addData('slf_mouse.stopped', slf_mouse.tStop)
        # the Routine "assess" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nSelf repeats of 'assess_emotion'
    
# completed 10 repeats of 'block_loop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
