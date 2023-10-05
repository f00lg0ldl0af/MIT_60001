# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:40:45 2023

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

# house down payment
house_down_payment = portion_down_payment * total_cost

# savings for down payment each mth 
savings_mth = portion_saved * (annual_salary / 12)

# invested savings at annual ROR 4%
mth_rate_of_return = 0.04 / 12

while current_savings < house_down_payment:
    current_savings += savings_mth + (current_savings * mth_rate_of_return)
    mth += 1
    
print("Number of months: ", mth)


