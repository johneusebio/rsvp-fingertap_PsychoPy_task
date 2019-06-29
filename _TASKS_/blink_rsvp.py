#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
NOTE TO SELF: for some reason the ttls are coming out in an improper order, 
and the responses aren't being recorded (though their accuracy is)

This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on May 22, 2018, at 11:14
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008

TTL 1: first stimulus has been displayed

TTL 4: a short-seperation trial is beginning
TTL 8: a long-seperation trial is beginning

TTL 11-19: The T1 stimulus +10 (the first number indicates which target stimulus it is)
TTL 21-29: The T2 stimulus +20 (the first number indicates which target stimulus it is)

TTL 254: Marks the end of the stimulus presentation phase

TTL 111-119: Participant's indicated T1 
TTL 121-129: Participant's indicated T2

TTL 210: Participant's T1 response was incorrect
TTL 211: Participant's T1 response was correct

TTL 220: Participant's T2 response was incorrect
TTL 221: Participant's T2 response was correct
'''

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
import random as rand
import pandas as pd
import string
# import SendKeys
# import win32api,win32con

# ==============================================================================
# USER PREFERENCES
# ==============================================================================

sendTTL    = False
colFont    = 'white' # font colour (rgb space)
colBkgd    = 'black' # background colour (rgb space)
colTest    = 'red'   # background colour for when sendTTL = False (rgb space)
stim_dur   = .050    # duration of stimulus presentation in seconds (0.05)
mask_dur   = .034    # duration of the mask in seconds (0.034)
iti_dur    = .75     # duration of ITI in seconds
fontSzStim = .5      # font size for the stimuli (starts at .1)

sep_short = 4 # SHORT number of stimuli that should seperate T1 from T2
sep_long  = 8 # LONG  number of stimuli that should seperate T1 from T2

nShortTrials = 4 #72  # number of short-interval trials
nLongTrials  = 9 #192 # number of long-interval trials

nBlocks = 2 # number of blocks in the task

parallelPortAddress = 61368 

# ==============================================================================
# SETUP EXPERIMENT
# ==============================================================================

if not sendTTL:
    colBkgd = colTest

def forceQuit():
    if sendTTL:
        port.setData(int(255))
    os.remove("tmp_stimuli.csv")
    core.quit()

# def isNumLockOn():
#     "return 1 if NumLock is ON"
#     return win32api.GetKeyState(win32con.VK_NUMLOCK)

# if isNumLockOn() != 1:
#     SendKeys.SendKeys("{NUMLOCK}")

event.globalKeys.add(key='escape', modifiers=['shift']           , func=forceQuit, name='forcequit')
# event.globalKeys.add(key='escape', modifiers=['shift', 'numlock'], func=forceQuit, name='forcequit')

if sendTTL:
    from psychopy import parallel
    port = parallel.ParallelPort(address = parallelPortAddress)
    port.setData(0) #make sure all pins are low

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'rsvp'  # from the Builder filename that created this script
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
    size=[3240, 2160], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=colBkgd, colorSpace='rgb',
    blendMode='avg', useFBO=True)
win.mouseVisible = False

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "code_Init"
code_InitClock = core.Clock()

# define trial types
trialType_stim = ['t1', 't2'] # stimulus condition types

# keeping track
trial_count = 0
block_count = 0

#create an array of short/long interval conditions

trialType_sep  = np.repeat(a = ['short', 'long'], repeats = [nLongTrials, nShortTrials])
trialType_sep  = np.repeat(a = trialType_sep    , repeats = len(trialType_stim))
trialType_stim = np.repeat(a = trialType_stim   , repeats = nLongTrials + nShortTrials)

# randomly re-order the arrays
np.random.shuffle(trialType_sep )
np.random.shuffle(trialType_stim)

#create an array of short/long interval conditions
trialType_mat  = np.stack((trialType_stim, trialType_sep))
trialType_mat = np.transpose(trialType_mat)

# number of trials
ntrials = trialType_mat.shape[0]

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruct_p1 = visual.TextStim(win=win, name='instruct_p1',
    text='Hello. Thank you for coming in today. \n\nFor this task, you will be asked to observe a series of characters flash on the screen and try to identify any number(s) you see in the stream. Numbers will be from 1 to 9. The characters will appear quickly, so you will have to pay close attention. \n\nSometimes a stream of characters will contain two numbers, and other times it will only contain one. Each stream will contain 15 to 19 characters and last for about a second. \n\nWhen two numbers are presented, please enter the numbers via keyboard in the order they were presented. When only one number is presented, enter in the number you saw along with any random number. \n\nPlease respond as accurately as you can. If you at any point are not sure which number(s) were presented, you can just guess. \n\nYou will be presented two blocks of this task; each block lasting between 13 to 15 minutes.\n\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=colFont, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "endTxt"
endTxtClock = core.Clock()
endTxt = visual.TextStim(win=win, name='endTxt',
    text='This part is done. Please inform the experimenter.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=colFont, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ready_block"
ready_blockClock = core.Clock()

ready = visual.TextStim(win=win, name='ready',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color=colFont, colorSpace='rgb', opacity=1,
    depth=-1.0);
go = visual.TextStim(win=win, name='go',
    text='GO',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color=colFont, colorSpace='rgb', opacity=1,
    depth=-2.0);
gap = visual.TextStim(win=win, name='gap',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color=colFont, colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "trial_def"
trial_defClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), wrapWidth=None, ori=0,
    color=colFont, colorSpace='rgb', opacity=0,
    depth=-1.0);

# Initialize components for Routine "disp_stimulus"
disp_stimulusClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=fontSzStim, wrapWidth=None, ori=0,
    color=colFont, colorSpace='rgb', opacity=1,
    depth=0.0);

mask = visual.TextStim(win=win, name='mask',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color=colFont, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "rec_resp_T1"
rec_resp_T1Clock = core.Clock()
Probe_t1 = visual.TextStim(win=win, name='Probe_t1',
    text='What numbers did you see?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color=colFont, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "rec_resp_T2"
rec_resp_T2Clock = core.Clock()
Probe_t2 = visual.TextStim(win=win, name='Probe_t2',
    text='What numbers did you see?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color=colFont, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "delay"
delayClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color=colBkgd, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "break"
BreakClock = core.Clock()
Break = visual.TextStim(win=win, name='Break',
    text="This block is done.\nPress SPACE when you're ready to continue",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color=colBkgd, colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ==============================================================================
# BEGIN EXPERIMENT
# ==============================================================================

# ------Prepare to start Routine "code_Init"-------
t = 0
code_InitClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
code_InitComponents = []
for thisComponent in code_InitComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "code_Init"-------
while continueRoutine:
    # get current time
    t = code_InitClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame


    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in code_InitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow: #or event.getKeys(keyList=["escape"])
        core.quit()


    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "code_Init"-------
for thisComponent in code_InitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "code_Init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
adv_p1 = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [instruct_p1, adv_p1]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instruct_p1* updates
    if t >= 0.0 and instruct_p1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct_p1.tStart = t
        instruct_p1.frameNStart = frameN  # exact frame index
        instruct_p1.setAutoDraw(True)

    # *adv_p1* updates
    if t >= 0.0 and adv_p1.status == NOT_STARTED:
        # keep track of start time/frame for later
        adv_p1.tStart = t
        adv_p1.frameNStart = frameN  # exact frame index
        adv_p1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if adv_p1.status == STARTED:
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
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=nBlocks, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:

    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))

    # ------Prepare to start Routine "ready_block"-------
    t = 0
    ready_blockClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.700000)
    # update component parameters for each repeat
    block_count = block_count + 1

    ready_txt = "Block " +  str(block_count)
    ready.setText(ready_txt + '\n\n' + "Ready?")
    # keep track of which components have finished
    ready_blockComponents = [ready, go, gap]
    for thisComponent in ready_blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "ready_block"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ready_blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame


        # *ready* updates
        if t >= 0.0 and ready.status == NOT_STARTED:
            # keep track of start time/frame for later
            ready.tStart = t
            ready.frameNStart = frameN  # exact frame index
            ready.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ready.status == STARTED and t >= frameRemains:
            ready.setAutoDraw(False)

        # *go* updates
        if t >= 1 and go.status == NOT_STARTED:
            # keep track of start time/frame for later
            go.tStart = t
            go.frameNStart = frameN  # exact frame index
            go.setAutoDraw(True)
        frameRemains = 1 + 0.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if go.status == STARTED and t >= frameRemains:
            go.setAutoDraw(False)

        # *gap* updates
        if t >= 1.5 and gap.status == NOT_STARTED:
            # keep track of start time/frame for later
            gap.tStart = t
            gap.frameNStart = frameN  # exact frame index
            gap.setAutoDraw(True)
        frameRemains = 1.5 + .2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if gap.status == STARTED and t >= frameRemains:
            gap.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow: # or event.getKeys(keyList=["escape"])
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "ready_block"-------
    for thisComponent in ready_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=ntrials, method='sequential',
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

        # ------Prepare to start Routine "trial_def"-------
        t = 0
        trial_defClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        trial_count = trial_count + 1
        stim_count  = 0 # keep track of which stimulus to display
        nstim = randint(15,19)

        trialType_cur = randint(0, np.shape(trialType_mat)[0]-1) # determine type of trial (eg. T2-present, long seperation)
        trialType_cur = trialType_mat[trialType_cur]
        stim_array    = [rand.choice(string.ascii_uppercase) for _ in range(nstim)] # begin building array of stimuli to be shown in this trial

        # determine the postions for the Target stimuli
        if trialType_cur[1] == 'long':
            t1_pos = np.random.choice(range(1,nstim - sep_long))
            t2_pos = t1_pos + sep_long
        elif trialType_cur[1] == 'short':
            t1_pos = np.random.choice(range(1,nstim - sep_short))
            t2_pos = t1_pos + sep_short

        # place the T1 target number into the stimulus array
        stim_array[t1_pos] = np.random.choice(range(1,9))

        # put T2 in the stimulus vector
        if trialType_cur[0] == 't2':
            stim_array[t2_pos] = np.random.choice(range(1,9))
        elif trialType_cur[0] == 't1':
            stim_array[t2_pos] = ' '

        # the 20% chance of the trial including a blank stimulus
        if trialType_cur[0] == 't2':
            roll_die = np.random.choice(range(1,5))
            if roll_die == 1:
                blank_pos = range(1,nstim)
                blank_pos.remove(t1_pos)
                blank_pos.remove(t2_pos)
                blank_pos = np.random.choice(blank_pos)

                stim_array[blank_pos] = ' '

        # create the columns to be saved
        sep_col   = [trialType_cur[1] for _ in range(nstim)]
        tnum_col  = [trialType_cur[0] for _ in range(nstim)]
        trial_col = [str(trial_count) for _ in range(nstim)]
        tnum_col  = [trialType_cur[0] for _ in range(nstim)]
        stimCount_col = range(1,nstim + 1)

        stim_cond = []
        for elem in range(len(stim_array)):
#            print(type(stim_array[elem]))
            if stim_array[elem] == ' ':
                stim_cond.append('mask')
            elif type(stim_array[elem]) is np.int32:
                stim_cond.append('target')
            elif type(stim_array[elem]) is str:
                stim_cond.append('distractor')

        trial_tab = np.vstack((trial_col, sep_col, tnum_col, stimCount_col, stim_array, stim_cond))
        trial_tab = np.transpose(trial_tab)
        trial_tab = pd.DataFrame(trial_tab)
        
        # print trial_tab

        # save dataframe to conditions *.csv file
        trial_tab.to_csv("tmp_stimuli.csv", header = ['block', 'sep_dur', 'Tx', 'trial', 'stimulus', 'cond'], index = False)
        text.setText(trial_count)
        # keep track of which components have finished
        trial_defComponents = [text]
        for thisComponent in trial_defComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
                
        if trialType_cur[1] == 'short':
            sep_ttl = sep_short
        elif trialType_cur[1] == 'long':
            sep_ttl = sep_long
            
        if sendTTL:
            port.setData(sep_ttl) # mark the end of stimulus presentation
        else:
            print("TTL {}".format(sep_ttl))

        # -------Start Routine "trial_def"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_defClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame


            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            frameRemains = 0.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_defComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow: # or event.getKeys(keyList=["escape"])
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial_def"-------
        for thisComponent in trial_defComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)


        # set up handler to look after randomisation of conditions etc
        stim = data.TrialHandler(nReps=1, method='sequential',
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('tmp_stimuli.csv'),
            seed=None, name='stim')
        thisExp.addLoop(stim)  # add the loop to the experiment
        thisStim = stim.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisStim.rgb)
        if thisStim != None:
            for paramName in thisStim:
                exec('{} = thisStim[paramName]'.format(paramName))


        trialOnsCount = 0
        targetList = []
        for thisStim in stim:
            frameCount=0
            if trialOnsCount == 0 and sendTTL:
                win.callOnFlip(port.setData, 1)
            elif trialOnsCount == 0 and not sendTTL:
                print "TTL 1"
            currentLoop = stim
            # abbreviate parameter names if possible (e.g. rgb = thisStim.rgb)
            if thisStim != None:
                for paramName in thisStim:
                    exec('{} = thisStim[paramName]'.format(paramName))
                if thisStim['cond'] == 'target' and frameCount == 0:
                    targetList.append(stimulus)
                    numTTL = int(stimulus) + len(targetList) * 10
                    # print stimulus
                    if sendTTL:
                        win.callOnFlip(port.setData, numTTL)
                    else:
                        print "TTL {}".format(numTTL)
                        
            # ------Prepare to start Routine "disp_stimulus"-------
            t = 0
            disp_stimulusClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(stim_dur + mask_dur)
            # update component parameters for each repeat
            text_2.setText(stimulus)
            # keep track of which components have finished
            disp_stimulusComponents = [text_2, mask]
            for thisComponent in disp_stimulusComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            

            # -------Start Routine "disp_stimulus"-------

            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = disp_stimulusClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame

                # *text_2* updates
                if t >= 0.0 and text_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_2.tStart = t
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.setAutoDraw(True)
                frameRemains = 0.0 + stim_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_2.status == STARTED and t >= frameRemains:
                    text_2.setAutoDraw(False)

                # *mask* updates
                if t >= .05 and mask.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    mask.tStart = t
                    mask.frameNStart = frameN  # exact frame index
                    mask.setAutoDraw(True)
                frameRemains = stim_dur + mask_dur - win.monitorFramePeriod * 0.75  # most of one frame period left
                if mask.status == STARTED and t >= frameRemains:
                    mask.setAutoDraw(False)

                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in disp_stimulusComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                # check for quit (the Esc key)
                if endExpNow: # or event.getKeys(keyList=["escape"])
                    core.quit()

                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#                    \
#                    if frameCount == 0:
#                        print stimulus
                    frameCount = frameCount + 1
                    trialOnsCount += 1
                    win.flip()
            
            # -------Ending Routine "disp_stimulus"-------
            for thisComponent in disp_stimulusComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.nextEntry()

        # completed 1 repeats of 'stim'
        if sendTTL:
            port.setData(254) # mark the end of stimulus presentation
        else:
            print "TTL 254"

        # ------Prepare to start Routine "rec_resp_T1"-------
        t = 0
        rec_resp_T1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        usr_input_t1 = event.BuilderKeyResponse()
        # keep track of which components have finished
        rec_resp_T1Components = [Probe_t1, usr_input_t1]
        for thisComponent in rec_resp_T1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "rec_resp_T1"-------
        while continueRoutine:
            # get current time
            t = rec_resp_T1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *Probe_t1* updates
            if t >= 1 and Probe_t1.status == NOT_STARTED:
                # keep track of start time/frame for later
                Probe_t1.tStart = t
                Probe_t1.frameNStart = frameN  # exact frame index
                Probe_t1.setAutoDraw(True)

            # *usr_input_t1* updates
            if t >= 1 and usr_input_t1.status == NOT_STARTED:
                # keep track of start time/frame for later
                usr_input_t1.tStart = t
                usr_input_t1.frameNStart = frameN  # exact frame index
                usr_input_t1.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(usr_input_t1.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if usr_input_t1.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9', 
                                                   'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9'])

                # check for quit:
                # if "escape" in theseKeys:
                #     endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if "num_" in theseKeys[0]:
                        theseKeys[0] = theseKeys[0].split("_")[1]
                    
                    if targetList[0] == theseKeys[0]:
                        acc_t1 = 211
                    else:
                        acc_t1 = 210

                    if sendTTL:
                        print "TTL {}".format(int(theseKeys[0]) + 110)
                        port.setData(int(theseKeys[0]) + 110) # send participant's t1 response
                        
                        port.setData(acc_t1)                  # send participant's t1 accuracy
                    else:
                        print "TTL {}".format(int(theseKeys[0]) + 110)
                        print "TTL {}".format(acc_t1)
                    if usr_input_t1.keys == []:  # then this was the first keypress
                        usr_input_t1.keys = theseKeys[0]  # just the first key pressed
                        usr_input_t1.rt = usr_input_t1.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rec_resp_T1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow: # or event.getKeys(keyList=["escape"])
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "rec_resp_T1"-------
        for thisComponent in rec_resp_T1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if usr_input_t1.keys in ['', [], None]:  # No response was made
            usr_input_t1.keys=None
        trials.addData('usr_input_t1.keys',usr_input_t1.keys)
        if usr_input_t1.keys != None:  # we had a response
            trials.addData('usr_input_t1.rt', usr_input_t1.rt)
        # the Routine "rec_resp_T1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        # ------Prepare to start Routine "rec_resp_T2"-------
        t = 0
        rec_resp_T2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        usr_input_t2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        rec_resp_T2Components = [Probe_t2, usr_input_t2]
        for thisComponent in rec_resp_T2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "rec_resp_T2"-------
        while continueRoutine:
            # get current time
            t = rec_resp_T2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *Probe_t2* updates
            if t >= 0.0 and Probe_t2.status == NOT_STARTED:
                # keep track of start time/frame for later
                Probe_t2.tStart = t
                Probe_t2.frameNStart = frameN  # exact frame index
                Probe_t2.setAutoDraw(True)

            # *usr_input_t2* updates
            if t >= 0.0 and usr_input_t2.status == NOT_STARTED:
                # keep track of start time/frame for later
                usr_input_t2.tStart = t
                usr_input_t2.frameNStart = frameN  # exact frame index
                usr_input_t2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(usr_input_t2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if usr_input_t2.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9', 
                                                   'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9'])

                # check for quit:
                # if "escape" in theseKeys:
                #     endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if "num_" in theseKeys[0]:
                        theseKeys[0] = theseKeys[0].split("_")[1]

                    if len(targetList) > 1:
                        if targetList[1] == theseKeys[0]:
                            acc_t2 = 221
                        else:
                            acc_t2 = 220
                    else:
                        acc_t2 = 220
                    
                    if sendTTL:
                        port.setData(int(theseKeys[0]) + 120)
                        port.setData(acc_t2)
                    else:
                        print "TTL {}".format(int(theseKeys[0]) + 120)
                        print "TTL {}".format(acc_t2)
                    if usr_input_t2.keys == []:  # then this was the first keypress
                        usr_input_t2.keys = theseKeys[0]  # just the first key pressed
                        usr_input_t2.rt = usr_input_t2.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rec_resp_T2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow: # or event.getKeys(keyList=["escape"])
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "rec_resp_T2"-------
        for thisComponent in rec_resp_T2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if usr_input_t2.keys in ['', [], None]:  # No response was made
            usr_input_t2.keys=None
        trials.addData('usr_input_t2.keys',usr_input_t2.keys)
        if usr_input_t2.keys != None:  # we had a response
            trials.addData('usr_input_t2.rt', usr_input_t2.rt)
        # the Routine "rec_resp_T2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        # ------Prepare to start Routine "delay"-------
#        if sendTTL:
#            port.setData(255) # mark the end of the trial
#        else:
#            print "TTL 255"

        t = 0
        delayClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(iti_dur)
        # update component parameters for each repeat
        # keep track of which components have finished
        delayComponents = [blank]
        for thisComponent in delayComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "delay"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = delayClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *blank* updates
            if t >= 0.0 and blank.status == NOT_STARTED:
                # keep track of start time/frame for later
                blank.tStart = t
                blank.frameNStart = frameN  # exact frame index
                blank.setAutoDraw(True)
            frameRemains = 0.0 + iti_dur - win.monitorFramePeriod * 0.75  # most of one frame period left
            if blank.status == STARTED and t >= frameRemains:
                blank.setAutoDraw(False)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in delayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow: # or event.getKeys(keyList=["escape"])
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "delay"-------
        for thisComponent in delayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()

    # completed ntrials repeats of 'trials'
    routineTimer.reset()
    thisExp.nextEntry()

    # ==========================================================================
    # Prepare to start Routine "Break"
    # ==========================================================================

    t = 0
    BreakClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    adv_Break = event.BuilderKeyResponse()
    # update component parameters for each repeat
    # keep track of which components have finished
    BreakComponents = [Break, adv_Break]
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Break"-------
    while continueRoutine:
        # get current time
        t = BreakClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *Break* updates
        if t >= 0.0 and instruct_p1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Break.tStart = t
            Break.frameNStart = frameN  # exact frame index
            Break.setAutoDraw(True)

        # *adv_Break* updates
        if t >= 0.0 and adv_Break.status == NOT_STARTED:
            # keep track of start time/frame for later
            adv_Break.tStart = t
            adv_Break.frameNStart = frameN  # exact frame index
            adv_Break.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if adv_Break.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow: # or event.getKeys(keyList=["escape"])
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

# completed nBlocks repeats of 'block'

# remove the tmp_stimuli.csv file
os.remove("tmp_stimuli.csv")

# ------Prepare to start Routine "endTxt"-------
t = 0
endTxtClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
end_p1 = event.BuilderKeyResponse()
# keep track of which components have finished
endTxtComponents = [endTxt, end_p1]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "endTxt"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instruct_p1* updates
    if t >= 0.0 and instruct_p1.status == NOT_STARTED:
        # keep track of start time/frame for later
        endTxt.tStart = t
        endTxt.frameNStart = frameN  # exact frame index
        endTxt.setAutoDraw(True)

    # *end_p1* updates
    if t >= 0.0 and end_p1.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_p1.tStart = t
        end_p1.frameNStart = frameN  # exact frame index
        end_p1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if end_p1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space', 'escape'])

        # check for quit:
        if "space" in theseKeys: #"escape" in theseKeys or 
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endTxtComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow: # or event.getKeys(keyList=["escape"])
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endTxt"-------
for thisComponent in endTxtComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check for quit (the Esc key)
if endExpNow: # or event.getKeys(keyList=["escape"])
    core.quit()

thisExp.nextEntry()
win.close()
core.quit()