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
        fx= 0
        fy = 0
        sx = 0
        sy = 0
        infile = open('dots.txt', 'r')
        while True:
            sx = fx
            sy = fy
            line = infile.readline()
            if line == '':  break
            line = line.rstrip('\n')
            line = line.split('\t')
            sx = WIDTH*(int(line[0])/100)
            sy = HEIGHT*float(line[1])
            self.canvas.create_line(fx, fy, sx, sy)
            fx = sx
            fy = sy
        infile.close()
        self.canvas.pack()
        tkinter.mainloop()
my_grafic = grafic()