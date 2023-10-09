# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:53:21 2023

@author: LOHTECKFEILOHTECKFEI
"""

def search(L, e): # wrapper function 
    
    def bSearch(L, e, low, high):
        
        # check if last element contains e
        if high == low:
            return L[low] == e
        
        mid = (low + high) / 2
        
        if L(mid) == e:
            return True
        # look lower half of search space
        elif L(mid) > e: 
            if mid == low:
                return False
            return bSearch(L, e, low, mid - 1)
        else:
            # look upper half of search space
            return bSearch(L, e, mid + 1, high) 
        
        # alternative
        while low <= high:
            mid = (low + high)/2
            guess = L(mid)
            
            if guess == e:
                return True
            elif guess < e:
                low = mid + 1
            else:
                high = mid - 1
        return False