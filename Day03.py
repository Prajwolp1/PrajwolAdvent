import re

def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("input.txt")
listOfNum = []
for line in file_data:
    x = re.findall("([(][0-9]+,[0-9]+[)])", line)
    listOfNum.append(x)
print(listOfNum)
sum = 0
for lines in listOfNum:
    for lineTwo in lines:
        splitLine = lineTwo.split(", ")
        print(splitLine)
        for i in range(len(splitLine)):
            print(i)
            if splitLine[i] == "(":
                sum += (splitLine[i + 1] * splitLine[i + 3])
                print(sum)
print(listOfNum)
