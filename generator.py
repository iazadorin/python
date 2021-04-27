# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:19:10 2021

@author: vedi
"""

import random
outfile = open('dots.txt', 'w')
i = 1
for i in range(100):
    y = random.randint(10, 20)
    outfile.write(str(i)+'\t'+str(y)+'\n')
outfile.close()