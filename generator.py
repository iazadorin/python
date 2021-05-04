# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:19:10 2021

@author: vedi
"""

import math
outfile = open('dots.txt', 'w')
i = 0
while i<12.56:
    y = math.sin(i)
    outfile.write(str(i)+'\t'+str(y)+'\n')
    i+=0.01
outfile.close()