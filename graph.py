# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:25:42 2021

@author: vedi
"""
import tkinter
WIDTH = 300
HEIGHT = 300
class grafic():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window,
                                     width = WIDTH, height = HEIGHT)
        
        dots = []
        infile = open('dots.txt', 'r')
        while True:
            line = infile.readline()
            if line == '':  break
            line = line.rstrip('\n')
            line = line.split('\t')
            dots.append((float(line[0]),float(line[1])))
        maxValue = dots[0][1]
        minValue = dots[0][1]
        for dot in dots:
            if dot[1]>maxValue:
                maxValue = dot[1]
            if dot[1]<minValue:
                minValue = dot[1]
        fx= 0
        fy = 0
        sx = 0
        sy = 0
        for dot in dots:
            sx = WIDTH*dot[0]/100
            sy = HEIGHT*(dot[1]-minValue)/(maxValue-minValue)
            self.canvas.create_line(fx, fy, sx, sy)
            fx = sx
            fy = sy
        infile.close()
        self.canvas.pack()
        tkinter.mainloop()
my_grafic = grafic()