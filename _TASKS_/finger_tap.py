#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on September 24, 2018, at 15:17
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008

TTL 10  = practice press
TTL 100 = space bar press
"""

# ==============================================================================
# IMPORT PACKAGES
# ==============================================================================

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# ==============================================================================
# USER PREFERENCES
# ==============================================================================

sendTTL    = True
duration_s = 240     # how long the task lasts in seconds (not including training)
colFont    = 'white' # font colour (rgb space)
colBkgd    = 'black' # background colour (rgb space)
colTest    = 'red'   # background colour for when sendTTL = False (rgb space)

parallelPortAddress = 61368 

# ==============================================================================
# SETUP EXPERIMENT
# ==============================================================================

if not sendTTL:
    colBkgd = colTest

def forceQuit():
    if sendTTL:
        port.setData(int(255))
    core.quit()

event.globalKeys.add(key='escape', modifiers=['shift']           , func=forceQuit, name='forcequit')
event.globalKeys.add(key='escape', modifiers=['shift', 'numlock'], func=forceQuit, name='forcequit')

if sendTTL:
    from psychopy import parallel
    port = parallel.ParallelPort(address = parallelPortAddress)
    port.setData(0) #make sure all pins are low

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'tap'  # from the Builder filename that created this script
expInfo = {u'run': u'r', u'participant': u'10'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/John_%s_%s_%s' % (expName, expInfo['participant'], expInfo['run'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[2160, 1440], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=colBkgd, colorSpace='rgb',
    blendMode='avg', useFBO=True)
win.mouseVisible = False

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions_2"
instructions_2Clock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text=u'For this next task, you will be asked to press the space bar once every 600 ms (0.6 seconds). A metronome sound will be played during the first 10 seconds to help you establish a rythm. Afterwards, you are to continue this rythm to the best of your ability for 4 minutes.\n\nPlease keep your eyes open and fixed on the crosshairs.\n\nPress Space to continue.',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=colFont, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "inter_stimulus"
inter_stimulusClock = core.Clock()
blank_iti = visual.TextStim(win=win, name='blank_iti',
    text=None,
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=colFont, colorSpace='rgb', opacity=1,
    depth=0.0);

# define crosshair
crosshair = visual.TextStim(win, 
    text='+', 
    font='', 
    color=colFont, 
    name='crosshair');
crosshair_Clock = core.Clock()

# Initialize components for Routine "training"
trainingClock = core.Clock()
tick = sound.Sound(u'../stimuli/clock-tick1.wav', secs=0.1)
tick.setVolume(1)

# Initialize components for Routine "pressing"
pressingClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ==============================================================================
# BEGIN EXPERIMENT
# ==============================================================================

# ------Prepare to start Routine "instructions_2"-------
t = 0
instructions_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
space_start = event.BuilderKeyResponse()
# keep track of which components have finished
instructions_2Components = [instructions_text, space_start]
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions_2"-------
while continueRoutine:
    # get current time
    t = instructions_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_text* updates
    if t >= 0.0 and instructions_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_text.tStart = t
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.setAutoDraw(True)
    
    # *space_start* updates
    if t >= 0.0 and space_start.status == NOT_STARTED:
        # keep track of start time/frame for later
        space_start.tStart = t
        space_start.frameNStart = frameN  # exact frame index
        space_start.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if space_start.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        # if "escape" in theseKeys:
        #     endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow: # or event.getKeys(keyList=["escape"])
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_2"-------
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inter_stimulus"-------
t = 0
inter_stimulusClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
inter_stimulusComponents = [blank_iti]
for thisComponent in inter_stimulusComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inter_stimulus"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = inter_stimulusClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank_iti* updates
    if t >= 0.0 and blank_iti.status == NOT_STARTED:
        # keep track of start time/frame for later
        blank_iti.tStart = t
        blank_iti.frameNStart = frameN  # exact frame index
        blank_iti.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if blank_iti.status == STARTED and t >= frameRemains:
        blank_iti.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inter_stimulusComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow: # or event.getKeys(keyList=["escape"])
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inter_stimulus"-------
for thisComponent in inter_stimulusComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
train_loop = data.TrialHandler(nReps=17, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='train_loop')
thisExp.addLoop(train_loop)  # add the loop to the experiment
thisTrain_loop = train_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrain_loop.rgb)
if thisTrain_loop != None:
    for paramName in thisTrain_loop:
        exec('{} = thisTrain_loop[paramName]'.format(paramName))

# setup crosshair
completeFrameN = -1
crosshair_Clock.reset()

for thisTrain_loop in train_loop:
    completeFrameN += 1

    # *crosshair* updates
    t = crosshair_Clock.getTime()
    if t >= 0.0 and crosshair.status == NOT_STARTED:
        # keep track of start time/frame for later
        crosshair.tStart = t
        crosshair.frameNStart = completeFrameN  # exact frame index
        crosshair.setAutoDraw(True)
    
    currentLoop = train_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrain_loop.rgb)
    if thisTrain_loop != None:
        for paramName in thisTrain_loop:
            exec('{} = thisTrain_loop[paramName]'.format(paramName))
    
    crosshair.setAutoDraw(True)

    # ------Prepare to start Routine "training"-------
    t = 0
    trainingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.600000)
    # update component parameters for each repeat
    train_press = event.BuilderKeyResponse()
    tick.setSound(u'../stimuli/clock-tick1.wav', secs=0.1)
    # keep track of which components have finished
    trainingComponents = [train_press, tick]
    for thisComponent in trainingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "training"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trainingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *train_press* updates
        if t >= 0.0 and train_press.status == NOT_STARTED:
            # keep track of start time/frame for later
            train_press.tStart = t
            train_press.frameNStart = frameN  # exact frame index
            train_press.status = STARTED
            # keyboard checking is just starting
        frameRemains = 0.0 + .6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if train_press.status == STARTED and t >= frameRemains:
            train_press.status = STOPPED
        if train_press.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

            # check for quit:
            # if "escape" in theseKeys:
            #     endExpNow = True
            # send practice TTL
            if "space" in theseKeys:
                if sendTTL:
                    port.setData(int(10))
                else:
                    print "TTL {}".format(int(10))

        # start/stop tick
        if t >= 0.0 and tick.status == NOT_STARTED:
            # keep track of start time/frame for later
            tick.tStart = t
            tick.frameNStart = frameN  # exact frame index
            tick.play()  # start the sound (it finishes automatically)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow: # or event.getKeys(keyList=["escape"])
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            if sendTTL:
                port.setData(int(0))
    
    # -------Ending Routine "training"-------
    for thisComponent in trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    tick.stop()  # ensure sound has stopped at end of routine
    thisExp.nextEntry()
    
# completed 17 repeats of 'train_loop'


# ------Prepare to start Routine "pressing"-------
t = 0
pressingClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(duration_s)
# update component parameters for each repeat
button_press = event.BuilderKeyResponse()
# keep track of which components have finished
pressingComponents = [button_press]
for thisComponent in pressingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "pressing"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = pressingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *button_press* updates
    if t >= 0.0 and button_press.status == NOT_STARTED:
        # keep track of start time/frame for later
        button_press.tStart = t
        button_press.frameNStart = frameN  # exact frame index
        button_press.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(button_press.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + duration_s - win.monitorFramePeriod * 0.75  # most of one frame period left
    if button_press.status == STARTED and t >= frameRemains:
        button_press.status = STOPPED
    if button_press.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        # if "escape" in theseKeys:
        #     endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            button_press.keys.extend(theseKeys)  # storing all keys
            button_press.rt.append(button_press.clock.getTime())
            if sendTTL:
                port.setData(int(100))
            else:
                print "TTL {}".format(int(100))
                    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pressingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow: # or event.getKeys(keyList=["escape"])
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        if sendTTL:
            port.setData(int(0))

# -------Ending Routine "pressing"-------
for thisComponent in pressingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if button_press.keys in ['', [], None]:  # No response was made
    button_press.keys=None
thisExp.addData('button_press.keys',button_press.keys)
if button_press.keys != None:  # we had a response
    thisExp.addData('button_press.rt', button_press.rt)
thisExp.nextEntry()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
