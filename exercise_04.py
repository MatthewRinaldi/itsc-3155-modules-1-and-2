# Used w3schools and the powerpoint offered in canvas

size = int(input('Enter a number: '))
i = 0
average = 0
numberList = []
while i < size:
    temp = float(input('Enter number: '))
    numberList.append(temp)
    i += 1
for elem in numberList:
    average += elem
print('List: ', numberList)
print('Average:', (average / size))