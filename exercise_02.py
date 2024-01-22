# I used w3schools to find the check string statement

inputOne = input('Enter a string: ')
inputTwo = input('Enter another string: ')
boolean = True
if inputOne in inputTwo:
    boolean = True
elif inputTwo in inputOne:
    boolean = True
else:
    boolean = False
print(boolean)