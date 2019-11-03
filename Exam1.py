# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 23:49:36 2019

@author: swethap
"""

def main (): 
    sentence="The Python programming language makes manipulating strings very easy!"
    sentencelen=len(sentence)
    for i in range(0, sentencelen, 3): 
        print("Every third letter:", sentence[i])
        
main()