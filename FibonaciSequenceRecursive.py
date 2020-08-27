#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 19:13:41 2020

@author: Alaisha Naidu
Name: #Fibonaci Sequence Recursion 
"""

#Question 2
#Fibonaci Sequence Recursion 
def fibR(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return (fibR(n-1) + fibR(n-2)) #note problem of redundancy not solved in this function. Program takes a long time to work out big numbers 