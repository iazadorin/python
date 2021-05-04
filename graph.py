# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:25:42 2021

@author: vedi
"""
import tkinter
WIDTH = 300
HEIGHT = 300
GAPL = 20
GAPR = 20
GAPT = 20
GAPB = 20
STEP = 30
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
        maxValueY = dots[0][1]
        minValueY = dots[0][1]
        maxValueX = dots[0][0]
        minValueX = dots[0][0]
        for dot in dots:
            if dot[1]>maxValueY:
                maxValueY = dot[1]
            if dot[1]<minValueY:
                minValueY = dot[1]
        for dot in dots:
            if dot[0]>maxValueX:
                maxValueX = dot[0]
            if dot[0]<minValueX:
                minValueX = dot[0]
        fx = 0
        fy = 0
        sx = 0
        sy = 0
        stepNum = 0
        for dot in dots:
            sx = (WIDTH-GAPR-GAPL)*((dot[0]-minValueX)/(maxValueX-minValueX))+GAPL
            sy = (HEIGHT-GAPB-GAPT)*((dot[1]-minValueY)/(maxValueY-minValueY))+GAPT
            if stepNum!=0:  self.canvas.create_line(fx, fy, sx, sy, fill = 'firebrick')
            if stepNum%STEP==0:    self.canvas.create_oval(sx-1.5, sy-1.5, sx+1.5, sy+1.5, fill = 'firebrick')
            fx = sx
            fy = sy
            stepNum+=1
        infile.close()
        self.canvas.pack()
        tkinter.mainloop()
my_grafic = grafic()