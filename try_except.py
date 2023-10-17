try:
   age = int(input('Enter your age: '))
except:
  print("unable to convert given number to int")
try:
  faveNum = int(input('What is your favorite number: '))
except:
  print("unable to convert given number to int")
if age <= 21:
 print('You are not allowed to enter, you are too young.')
else:
 print('Welcome, you are old enough.')

print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)