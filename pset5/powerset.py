"""
Created on Fri Oct  6 20:41:25 2023

@author: LOHTECKFEILOHTECKFEI
"""

def powerSet(L):
    """
    L: list of integers
    returns: list of lists containing all possible combinations of
    integers in L 
    """
    
    # base case 
    if len(L) == 0:
        return [[]]
    
    # recursive case
    else:
        # take all subsets without last element
        subset = powerSet(L[:-1])
        # create list for last element, with colon (without colon, its just indexing)
        last_char = L[-1:] 
        new = []
        # iterate through the element in subset
        for sub in subset:
            # create new list (with last element) by concatenating lists
            new.append(sub + last_char)
                
    return subset + new
    

L = [1,2]
print(powerSet(L))
# should return [], [1], [2], [1,2]