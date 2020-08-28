#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:48:20 2020

@author: Alaisha Naidu
Name: Palindrome check
"""

#Question 3
#Palindrome check
def PalCheck1(string): 
    # Comparing first and last, working inwards saves half the number of comparisons
    # than inverting each word and comparing every letter
    char_index1 = 0 
    char_index2 = len(string)-1
    while char_index1 <= char_index2: #work from outside inwards for shorter processing time
        if string[char_index1] == string[char_index2]:
            print(string[char_index1],string[char_index2], "True")
            char_index1 +=1
            char_index2 -=1
        else:
            return False

print(PalCheck1("racecar"))