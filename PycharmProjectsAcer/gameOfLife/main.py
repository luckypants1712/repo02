import random, time, copy
width = 50
height = 30
aliveChar = '#'
deadChar = ' '
# \\\\\\\\\\\\\\ create empty cells /////////////
cells = []
for y in range(height):
    row = []
    for x in range(width):
        row.append(deadChar)
    cells.append(row)

#\\\\\\\\ Life starting to form ////////////
cells[2][3] = aliveChar
cells[2][4] = aliveChar
cells[2][5] = aliveChar
cells[3][7] = aliveChar
cells[3][6] = aliveChar
cells[3][5] = aliveChar



for y in range(height):
    for x in range(width):
        print(cells[y][x],end='')
    print('')

liveNeighbour = 0

for y in range(height):
    for x in range(width):
        if x == 0:
            left = width - 1
        else:
            left = x - 1
        if x == width - 1:
            right = 0
        else:
            right= x + 1
        if y == 0:
            top = height -1
        else:
            top = y-1
        if y == height - 1
            down = 0
        else:
            down = y + 1

        liveNeighbour=0

        if cells[top][left]==aliveChar:
            liveNeighbour += 1
        if cells[top][right] == aliveChar:
            liveNeighbour += 1
        if cells[down][left]==aliveChar:
            liveNeighbour += 1
        if cells[down][right]==aliveChar:
            liveNeighbour += 1
        if cells[top][x]==aliveChar:
            liveNeighbour += 1
        if cells[down][x]==aliveChar:
            liveNeighbour += 1
        if cells[y][left]==aliveChar:
            liveNeighbour += 1
        if cells[y][right]==aliveChar:
            liveNeighbour += 1

        if liveNeighbour == 2 or liveNeighbour == 3:
