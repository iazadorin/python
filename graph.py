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
        infile.close()
        self.maxValueY = dots[0][1]
        self.minValueY = dots[0][1]
        self.maxValueX = dots[0][0]
        self.minValueX = dots[0][0]
        for dot in dots:
            if dot[1]>self.maxValueY:
                self.maxValueY = dot[1]
            if dot[1]<self.minValueY:
                self.minValueY = dot[1]
            if dot[0]>self.maxValueX:
                self.maxValueX = dot[0]
            if dot[0]<self.minValueX:
                self.minValueX = dot[0]
        fx = 0
        fy = 0
        sx = 0
        sy = 0
        stepNum = 0
        self.canvas.create_line(self.coordXCreator(self.minValueX),
                                self.coordYCreator(0),
                                self.coordXCreator(self.maxValueX),
                                self.coordYCreator(0))
        
        self.canvas.create_line(self.coordXCreator(0),
                                self.coordYCreator(self.maxValueY),
                                self.coordXCreator(0),
                                self.coordYCreator(self.minValueY))
        for dot in dots:
            sx = self.coordXCreator(dot[0])
            sy = self.coordYCreator(dot[1])
                        
            if stepNum!=0:  self.canvas.create_line(fx, fy, sx, sy, fill = 'firebrick')
            if stepNum%STEP==0:    self.canvas.create_oval(sx-1.5, sy-1.5, sx+1.5, sy+1.5, fill = 'firebrick')
            fx = sx
            fy = sy
            stepNum+=1
        
        
        self.canvas.pack()
        tkinter.mainloop()
    def coordXCreator(self, arg):
        return (WIDTH-GAPR-GAPL)*((arg-self.minValueX)/(self.maxValueX-self.minValueX))+GAPL
    def coordYCreator(self, arg):
        return (HEIGHT-GAPB-GAPT)*((arg-self.minValueY)/(self.maxValueY-self.minValueY))+GAPT
my_grafic = grafic()