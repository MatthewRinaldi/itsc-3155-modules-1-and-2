words = []
i = 0

while i < 5:
    words.append(input('Enter a word: '))
    i += 1
print('Words: ', words)

string = "One String: "
for elem in words:
    string += str(elem) + " "
print(string)