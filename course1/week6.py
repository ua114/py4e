# Functions
#Make code that gives modulus
import math
# def complex_number(real,imaginary):
#     modulus = math.sqrt(real/imaginary)
#     print(modulus)
#
# complex_number(3.1,4)
#
# def greet():
#     return "Done"
#
# print(greet())

# Hypotnous calculator
# def hyp(a,b):
#     hyp_length = math.sqrt(a**2+b**2)
#     return hyp_length
#
# x = hyp(3,4)
# print(x)

# Exercise 4.6
def pay(h,r):
    if h <40:
        money = h*r
    else :
        money = 40*r + (h-40)*r*1.5
    return money

hours = input('Enter the number of hours:')
rate = input('Enter the pay rate:')
x = pay(int(hours),float(rate))
print(x)
