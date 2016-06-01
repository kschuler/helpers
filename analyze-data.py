#!/usr/bin/env python
'''
This is a script that I run whenever I want to analyze data.  It requires that I have first added a copy of the raw data to the analysis folder, as well as already preprocessed the data.  It will ask to make sure I have completed these tasks. This file is aliased on my computer as:

alias analyze="python ~/git/helpers/analyze-data.py"


'''
import os
PATH = '/Users/kathrynschuler/Dropbox/Research/analyses'


RAWDATA = raw_input('Have you added the raw data? ')
PROCESSEDDATA = raw_input("Have you preprocessed the data? ")

if RAWDATA and PROCESSEDDATA :
    print 'opening jupyter...'
    os.system("cd "+PATH)
    os.system("source activate jupyter")
    os.system("jupyter notebook")
else :
    print 'please add raw data and preprocess before you analyze'
    print "exiting analysis"
