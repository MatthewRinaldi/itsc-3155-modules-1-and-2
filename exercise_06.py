# I used the powerpoint and w3schools. 
# I found how to print on the same line by googling it and coming across the 'end=" "' statement on tutorialspoint.com
# https://www.tutorialspoint.com/how-to-print-in-same-line-in-python

row = [0, 0, 0, 0, 0]
col = [0, 0, 0, 0, 0]

temp = int(input('Enter a row number from 1 to 5: ')) - 1
row[temp] = 1
temp = int(input('Enter a col number from 1 to 5: ')) - 1
col[temp] = 1

for elem in row:
    for elem2 in col:
        if elem == 1 and elem2 == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
