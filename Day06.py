def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def checkedValue(y_value, x_value):
    for i in range(len(checkedY)):
        if (checkedY[i] == y_value and checkedX[i] == x_value):
            return False
    return True
    



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
posY = int(posY)
posX = int(posX)
end = False
checkedY = []
checkedX = []
while not end:
    if facing == "up" and posY >= 0:
        if (file_data[posY - 1][posX] != "#"):
            if (checkedValue(posY - 1, posX)):
                count += 1
                checkedY.append(posY)
                checkedX.append(posX)
            posY -= 1
        if (posY <= 0):
            end = True
        if not end:
            if (file_data[posY - 1][posX] == "#"):
                facing = "right"
    if facing == "right" and posX < len(file_data[posY]) - 1:
        if (file_data[posY][posX + 1] != "#"):
            if (checkedValue(posY, posX + 1)):
                count += 1
                checkedY.append(posY)
                checkedX.append(posX)
            posX += 1
            
        if (posX >= len(file_data) - 1):
            end = True
        if not end:
            if (file_data[posY][posX + 1] == "#"):
                facing = "down"

    if facing == "down" and posY < len(file_data):
        if (file_data[posY + 1][posX] != "#"):
            if (checkedValue(posY + 1, posX)):
                count += 1
                checkedY.append(posY)
                checkedX.append(posX)
            posY += 1
            

        if (posY >= len(file_data) - 1):
            end = True
        if not end:
            if file_data[posY + 1][posX] == "#":
                facing = "left"

    if facing == "left" and posX > 0:
        if (file_data[posY][posX - 1] != "#"):
            if (checkedValue(posY, posX + 1)):
                count += 1
                checkedY.append(posY)
                checkedX.append(posX)
            posX -= 1
            
        if (posX <= 0):
            end = True
        if not end:
            if (file_data[posY][posX - 1] == "#"):
                facing = "up"
    
    
print(count)
