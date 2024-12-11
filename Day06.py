def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("input.txt")
count = 0
posX = 0
posY = 0
facing = ""
positions = []
for i in range(len(file_data)):
    for j in range(len(file_data[i])):
        if (file_data[i][j] == "^"):
            posY = i
            posX = j
            facing = "up"
        if (file_data[i][j] == ">"):
            posY = i
            posX = j
            facing = "right"
        if (file_data[i][j] == "<"):
            posY = i
            posX = j
            facing = "left"
        if (file_data[i][j] == "v"):
            posY = i
            posX = j
            facing = "down"
posX = int(posX)
posY = int(posY)
print(facing)
print(posX)
print(posY)
while True:
    if (facing == "up" and posY > 0):
        if (file_data[posX][posY - 1] != "#"):
            posY -= 1
            if (file_data[posX][posY] != "X"):
                count += 1
            else:
                file_data[posX][posY] == "X"
        else:
            facing = "right"
    else:
        break
    

