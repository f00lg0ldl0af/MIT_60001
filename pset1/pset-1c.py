"""Find best savings rate as function of 
starting salary to make down payment in 36 mths 
"""
import sys
print("Recursion limit:", sys.getrecursionlimit())

# user inputs
start_salary = float(input("Enter the starting salary: "))
    
# initialise variables 
semi_annual_raise = 0.07
monthly_ror  = 0.04 / 12
total_cost = 1000000
down_payment = 0.25 * total_cost
months = 36

"""avoid declaring pointless global variables
use local variable for passing and manipulating
data"""
#month = 0
#current_savings = 0 

# margin of error
margin_error = 100

# range for bisection search to find best savings rate
low = 0 # for 0%
high = 10000 # for 100% 
"""using this range prevents infinite no. of
decimals to search if range is between 0 and 1
"""
step = 0 

# bisection search 
def bisection_search(f, low, high, margin_error):
    global step 
    step += 1 
    m = (low + high) / 2
    
    if abs(f(m) - down_payment) < margin_error:
        return m
    elif f(m) < down_payment:
        return bisection_search(f, m, high, margin_error)
    elif f(m) > down_payment:
        return bisection_search(f, low, m, margin_error)

        
# function of starting salary takes savings rate and outputs current savings
def f(savings_rate):
    month = 0 
    current_savings = 0 
    annual_salary = start_salary
    
    while month < 37 and current_savings < down_payment:
        savings_mth = (savings_rate / 10000) * (annual_salary / 12)
        current_savings += savings_mth + (current_savings * monthly_ror)
        month += 1

        # increment after every 6 mths
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    return current_savings

try:
    best_saving_rate = bisection_search(f, 0, 10000, 100)
    print("Best savings rate: {:.4f}".format(best_saving_rate / 10000))
    print("Steps in Bisection search: {}".format(step))
except: # to account for RecursionError given no possible solutions
    print("It is not possible to pay the down payment in three years.")   