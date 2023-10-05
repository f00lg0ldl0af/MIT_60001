# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:38:02 2023

@author: LOHTECKFEILOHTECKFEI
"""

def getBinaryRep(n, numDigits):
    """
    n, numDigits: int >= 0
    returns: str of length numDigits that is binary
    representation of n
    """
    # initialise str variable
    binstr = ''
    while n > 0:
        # each char of str is either '1' or '0'
        # 3 returns 11, 2 returns 10, 1 returns 1
        binstr = str(n % 2) + binstr
        n = n // 2
    # check if enough digits for binary representation
    if numDigits < len(binstr):
        raise ValueError("Not enough digits for binary representation.")
    # if more digits provided, add '0' in front of binstr
    for i in range(numDigits - len(binstr)):
        binstr = '0' + binstr
    return binstr

def getPowerSet(L):
    """
    Consider a list of n elements.
    Represent any combination of elements by 
    '0' (element absent) or
    '1' (element present).
    
    L: list of ints 
    returns: list of lists with permutations of L's ints
    
    L = [1,2] will return a list of lists: [ [1], [2], [1,2] ]
    """
    # superlist to store sublists
    superlist = []
    
    # to get sublists of list L of length n
    # generate binaries of 0 < num < 2**n
    for i in range(2**len(L)):
        binstr = getBinaryRep(i, len(L))
        # sublist to store each combination of '0's and '1's
        sublist = []
        # check if element present
        for j in binstr:
            if binstr[j] == '1':
                # append element to sublist
                sublist.append(L[j])
        superlist.append(sublist)
    return superlist
            
        
    
    
        
        