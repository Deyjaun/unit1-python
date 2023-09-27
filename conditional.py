'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
number = int(input("Enter number:")) #Made for the number input

if number > 10 and number % 2 == 0: #used to asked if the number chosen is greater than 10 and even
    print("True")#used if the statement is true
else:
    print ("False")# used if the statement is false
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
b = int(input('put your age:'))#used for age input
c = input('education')#used for education input
if b < 18 or c == 'yes': #used to see if your age is less than 18
    print('Price would be $10')
else:
    print('price would be $20')
'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
Student_grade = int(input("Enter your overall grade:"))
if Student_grade >= 90 and Student_grade < 101:
    print("you have an A!")
elif Student_grade >= 80 and Student_grade < 90:
    print("you have a B!")
elif Student_grade >= 70 and Student_grade < 80:
    print("you have a C!")
elif Student_grade <= 70:
    print("you have a F!")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
user=input("Enter the year:")
if int(user) %4 == 0 and int(user) %100 == 0:
    print("your year is a century and a leap year")
else:
    print("It's not a leap or a century year")
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''