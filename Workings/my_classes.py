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
"""
#puts the Instruction into the desired format
def iFormat(str):
    #replace
    strReplaceList = [("turn", ""), ("through", ""), (",", " ")] #replace useless strings
    for s in strReplaceList:
        str = str.replace(s[0], s[1])
    str = str.split() #turn it from string to list
    return str #this is now a list

i1 = "turn on 1,2 through 3,4"
i2 = "turn off 2,3 through 2, 3"
i3 = "switch 4,4 through 5,5"
i1 = iFormat(i1)
i2 = iFormat(i2)
i3 = iFormat(i3)
print("")
print("i1:", i1)
print("i2:", i2)
print("i3:", i3)

    
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

print("")
print("Valid Status 1:", iValid(i1))
print("Valid Status 2:", iValid(i2))
print("Valid Status 3:", iValid(i3))

#makes sure the integer values are within acceptable ranges
def iRange(iList, upperBound):
    for i in range(1, 5, 1):
        iList[i] = str(max(0, int(iList[i])))
        iList[i] = str(min(int(iList[i]), upperBound))
    return iList

print("")
print("Range Fix 1:", iRange(i1, lengthValue))
print("Range Fix 2:", iRange(i2, lengthValue))
print("Range Fix 3:", iRange(i3, lengthValue))


#makes sure that x1<=x2 and y1<=y2
def iOrder(iList):
    return (int(iList[1]) <= int(iList[3]) and int(iList[2]) <= int(iList[4]))

print("")
print("Order 1:", iOrder(i1))
print("Order 2:", iOrder(i2))
print("Order 3:", iOrder(i3))


def iMake(str, upperBound): #input string from file, upperBound from file as int
    iStatus = True
    while iStatus == True:
        iList = iFormat(str) #format string into list
        iStatus = iValid(iList) #check that the list has a valid form
        iList = iRange(iList, upperBound) #make sure that the range is within the bounds
        iStatus = iOrder(iList) #check that the range is well ordered
        return iList

