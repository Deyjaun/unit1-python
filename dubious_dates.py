import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print(datetime.datetime.now())

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
x= datetime.datetime.now()
print(x.strftime("%D"))
print(x.strftime("%T"))
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
str_d1 = '2023/10/12'
str_d2 = '2023/12/12'

d1 = datetime.strptime(str_d1, "%y/%m/%d")
d2 = datetime.strptime(str_d2, "%y/%m/%d")
delta = d2 - d1
print(f'Difference is {delta.days} days')
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""