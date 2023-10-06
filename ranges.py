"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for x in range (1,11,1):#sets the start number to one and counts by one till you get to ten
    print(x)#prints numbers from 1-10

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print("_________________")
for y in range (900,1001,10):#Starts at 900 and counts by 10 to 1000
    print(y)#prints numbers 900 to 1000 counting up by 10s
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print("________________")
for z in range (1,101,9):#starts at 1 and counts to 100 in intervals of 9
    print(z) #prints numbers 1-100 counting up by 9
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
print("______________________")
sum = 0
for z in range (1,11):
    sum+=z
print(sum)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()