#creates a set of instructions
class Instruction:

    #input requirements
    # list = [str, int, int, int, int]
    ## str = 'on', 'off', 'switch'
    
    #input: list
    #output: list or int
    def __init__(self, theList):
        self.instruction = theList
        self.command = theList[0]
        self.x1 = int(theList[1])
        self.y1 = int(theList[2])
        self.x2 = int(theList[3])
        self.y2 = int(theList[4])
        

aList = ['on', 1, 2, 3, 4]
anInstruction = Instruction(aList)
print(anInstruction.instruction)
print(anInstruction.command)
print(anInstruction.x1)
print(anInstruction.y1)
print(anInstruction.x2)
print(anInstruction.y2)