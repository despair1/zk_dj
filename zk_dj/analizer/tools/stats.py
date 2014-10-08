'''
Created on Oct 5, 2014

@author: despair1
'''

import pstats

s = pstats.Stats("/tmp/t_tstats")
s.sort_stats("time", "name").print_stats()