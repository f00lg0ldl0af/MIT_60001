# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:18:10 2023

@author: LOHTECKFEILOHTECKFEI
"""

# bisection method to find cube root 
"""Note: typically, when applying bisection method to find
cube root of numbers, initial upper bound is set as cube.
However, this does not work for numbers that are in range 
of - 1 and 1, since cube root (i.e., answer) of such numbers 
is bigger than the number itself. So set initial upper bound as 1""" 

x = input("Enter a number: ")
try:
    cube = float(x)
except:
    print("Invalid entry.")
    
# for 0 < numbers < 1 or -1 < numbers < 0 
if (cube > 0 and cube < 1) or (cube > -1 and cube < 0):
    low = abs(cube)
    high = 1
else:
    if cube >= 1 or cube <= -1:
        low = 0
        high = abs(cube)
guess = (low + high) / 2

# initialise variables 
epsilon = 0.01
guess_count = 0

# start bisection search 
while abs(guess**3 - cube) >= epsilon:
    guess_count += 1
    if guess**3 < cube:
        low = guess # look up in upper half search space
    else:
        high = guess # look up in lower half search space
    guess = (low + high) / 2
    
if cube > 0:
    print("Cube root of {} is".format(cube), guess)
else:
    print("Cube root of {} is".format(cube), -1*guess)
    
print("Guesses taken:", guess_count)      
        
        
        
        
        
        
        
        
        
        