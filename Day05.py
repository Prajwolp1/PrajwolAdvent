import re
order = []
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("input.txt")    
        
pages = []
order = []

for line in file_data:
    added = False
    for i in line:
        if i == "|":
            pages.append(line)
        if i == "," and not(added):
            order.append(line)
            added = True

columnOne = []
columnTwo = []
for line in pages:
    columnOne.append(line[0] + line[1])
    columnTwo.append(line[3] + line[4])

total = 0
for line in order:
    orderedOrder = line.split(",")
    
    count = 0
    for i in range(len(orderedOrder) - 1):
        for j in range(len(columnOne)):
            if columnOne[j] == orderedOrder[i] and columnTwo[j] == orderedOrder[i + 1]:
                count += 1
    if (count == len(orderedOrder) - 1):
        middle = int((len(orderedOrder) / 2))
        print(middle)
        total += int(orderedOrder[middle])

print(total)



