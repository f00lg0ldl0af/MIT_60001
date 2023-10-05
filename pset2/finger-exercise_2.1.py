# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 17:26:00 2023

@author: LOHTECKFEILOHTECKFEI
"""
def is_odd(x):
    if int(x) % 2 != 0:
        return True
    else:
        return False

def largest_odd():
    """
    Returns largest odd number of user input(s).
    returns: int >= 0
    
    """
    num_list = []
    while True:
        num = input("Enter a value: ")
        num_list.append(num)
        

        if len(num_list) > 1:
            if num == "end":
                break
        else:
            if num == "end":
                print("Need at least more than one value.")        
        
    num_list.remove("end")
        
    # check for any even numbers
    for num in num_list:
        if is_odd(num):
            continue
        else:
            print(num + " is not odd.")
            num_list.remove(num) # remove even number
 
    print("Only comparing even numbers: ", *num_list)
    # compare odd numbers
    largest_odd = num_list[0]
    for num in num_list:
        if int(num) > int(largest_odd):
            largest_odd = num
    
    return largest_odd
 
print(largest_odd())
"""
Refactor old code 

    if total_num % 2 == 0:
        print("All numbers are even ")
                        
    # none of the numbers are odd
    if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
        print("All numbers are odd.")
        return
        
    # compare the two even numbers, if one number is odd
    list = []
    
    for i in:
        
    elif x % 2 == 0:
        if y < z:
            print("Largest odd number:", z)
            return z
        else:
            print("Largest odd number:", y)
            return y
    elif y % 2 == 0:
        if x < z:
            print("Largest odd number:", z)
            return z
        else:
            print("Largest odd number:", x)
            return x
    elif z % 2 == 0:
        if x < y:
            print("Largest odd number:", y)
            return y
        else:
            print("Largest odd number:", x)
            return x
    # all three numbers are odd
    else:
        if x < y and y < z:
            print("Largest odd number:", z)
            return z
        elif x < z and z < y:
            print("Largest odd number:", y)
            return y
        else:
            print("Largest odd number:", x)
            return x



x = int(input("Enter value for x: ")
y = int(input("Enter value for y: ")
z = int(input("Enter value for z: ")
largest_odd(x, y, z)
"""