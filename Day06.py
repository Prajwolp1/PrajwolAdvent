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
posX = int(posX) + 1
posY = int(posY) + 1
print(facing)
print(posX)
print(posY)
while False:
    if facing == "up":
        print("up")
        if (posY - 1 >= 0 and file_data[posX][posY] != "#"):
            posY -= 1
            count += 1
        if (file_data[posX][posY] == "#"):
            facing = "right"
        if (posX - 1 < 0):
            break
    if facing == "down":
        print("down")
        if (posY + 1 < (len(file_data) - 1) and file_data[posX][posY] != "#"):
            posY += 1
            count += 1
        if (file_data[posX][posY] == "#"):
            facing = "right"
        if (posY + 1 > (len(file_data) - 1)):
            break
    if facing == "right":
        print("right")
        if (posX + 1 < (len(file_data[0]) - 1) and file_data[posX][posY] != "#"):
            posX += 1
            count += 1
        if (file_data[posX][posY] == "#"):
            facing = "up"
        if (posY + 1 > (len(file_data[0]) - 1)):
            break
    if facing == "left":
        print("left")
        if (posX - 1 >= 0 and file_data[posX][posY] != "#"):
            posX -= 1
            count += 1
        if (file_data[posX][posY] == "#"):
            facing = "down"
        if (posY + 1 > (len(file_data[0]) - 1)):
            break
        
print(count)
                
