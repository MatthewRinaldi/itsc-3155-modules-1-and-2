numList = []
evenList = []
i = 0

while i < 1:
    temp = input('Enter a number or QUIT to quit: ')
    
    if 'QUIT' in temp:
        break
    else:
        numList.append(int(temp))

print('All Nums: ', numList)

for elem in numList:
    temp = elem % 2
    if elem in evenList:
        i = 0
    elif temp == 0:
        evenList.append(elem)

print('Even Nums: ', evenList)