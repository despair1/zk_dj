'''
Created on Oct 9, 2014

@author: despair1
'''

import hotshot.stats
#import sys

stats = hotshot.stats.load("../../myprof")
#stats.strip_dirs()
stats.sort_stats("cumulative")
stats.print_stats()