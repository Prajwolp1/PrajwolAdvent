def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("input.txt")

grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

total = 0
for j in range(len(grid)):
    for i in range(len(grid[j])):
        if (grid[j][i] == "X"):
            if (i + 3 < len(grid[j]) and grid[j][i + 1] == "M" and grid[j][i + 2] == "A" and grid[j][i + 3] == "S"):
                total += 1
            
            if (i - 3 >= 0 and grid[j][i - 1] == "M" and grid[j][i - 2] == "A" and grid[j][i - 3] == "S"):
                total += 1
                
            if (j + 3 < len(grid) and grid[j + 1][i] == "M" and grid[j + 2][i] == "A" and grid[j + 3][i] == "S"):
                total += 1
                
            if (j - 3 >= 0 and grid[j - 1][i] == "M" and grid[j - 2][i] == "A" and grid[j - 3][i] == "S"):
                total += 1
            
            if (i + 3 < len(grid[j]) and j + 3 < len(grid) and grid[j + 1][i + 1] == "M" and grid[j + 2][i + 2] == "A" and grid[j + 3][i + 3] == "S"):
                total += 1
            
            if (i + 3 < len(grid[j]) and j - 3 >= 0 and grid[j - 1][i + 1] == "M" and grid[j - 2][i + 2] == "A" and grid[j - 3][i + 3] == "S"):
                total += 1
            
            if (i - 3 >= 0 and j - 3 >= 0 and grid[j - 1][i - 1] == "M" and grid[j - 2][i - 2] == "A" and grid[j - 3][i - 3] == "S"):
                total += 1
            
            if (i - 3 >= 0 and j + 3 < len(grid) and grid[j + 1][i - 1] == "M" and grid[j + 2][i - 2] == "A" and grid[j + 3][i - 3] == "S"):
                total += 1
print(total)