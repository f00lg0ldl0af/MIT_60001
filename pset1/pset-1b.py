# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:28:41 2023

@author: LOHTECKFEILOHTECKFEI
"""

# Calculate how many mths to save for down payment 

# initialise variables 
portion_down_payment = 0.25
current_savings = 0
mth = 0

# user inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

# house down payment (fixed)
house_down_payment = portion_down_payment * total_cost

# savings for down payment each mth; shift loc (below) down since this is not fixed
# savings_mth = portion_saved * (annual_salary / 12)

# invested savings at annual ROR 4%
mth_rate_of_return = 0.04 / 12

while current_savings < house_down_payment:
    savings_mth = portion_saved * (annual_salary / 12)
    current_savings += savings_mth + (current_savings * mth_rate_of_return)
    mth += 1

    # increment after every 6 mths
    if mth % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    
print("Number of months: ", mth)