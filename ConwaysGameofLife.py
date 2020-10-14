#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:41:39 2020

@author: Alaisha Naidu
Name: Conway's Game of Life
Creds: Giuseppe Vettigli
"""

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

def Life(X, steps):
    
    def roll_it(x,y):
        return np.roll(np.roll(X, y, axis=0), x, axis=1)
    
    for _ in range(steps):
        Y = roll_it(1,0) + roll_it(0,1) + roll_it(-1,0) \
            + roll_it(0,-1) + roll_it(1,1) + roll_it(-1, -1) \
            + roll_it(1,-1) + roll_it(-1, 1)
        X = np.logical_or(np.logical_and(X, Y == 2), 3)
        X = X.astype(int)
        yield Y
        
X = np.zeros((40, 40))

X[23, 22:24]= 1
X[24, 21:23]= 1
X[25, 22]= 1

FFpegWriter = manimation.writers['ffmpeg']
metadata = dict(title = "Conway's Game of Life", artist = "Alaisha" )
writer = FFpegWriter(fps = 10, metadata = metadata)

fig = plt.figure()
fig.patch.set_facecolor('black')
with writer.saving(fig, "game_of_life.mp4", 200):
    plt.spy(X)
    plt.axis('off')
    writer.grab_frame()
    plt.clf()
    for x in Life(X, 800):
        plt.spy(x)
        plt.axis('off')
        writer.grab_frame()
        plt.clf()
    

