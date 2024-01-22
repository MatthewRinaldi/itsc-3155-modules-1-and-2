numList = []
singleList = []
i = 0
x = 0

while i < 10:
    numList.append(input('Enter number ' + str(i+1) + ': '))
    i += 1
print('Original List: ', numList)

for elem in numList:
    for elem2 in numList:
        if elem == elem2:
            x += 1
    if x == 1:
        singleList.append(elem)
    x = 0
print('Nums that appear once: ', singleList)