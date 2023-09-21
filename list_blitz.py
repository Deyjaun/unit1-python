"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
Movies = ["Chucky","Mario","Elvis","Barbie"] #Made movies equal to the list to give the list a value
print (Movies) #Used print to make my list show in terminal
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
Movies.append("Shrek")#used append to add a movie to the list
print(Movies)#used to print the updated list
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
Movies.remove("Barbie")#used remove to deleted a movie from the list
print(Movies)#used to print the updated list
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
Movies[0] = "IT"#used to change the first movie on my list to IT
print(Movies)#used to print the updated list
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
Movies.append("Dora")
Movies.append("Freddy")
print(Movies)
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
Movies.remove("Mario")
Movies.remove("Elvis")
print(Movies)
"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
Shows = [Movies[0:2]]
print(Shows)
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
