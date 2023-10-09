# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:33:00 2023

@author: LOHTECKFEILOHTECKFEI
"""

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    # think about problem recursively
    def isPal(s):
        # base case: word only has one or zero chars
        if len(s) <= 1:
            return True
        else:
            # think of simpler problem version
            # say middle char is 1 char, check if first and last char is the same 
            # keep doing that until I can get down to something directly
            # solvable with base case
            return s[0] == s[-1] and isPal(s[1:-1])