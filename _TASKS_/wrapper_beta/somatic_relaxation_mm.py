#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on October 03, 2018, at 12:01
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

# ==============================================================================
# IMPORT PACKAGES
# ==============================================================================

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from pygame import sndarray
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# ==============================================================================
# USER PREFERENCES
# ==============================================================================

sendTTL = True
colFont = 'white' # font colour (rgb space)
colBkgd = 'black' # background colour (rgb space)
colTest = 'red'   # background colour for when sendTTL = False (rgb space)

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
expName = u'audio'  # from the Builder filename that created this script
expInfo = {u'participant': u'10'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/John_%s_%s_%s' % (expName, expInfo['participant'], 'mm')

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
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=colBkgd, colorSpace='rgb',
    blendMode='avg', useFBO=True)
win.mouseVisible = False

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text=u'You are about to listen to a recording of a guided somatic relaxation. Please try to follow the instructions to the best of your ability while keeping still in your seat. The entire experience should last approximately 20 minutes. \n\nPress SPACE to continue.',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=colFont, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "stayStill"
stayStill = visual.TextStim(win=win, name='stayStill',
    text=u'Please keep relatively still while still following the directions.',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=colFont, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "intervention"
interventionClock = core.Clock()
sound_SR = sound.Sound(u'stimuli/body_scan_long_norm.ogg', secs=-1)
sound_SR.setVolume(1)

# Initialize components for Routine "ending"
endingClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'This part is done. Please inform the experimenter.',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=colFont, colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ==============================================================================
# BEGIN EXPERIMENT
# ==============================================================================

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
begin = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [Instructions, begin]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if t >= 0.0 and Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions.tStart = t
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.setAutoDraw(True)
    
    # *begin* updates
    if t >= 0.0 and begin.status == NOT_STARTED:
        # keep track of start time/frame for later
        begin.tStart = t
        begin.frameNStart = frameN  # exact frame index
        begin.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(begin.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if begin.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        # if "escape" in theseKeys:
        #     endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            begin.keys = theseKeys[-1]  # just the last key pressed
            begin.rt = begin.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow: # or event.getKeys(keyList=["escape"])
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if begin.keys in ['', [], None]:  # No response was made
    begin.keys=None
thisExp.addData('begin.keys',begin.keys)
if begin.keys != None:  # we had a response
    thisExp.addData('begin.rt', begin.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intervention"-------
t = 0
interventionClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(sound_SR.getDuration()) 
# update component parameters for each repeat
# keep track of which components have finished
interventionComponents = [sound_SR]
for thisComponent in interventionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "intervention"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = interventionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_SR

    if sendTTL:
        port.setData(int(1))
    else:
       print "TTL {}".format(int(1))

    if t >= 0.0 and sound_SR.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_SR.tStart = t
        sound_SR.frameNStart = frameN  # exact frame index
        sound_SR.play()  # start the sound (it finishes automatically)
        
        stayStill.tStart = t
        stayStill.frameNStart = frameN  # exact frame index
        stayStill.setAutoDraw(True)
    frameRemains = 0.0 + sound_SR.getDuration() - win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_SR.status == STARTED and t >= frameRemains:
        sound_SR.stop()  # stop the sound (if longer than duration)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in interventionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow: # or event.getKeys(keyList=["escape"])
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intervention"-------
for thisComponent in interventionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_SR.stop()  # ensure sound has stopped at end of routine
stayStill.setAutoDraw(False) # clear the text at the end of the routine

if sendTTL:
        port.setData(int(255))
else:
    print "TTL {}".format(int(255))

# ------Prepare to start Routine "ending"-------
t = 0
endingClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
end_exp = event.BuilderKeyResponse()
# keep track of which components have finished
endingComponents = [text, end_exp]
for thisComponent in endingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ending"-------
while continueRoutine:
    # get current time
    t = endingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    if text.status == STARTED and bool(0):
        text.setAutoDraw(False)
    
    # *end_exp* updates
    if t >= 0.0 and end_exp.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_exp.tStart = t
        end_exp.frameNStart = frameN  # exact frame index
        end_exp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_exp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if end_exp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        # if "escape" in theseKeys:
        #     endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            end_exp.keys = theseKeys[-1]  # just the last key pressed
            end_exp.rt = end_exp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow: # or event.getKeys(keyList=["escape"])
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ending"-------
for thisComponent in endingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_exp.keys in ['', [], None]:  # No response was made
    end_exp.keys=None
thisExp.addData('end_exp.keys',end_exp.keys)
if end_exp.keys != None:  # we had a response
    thisExp.addData('end_exp.rt', end_exp.rt)
thisExp.nextEntry()
# the Routine "ending" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
