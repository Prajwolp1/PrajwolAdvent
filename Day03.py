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
    x = re.findall("(mul[(][0-9]+,[0-9]+[)])", line)
    listOfNum.append(x)

sum = 0
for lines in listOfNum:
    for lineTwo in lines:
        numList = []
        x = re.findall("[0-9]+", lineTwo)
        numList.append(x)
        print(numList)
        print(numList[0][0])
        print(numList[0][1])
        sum += int(numList[0][0]) * int(numList[0][1])
    
print(sum)
