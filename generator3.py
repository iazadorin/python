# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:39:40 2021

@author: vedi
"""

outfile = open('dots.txt', 'w')
i = -2.1
while i<=2.1:
    y = -1/i
    y2 = 1/i
    outfile.write(str(i)+'\t'+str(y)+'\t'+str(y2)+'\n')
    i+=0.2
outfile.close()