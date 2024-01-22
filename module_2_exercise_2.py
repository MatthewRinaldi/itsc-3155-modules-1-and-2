# Used chatGPT to assist me in finding a proper sorting method

temp = input("Enter a string: ").strip()

def sortingMethod(char):
    return (char.isupper(), char.islower())

sortedString = ''.join(sorted(temp, key=sortingMethod))
print(sortedString)