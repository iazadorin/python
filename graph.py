# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:25:42 2021

@author: vedi
"""
import tkinter
WIDTH = 300
HEIGHT = 300
GAPL = 20
GAPR = 30
GAPT = 20
GAPB = 30
STEP = 30
STICK = 20
ARROWL = 10
ARROWW = 3
TICKNX = 5
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
        x = self.coordXCreator(self.maxValueX)+STICK
        y = self.coordYCreator(0)
        self.canvas.create_line(self.coordXCreator(self.minValueX),
                                y,
                                x,
                                y)
        
        self.canvas.create_line(x,
                                y,
                                x-ARROWL,
                                y+ARROWW)
        
        self.canvas.create_line(x,
                                y,
                                x-ARROWL,
                                y-ARROWW)
        
        self.canvas.create_text(self.coordXCreator(0)-10, y+10, text = '0')
        self.canvas.create_text(self.coordXCreator(self.maxValueX)+20, y+10, text = 'X')
        self.canvas.create_text(self.coordXCreator(0)-10, self.coordYCreator(self.maxValueY)-20, text = 'Y')
        
        x = self.coordXCreator(0)
        y = self.coordYCreator(self.maxValueY)-STICK
        
        self.canvas.create_line(x,
                                self.coordYCreator(self.minValueY),
                                x,
                                y)
        
        self.canvas.create_line(x,
                                y,
                                x-ARROWW,
                                y+ARROWL)
        
        self.canvas.create_line(x,
                                y,
                                x+ARROWW,
                                y+ARROWL)
        
        for dot in dots:
            sx = self.coordXCreator(dot[0])
            sy = self.coordYCreator(dot[1])
            
            if stepNum!=0:  self.canvas.create_line(fx, fy, sx, sy, fill = 'firebrick')
            if stepNum%STEP==0:
                self.canvas.create_oval(sx-1.5, sy-1.5, sx+1.5, sy+1.5, fill = 'firebrick')
            fx = sx
            fy = sy
            stepNum+=1
            
            
        x = self.minValueX
        hg = (self.maxValueX-self.minValueX)/TICKNX
        while x < self.maxValueX:
            a = self.coordXCreator(x)
            b = self.coordYCreator(0)
            self.canvas.create_line(a, b+5, a, b-5)
            if x>self.minValueX:   self.canvas.create_text(a, b+4, anchor=tkinter.NW, text="%.2f" % x)
            x+=hg
        self.canvas.pack()
        tkinter.mainloop()
    def coordXCreator(self, arg):
        return (WIDTH-GAPR-GAPL)*((arg-self.minValueX)/(self.maxValueX-self.minValueX))+GAPL
    def coordYCreator(self, arg):
        return HEIGHT-((HEIGHT-GAPB-GAPT)*((arg-self.minValueY)/(self.maxValueY-self.minValueY))+GAPT)
my_grafic = grafic()