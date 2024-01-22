# I used w3schools to learn how to slice strings
# I got stuck on the listOfLists clearing alongside the stringList, I was able to find what was wrong by finding a similar problem on stackoverflow. 
# The response to that question explained that Lists are mutable types, meaning any changes to the stringList would affect my listOfLists. 
# The fix to this was simple, I just need to change my code so that the whenever I created a copy to my listOfLists, I did so explicitly.
# https://stackoverflow.com/questions/11487049/python-list-of-lists

string = input('Enter a string: ')
stringList = []
listOfLists = []
i = 0

while i < len(string):
    temp = (i+1) % 3
    stringList.append(string[i:i+1])
    
    if temp == 0:
        listOfLists.append(list(stringList))
        stringList.clear()
    elif (i+1) == len(string):
        listOfLists.append(list(stringList))
        stringList.clear()
    i += 1
print(listOfLists)