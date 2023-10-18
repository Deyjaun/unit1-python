"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def add_num(a):
    return a * a
x = add_num(4)
print(x)
assert add_num(4) == 16
assert add_num(9) == 81
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def add_area(a,b):
    return a * b
x = add_area(16,5)
print(x)
assert add_area(16,5) == 80
assert add_area(12,4) == 48
"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def con_cf(a):
    return (a * 9) / 5 + 32
x = con_cf(67)
print(x)
assert con_cf(67) == 152.6
assert con_cf(25) == 77.0
"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def avg_num(a):
    tot=sum(a)
    return tot/len(a)
a=avg_num({1,2,3,4,5})
print(a)