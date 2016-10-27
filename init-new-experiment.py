#!/usr/bin/env python
'''
This is a script that I run whenever I start a new experiment.  It creates the folders and symbolic links for my experiment files.  It is an alias on my computer (mkexp)

alias mkexp="python /Users/kathrynschuler/git/helpers/init-new-experiment.py"

It helps me ensure that I keep good records of my experiments by forcing me to adhere to a consistent folder structure for all experiments.  More information about my workflow and how I document my studies at:

guide.kathrynschuler.com

The folder structure I use for experiment files as as follows:
Dropbox/
    Research/
        all-experiments-database.xlsx
        all-experiments-index.txt
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
        processed-data/
            0010-srt-pilot-processed/
                processing script and any fils/folders
        analyses/
            0010-srt-pilot-analysis/
                0010-srt-pilot-analysis-R/
                0010-srt-pilot-analysis-SPSS/
        design-sheets/
            0010-srt-pilot-design.xlsx
        docs/
            0010-srt-pilot-docs/
                README.md
                plus any number of docs releated to this

if any folder is empty, there will be a README.md file to explain.


Research/ exists on my local computer in /Users/kathrynschuler/Dropbox/.

'''
import os

PATH = '/Users/kathrynschuler/Dropbox/Research/'
EXPID = raw_input('Enter experiment ID (e.g. 0010-srt-pilot): ')
# first add the expeirment to my list of experiments (index.txt)
# access with sort index.txt in the terminal for
# reading it in an ordered list (similiar to cat, but ordered)
with open(PATH+'all-experiments-index.txt', 'a') as f:
    f.write(EXPID+"\n")

# create local folders we need
os.mkdir(PATH+'stimuli/'+EXPID+'-stims')
os.mkdir(PATH+'raw-data/'+EXPID+'-data')
os.mkdir(PATH+'processed-data/'+EXPID+'-processed')
os.mkdir(PATH+'experiments/'+EXPID+'-exp')
os.mkdir(PATH+'analyses/'+EXPID+'-analysis')
os.mkdir(PATH+'docs/'+EXPID+'-docs')

# create subfolders
os.mkdir(PATH+'analyses/'+EXPID+'-analysis/'+EXPID+'analysis-R')
os.mkdir(PATH+'analyses/'+EXPID+'-analysis/'+EXPID+'analysis-SPSS')

# Create files
open(PATH+"subject-tracking/"+EXPID+"-track.csv", 'a').close()
with open(PATH+'docs/'+EXPID+'-docs/'+'README.txt', 'a') as f:
    f.write("This folder contains additional documents relevant to" + EXPID+"\n")
with open(PATH+'design-sheets/'+EXPID+'-design.txt', 'a') as f:
    f.write(EXPID+"\n")


print "experiment "+EXPID+" has been created."
