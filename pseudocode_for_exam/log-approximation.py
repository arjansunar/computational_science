"""
function to approximate the natural log of a variable x
"""
import math
from xmlrpc.client import MAXINT

math.log


def ln(x): 
    n= 1000
    sum=0
    if (x< 0):  return math.nan;
    if (x == 0):  return MAXINT;
    if (x == 1): return 0

    if (x > 10):
        return ln(x/5) + ln(5)
    if (x < 1/2):
        # changing smaller values into their bigger forms using log properties
        return ln(2*x) + ln(0.5)
    
    for i in range (1, n):
        # formula for when x > 1/2
        sum += (1/i)*((x-1)/x)** i
    return sum 

def log_a_of_x(a, x):
    return ln(x)/ln(a)

print(f'log 10 of 10 {round(log_a_of_x(10, 10), 10)}')
print(f'log 10 of 100 {round(log_a_of_x(10, 100), 10)}')
print(f'log 10 of 1000 {round(log_a_of_x(10, 1000), 10)}')
print(f'log 10 of 10000 {round(log_a_of_x(10, 10000), 10)}')
print(f'log 10 of 100000 {round(log_a_of_x(10, 100000), 10)}')
print(f'log 10 of 10000000 {round(log_a_of_x(10, 10000000), 10)}')
print(f'log 0.983 of 1000 {round(log_a_of_x(0.983, 1000), 10)}')
print(f'log 123 of 8909 {round(log_a_of_x(123, 8909), 10)}')