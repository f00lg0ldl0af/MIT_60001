# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 18:49:30 2023

@author: LOHTECKFEILOHTECKFEI
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# takes 11M+ recursive calls
print(fibonacci(3)) 

# this uses memoization
def fibonacci_efficient(n,dic):
    if n in dic:
        return dic[n]
    else:
        ans = fibonacci_efficient(n-1,dic) + fibonacci_efficient(n-2,dic)
        dic[n] = ans
        return ans

dic = {1:1, 2:2}
# using dictionary to keep track of intermediate values, takes 65 calls
print(fibonacci_efficient(34,dic)) 