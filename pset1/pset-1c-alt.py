# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:02:43 2023

@author: LOHTECKFEILOHTECKFEI
"""

start_salary = float(input("Enter the starting salary: "))

# fixed variables
total_cost = 1000000
down_payment = 0.25 * total_cost
monthly_r = 0.04 / 12
semi_annual_raise = 0.07
months = 36

#sr for savings rate
margin_err = 100
low_sr = 0
start_high_sr = 10000 # for 100% sr
high_sr = start_high_sr
step = 0

current_savings = 0
best_sr = (low_sr + high_sr) / 2

while abs(current_savings - down_payment) > margin_err:
    step += 1
    current_savings = 0
    annual_salary = start_salary
    monthly_salary = annual_salary / 12
    monthly_saved = monthly_salary * (best_sr / 10000)
    
    for month in range(1, months + 1):
        current_savings += (current_savings * monthly_r)
        current_savings += monthly_saved
        
        if month % 6 == 0:
            annual_salary += (annual_salary * semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_saved = monthly_salary * (best_sr / 10000)
    
    # prev_sr would be used in conditional statement to break WHILE loop
    prev_sr = best_sr
    
    if current_savings < down_payment:
        low_sr = best_sr # sr need to be higher 
    else:
        high_sr = best_sr # sr can be lower
    
    best_sr = int(round((low_sr + high_sr) / 2))
    
    if prev_sr == best_sr:
        break

# Check    
if best_sr == start_high_sr:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: {}".format(round(best_sr / 10000, 4)))
    print("Steps in bisection search {}".format(step))    
    
    
    


