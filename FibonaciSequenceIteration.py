#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:43:31 2020

@author: Alaisha Naidu

"""

#Question 1
#Fibonaci Sequence Iteration
def fibI(n):
    terms = [0,1]
    i = 2 
    while i <= n:
        terms.append(terms[i-1] + terms[i -2])
        i = i + 1
    return terms