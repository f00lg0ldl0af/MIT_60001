# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:02:48 2023

@author: LOHTECKFEILOHTECKFEI

Recursion:
    - reduces problem to a simpler version of the same problem 
    - keep doing until I can get down to something I can solvely directly
    with a base case 
    - using that solution (gotten from base case) to solve the larger problem

"""

def printMove(fr, to):
    print("Move from " + str(fr) + ' to ' + str(to))
    
def Towers(n, fr, to, spare):
    # base case
    if n == 1:
        printMove(fr, to)
    
    # recursive case
    # smallest size-problem: moving tower of 2 stacks
    else:
        # move n - 1 stacks to spare; remaining bottom stack left in original 'fr' position
        Towers(n-1, fr, spare, to)
        # shift bottom stack to the 'to' position
        Towers (1, fr, to, spare)
        # shift back n - 1 stacks to the 'to' position
        Towers (n-1, spare, to, fr)
        
Towers(3, "fr", "to", "spare")