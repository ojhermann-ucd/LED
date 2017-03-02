#imports
import urllib.request
from urllib.error import URLError, HTTPError

"""
CONTENTS
#guide
#instructions
#manipulations
#links
#size
"""


"""
GUIDE
#the functions and classes are organised by their function in the overall process (see ReadMe file for overview)
#each function and class contains a single line description, input and output types, and line comments
#referencing the Read Me file should assist in providing context for each item below
#BEST PRACTICE: follow the flow of control of my_led and refer to this as needed
"""


"""
INSTRUCTIONS
"""
def iFormat(str):
#takes string from url and transforms it into a list of a desired format list
#input: str
#output: list
    #replace
    strReplaceList = [("turn", ""), ("through", ""), (",", " ")]
    for s in strReplaceList:
        str = str.replace(s[0], s[1])
    str = str.split()
    return str
    
def iValid(iList):
#determines if the result of iFormat is valid
#input: list
#output: boolean
    #test length is 5
    if len(iList) != 5:
        return False
    #test command is valid
    if iList[0] not in ["off", "on", "switch"]:
        return False
    #check valid integer entries
    for i in range(1, 5, 1):
        try:
            if not isinstance(int(iList[i]), int):
                return False
            else:
                iList[i] = int(iList[i]) #convert entry to integer
        except ValueError:
            return False
    return True

def iRange(iList, upperBound):
#makes sure the integer values are within acceptable ranges 0 and size of matrix minus one
#input: list, integer
#output: list
    for i in range(1, 5, 1):
        iList[i] = max(0, iList[i])
        iList[i] = min(iList[i], upperBound - 1)
    return iList

def iOrder(iList):
#makes sure that x1<=x2 and y1<=y2
#input: list
#output: boolean
    return (int(iList[1]) <= int(iList[3]) and int(iList[2]) <= int(iList[4]))

def iMake(str, upperBound):
#combines the Instruction functions into a single function
#input: str, int
#output: list
    iList = iFormat(str) #format string into list
    if not iValid(iList): #check that the list has a valid form
        return ['pass', False, False, False, False]
    iList = iRange(iList, upperBound) #make sure that the range is within the bounds
    if not iOrder(iList): #check that the range is well ordered
        return ['pass', False, False, False, False]
    return iList

class Instruc:
#turns lists into easier to use object for our purposes
#input: list
#output: list-like object useful for this exercise
    def __init__(self, iList):
        self.command = iList[0]
        self.x1 = iList[1]
        self.x2 = iList[3]
        self.y1 = iList[2]
        self.y2 = iList[4]
        self.xRange = range(self.x1, self.x2 + 1, 1)
        self.yRange = range(self.y1, self.y2 + 1, 1)


"""
MANIPULATIONS
"""
def mLED(xRange, yRange, theCoords, theCommand):
#donkey work of manipulating the LEDs; theCoords refers to matrix representing the LED structure
#input: Instruc.xRange, Instruc.yRange, list, Instruc.command
#output: list
    for x in xRange:
        for y in yRange:
            if theCommand=='on':
                theCoords[x][y] = True
            elif theCommand=='off':
                theCoords[x][y] = False
            elif theCommand=='switch':
                theCoords[x][y] = not bool(theCoords[x][y])
            else:
                pass
    return theCoords


"""
LINKS
"""
def validLink(strLink):
#checks if a link is valid
#input: str
#output: boolean
    try:
        theLink = urllib.request.urlopen(strLink)
        return True
    except ValueError:
        return False
    except HTTPError:
        return False
    except URLError:
        return False
    else:
        return False

class CleanLink:
#makes a clean link; done as a class in the event want to clean more extensively (not require for this assignment)
#input: str
#output: new object that is basically a polished str    
    def __init__(self, strLink):
        self.str = strLink
        self.clean = self.str.rstrip('\n')


"""
SIZE
"""   
#checks if length is one i.e. only one number was given
def sCheckSize(strInput): #str
    return (len(strInput.split()) == 1) #boolean output

#checks if the entry is an integer
def sCheckInt(strInput): #str
    try:
        return isinstance(int(strInput), int)
    except ValueError:
        return False

#checks the range
def sCheckRange(strInput): #str
    theInt = int(strInput)
    return (theInt > -1) and (theInt < 10**9)

def sChecks(strInput):
    return sCheckSize(strInput) and sCheckRange(strInput) and sCheckRange(strInput)