# Used the powerpoint provided on canvas

listOne = []
listTwo = []
commonList = []
i = 0
while i < 5:
    listOne.append(input('Enter a number for the first list: '))
    i += 1

i = 0
while i < 5:
    listTwo.append(input('Enter a number for the second list: '))
    i += 1

print('First List: ', listOne)
print('Second List: ', listTwo)

for elem in listOne:
    if elem in commonList:
        i = 0
    elif elem in listTwo:
        commonList.append(elem)

print('Common List: ', commonList)