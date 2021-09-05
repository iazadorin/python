# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:39:40 2021

@author: vedi
"""

outfile = open('dots.txt', 'w')
i = -4
while i<=4:
    y = abs(2*i)
    y2 = i*i
    outfile.write(str(i)+'\t'+str(y)+'\t'+str(y2)+'\n')
    i+=0.1
outfile.close()