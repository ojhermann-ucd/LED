"""
CONTENTS
#coordinates
#instructions
#manipulations
"""


"""
COORDINATES
"""
#make the coordinate lists: xList and yList
class CoordinateList: 
    def __init__(self, intNum):
        self.length = intNum
        self.list = [False] * (intNum + 1)

lengthValue = 5
xList = CoordinateList(lengthValue).list
yList = CoordinateList(lengthValue).list
print("xList:", xList)
print("yList:", yList)


"""
INSTRUCTIONS
# a few formatting and test functions are combined into a single function
"""
#puts the Instruction into the desired format
def iFormat(str):
    #replace
    strReplaceList = [("turn", ""), ("through", ""), (",", " ")] #replace useless strings
    for s in strReplaceList:
        str = str.replace(s[0], s[1])
    str = str.split() #turn it from string to list
    return str #this is now a list
    
#determines if the Instruction is valid
def iValid(iList):
    if len(iList) != 5: #all valid Instructions are of length 5
        return False
    if iList[0] not in ["off", "on", "switch"]: #all valid instructions begin with one of these Commands
        return False
    for i in range(1, 5, 1): # all valid instructions have four integer inputs
        try:
            if not isinstance(int(iList[i]), int):
                return False
        except ValueError:
            return False
    return True

#makes sure the integer values are within acceptable ranges
def iRange(iList, upperBound):
    for i in range(1, 5, 1):
        iList[i] = str(max(0, int(iList[i])))
        iList[i] = str(min(int(iList[i]), upperBound))
    return iList

#makes sure that x1<=x2 and y1<=y2
def iOrder(iList):
    return (int(iList[1]) <= int(iList[3]) and int(iList[2]) <= int(iList[4]))

#changes numbers into int
def iInt(iList):
    for i in range(1, 5, 1):
        iList[i] = int(iList[i])
    return iList

#combines the Instruction functions into a single function
def iMake(str, upperBound): #input string from file, upperBound from file as int
    iStatus = True
    while iStatus == True:
        iList = iFormat(str) #format string into list
        iStatus = iValid(iList) #check that the list has a valid form
        iList = iRange(iList, upperBound) #make sure that the range is within the bounds
        iStatus = iOrder(iList) #check that the range is well ordered
        iList = iInt(iList) #convert numbers into int
        break
    if iStatus == True:
        return iList
    else:
        return ['pass', False, False, False, False]
    
made1 = "turn on 1,2 through 3,4"
made2 = "turn off 2,3 through 2, 3"
made3 = "switch 4,4 through 5,5"

made1 = iMake(made1, lengthValue)
made2 = iMake(made2, lengthValue)
made3 = iMake(made3, lengthValue)

print("")
print(made1)
print(made2)
print(made3)


"""
MANIPULATIONS
"""
#generates the ranges for manipulation
def mRange(iList, mAxis): #list, str
    if mAxis == 'x':
        mOutput = range(iList[1], iList[3] + 1, 1)
    else:
        mOutput = range(iList[2], iList[4] + 1, 1)
    return mOutput

#converts a given boolean value to another boolean value
def mCommand(iCommand, iBool): #str, bool
    if iCommand == "on":
        iBool = True
    elif iCommand == "off":
        iBool = False
    else:
        iBool = not bool(iBool)

#manipulates the boolean values of xList and yList given information in iList
def mMain(iList, xList, yList): #list, list, list
    #ranges
    xRange = mRange(iList, 'x')
    yRange = mRange(iList, 'y')
    #manipulate booleans
    iCommand = iList[0]
    for x in xRange:
        xList[x] = mCommand(iCommand, xList[x])
    for y in yRange:
        yList[y] = mCommand(iCommand, yList[y])