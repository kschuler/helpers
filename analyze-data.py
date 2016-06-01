#!/usr/bin/env python
'''
This is a script that I run whenever I want to analyze data.  It requires that I have first added a copy of the raw data to the analysis folder, as well as already preprocessed the data.  It will ask to make sure I have completed these tasks. This file is aliased on my computer as:

alias analyze="python ~/git/helpers/analyze-data.py"

run it by typing "analyze" in the terminal


'''
import os
PATH = '/Users/kathrynschuler/Dropbox/Research/analyses'
os.chdir(PATH)


RAWDATA = raw_input("Have you added the raw data? (y/n) ")
PROCESSEDDATA = raw_input("Have you preprocessed the data? (y/n) ")

if RAWDATA == 'y' and PROCESSEDDATA == 'y' :
    print 'opening jupyter...'
    os.system("source activate jupyter")
    os.system("jupyter notebook")
else :
    print 'please add raw data and preprocess before you analyze'
    print "exiting analysis"
