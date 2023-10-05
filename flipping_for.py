"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
a = 'Gorilla' #sets a variable
for animals in a: 
    print(animals)#prints my list

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
b = [1, 2] #sets variable
l = 0
for num in b: #prints my numbers
    l += num
    print(l)
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
my_string = 'Apes,Monkeys,Cheetahs,Elephants,jaguars,Lions' 
my_string = my_string.split(" ")
for we in my_string:
    print(we)
print(len(we))

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""