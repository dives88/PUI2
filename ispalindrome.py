import numpy as np
import sys


    
def lookforpal(text):
    #'''defines whether an imput is a palendrome or not'''
    text=sys.arg[1]
    if text.lower()==text.lower()[::-1]:
        message =  "Palindrome"
    else:
        message = "NOT Palindrome"
    return [message]

