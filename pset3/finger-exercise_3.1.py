# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:31:50 2023

@author: LOHTECKFEILOHTECKFEI
"""

def find_root():
    """
    Checks if integer entered by user has nth root
    given 0 < n < 6. Prints root and n, if any.
    If not, print a message to that effect.
    
    This uses exhaustive enumeration. Newton-Raphson method
    is faster.
    """
    number = int(input("Enter an integer: "))
    print("Finding root...")
    root_list = {}
    
    for pwr in range(2,6):
        root = 0
        while root**pwr < abs(number):
            root += 1
        if root**pwr == abs(number):
            root_list.update({root: pwr})
        
     
    if len(root_list) == 0:
        print("Number", number, "has no roots.")
    else:
        for k, v in root_list.items():
            print("Root:", k, "Power:", v)
             
# find_root()

def find_approx_root(epsilon):
    """
    Displays approximates of nth roots for integer entered 
    by user given 0 < n < 6. Prints root and n, if any.
    If not, print a message to that effect.
    
    epsilon: float >= 0 
        
    """
    x = input("Enter a number: ")
    try:
        number = float(x)
    except:
        print("Invalid entry.")
        
    print("Finding approximate root of {} ...".format(number))
    print("----------------------------------------------------------------------")

    guess_count = 0
    
    # for 0 < number < 1 or -1 < number < 0, make sure answer in search space
    if (number > 0 and number < 1) or (number > -1 and number < 0):
        low = abs(number)
        high = 1
    else:
        if number >= 1 or number <= -1:
            low = 0
            high = abs(number)
    guess_root = (low + high) / 2
    reset_guess_root = guess_root    
    reset_low = low
    reset_high = high
    
    root_list = {}

    # start bisection search
    # for negative numbers, possible roots: cube root(s) and/or 5th root(s) 
    if number < 0:
        start = 3
        stop = 6
        step = 2        
    else:
        start = 2
        stop = 6
        step = 1
    
    for exp in range(start,stop,step):
        # with every new exp, reset guess_root, low and high
        guess_root = reset_guess_root
        low = reset_low
        high = reset_high
        
        while abs(guess_root**exp - abs(number)) >= epsilon:
            guess_count += 1
            
            if (guess_root**exp) < abs(number):
                low = guess_root
            else:
                high = guess_root
                
            guess_root = (low + high) / 2
        
        if number < 0:
            root_list.update({-1*guess_root: exp})
        else:
            root_list.update({guess_root: exp})
        
    for k, v in root_list.items():
        print("Root: {:.2f}".format(k), "\nPower:", v)
        print("----------------------------------------------------------------------")
    
find_approx_root(0.01)

    
    