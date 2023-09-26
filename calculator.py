print("Welcome to my calculator")
print()
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication") #printed all the possible operations for the list
print("4.Division")
print("5.Floor Dvision")
print("6.Exponents")
print("7.Remainder")
print()
a = float(input("Enter your first digit:")) #input for the fisrt digit
b = float(input("Enter your second digit:")) #input for the second digit
c = int(input("Choose your operation number:")) #input for the operation

if c == 1: # used to print the first operation
    d = a + b
    print(d)
elif c == 2: # used to print the second operation
    d = a - b
    print(d)
elif c == 3: # used to print the third operation
    d= a * b
    print(d)
elif c == 4: # used to print the forth operation
    d = a /  b
    print(d) 
elif c == 5: # used to print the fifth operation
    d = a // b
    print(d)
elif c == 6: # used to print the sixth operation
    d = a ** b
    print(d)
elif c == 7: # used to print the seventh operation
    d = a % b
    print(d)
else:
    print("Invalid Input") # used if the user puts in an operation value that  is not valid