import Grid
import Instructions

def modify(grid, instruc):
    for x in range(instruc.x1, instruc.x2 + 1, 1):
        for y in range(instruc.y1, instruc.y2 + 1, 1):
            if instruc.command == "on":
                grid[x][y] = True
            elif instruc.command == "off":
                grid[x][y] = False
            else:
                grid[x][y] = not bool(grid[x][y])
    return grid


theGrid = Grid.Grid(3).grid
theGrid2 = theGrid
print(theGrid)
print(theGrid2)

aList = ['on', 0, 1, 1, 2]
aInstruc = Instructions.Instruction(aList)
print(aInstruc.instruction)

for x in range(aInstruc.x1, aInstruc.x2 + 1, 1):
    for y in range(aInstruc.y1, aInstruc.y2 + 1, 1):
        if aInstruc.command == "on":
            theGrid[x][y] = True
        elif aInstruc.command == "off":
            theGrid[x][y] = False
        else:
            theGrid[x][y] = not theGrid[x][y]
print(theGrid)

print(modify(theGrid2, aInstruc))