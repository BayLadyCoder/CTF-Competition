def findRepeatChar(text):
    theList = []
    chars = {}
    for char in text:
        if char not in chars.keys():
            chars[char] = 1
        else:
            chars[char] = chars[char]+1
    chars = sorted(chars.items(), key=lambda x: x[1], reverse=False)

    print(chars)

# file = open('text1.txt', 'r')
# list = list(file)
string = ""
with open('text1.txt') as f:
    for line in f:
        line = line.split()
        for text in line:
            string+=text
    print(string)
    # result = [list(line.rstrip()) for line in list]
# print(list)
findRepeatChar(string)
