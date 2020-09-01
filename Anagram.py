#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:29:20 2020

@author: Alaisha Naidu
Name: Anagram Check
"""

#Question 4
#Anagram check

from collections import Counter

def AnaCheck(string1, string2):
    str1 = string1.replace(" ", "")
    str2 = string2.replace(" ", "")
    if len(str1) == len(str2):
        count1 = Counter(str1)
        count2 = Counter(str2)
        print (count1-count2) #If it returns empty then it is an anagram
        if count1 == count2:
            print(string1,"-", string2, "\n", "This is an anagram")
        else:
            print(string1,"-", string2, "\n", "not an anagram")
    else:
        print(string1,"-", string2, "\n", "not an anagram")
        
print(AnaCheck("school master", "the classroom")) 