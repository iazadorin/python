# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:24:25 2021

@author: vedi
"""

import tkinter
import random
WIDTH = 900
HEIGHT = 900
class my_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window,
                                     width = WIDTH, height = HEIGHT)
        fx = 0
        fy = 0
        sx = 0
        sy = 0
        vx = 300
        vy = 400
        n = 0
        while n != 25:
            sx = fx + vx
            sy = fy + vy
            if sx >= WIDTH or sx<0:
                vx = -vx + random.randint(-20, 20)
                if sx<0:
                    sx = 0
                else:
                    sx=WIDTH
            if sy >= HEIGHT or sy<0:
                vy = -vy + random.randint(-20, 20)
                if sy<0:
                    sy = 0
                else:
                    sy=HEIGHT
            self.canvas.create_line(fx, fy, sx, sy)
            fx = sx
            fy = sy
            n+=1
        self.canvas.pack()
        tkinter.mainloop()
my_gui = my_GUI()