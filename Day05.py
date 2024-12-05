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
    for i in line:
        if i == "|":
            pages.append(line)
        if i == ",":
            order.append(line)

columnOne = []
columnTwo = []
for line in pages:
    columnOne.append(line[0] + line[1])
    columnTwo.append(line[3] + line[4])

total = 0
for line in order:
    splitLine = line.split(",")
    for lines in splitLine:
        print(lines)


