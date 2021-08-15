# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:19:10 2021

@author: vedi
"""

import math
outfile = open('dots.txt', 'w')
i = 0
while i<25.12:
    y = math.sin(i)
    y2 = math.sin(i*2)
    outfile.write(str(i)+'\t'+str(y)+'\t'+str(y2)+'\n')
    i+=0.01
outfile.close()