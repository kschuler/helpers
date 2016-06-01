#!/usr/bin/env python
'''
This is a script that I run whenever I start a new experiment.  It creates the folders and symbolic links for my experiment files.  It is an alias on my computer (mkexp)

alias mkexp="python /Users/kathrynschuler/git/helpers/init-new-experiment.py"

It helps me ensure that I keep good records of my experiments by forcing me to adhere to a consistent folder structure for all experiments.  More information about my workflow and how I document my studies at:

docs.kathrynschuler.com

The folder structure I use for experiment files as as follows:
Dropbox/
    Research/
        index.txt
        summaries/
            0010-srt-pilot-summary.pdf
        stimuli/
            0010-srt-pilot-stims/
        experiments/
            0010-srt-pilot-exp/
        subject-tracking/
            0010-srt-pilot-track.csv
        raw-data/
            0010-srt-pilot-data/
        analyses/
            0010-srt-pilot-analysis/
        figures/
            0010-srt-pilot-figs/

Research/ exists on my local computer in /Users/kathrynschuler/Dropbox/.

'''
import os

PATH = '/Users/kathrynschuler/Dropbox/Research/'
EXPID = raw_input('Enter experiment ID (e.g. 0010-srt-pilot): ')
# first add the expeirment to my list of experiments (index.txt)
# access with sort index.txt in the terminal for
# reading it in an ordered list (similiar to cat, but ordered)
with open(PATH+'index.txt', 'a') as f:
    f.write(EXPID+"\n")

# create local folders for stimuli and raw data
# these local folders are in dropbox as well
os.mkdir(PATH+'stimuli/'+EXPID+'-stims')
os.mkdir(PATH+'raw-data/'+EXPID+'-data')
os.mkdir(PATH+'figures/'+EXPID+'-figs')
os.mkdir(PATH+'experiments/'+EXPID+'-exp')
os.mkdir(PATH+'analyses/'+EXPID+'-analysis')

# Make the subject tracking file
open(PATH+"subject-tracking/"+EXPID+"-track.csv", 'a').close()


print "experiment "+EXPID+" has been created."
