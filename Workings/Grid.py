#creates the grid with initial values of False
class Grid: 

    #input requirements:
    # num s.t. int > 0
    
    #input: num=int
    #output: .rows = int; .columns = int; .grid = list of lists
    def __init__(self, num):
        self.rows = int(num)
        self.columns = int(num)
        self.grid = self.generateGrid()

    #input: n/a
    #output: list of lists
    def generateGrid(self):
        gridMult = self.rows + 1
        theGrid = [ [False]*gridMult for s in range(0, gridMult, 1) ]
        return theGrid

"""
aGrid = Grid(4).grid
print(aGrid)
"""