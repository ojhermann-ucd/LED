#imports
import argparse
import my_classes
import sys
import urllib.request
from urllib.error import URLError, HTTPError

#argparse
parser = argparse.ArgumentParser()
parser.add_argument("source", help="a valid url")

group = parser.add_mutually_exclusive_group()
group.add_argument("-i", "--input", action="store_true")

args = parser.parse_args()

#link
theLink = my_classes.CleanLink(args.source).clean
if not my_classes.validLink(theLink):
    print("That was not a valid url.")    

#size
theSource = urllib.request.urlopen(theLink)
theSize = 0
with theSource as theSrc:
    #clean
    theSrc = theSrc.readline().decode('utf-8')
    #checks
    if not my_classes.sCheckSize(theSrc):
        print("There was more than one number input for size")
        sys.exit()
    if not my_classes.sCheckInt(theSrc):
        print("Whatever was entered for size is not Python-integer friendly.")
        sys.exit()
    if not my_classes.sCheckRange(theSrc):
        print("The integer entered for the size is not within the appropriate range [0, 10^9]")
        sys.exit()
    theSize = int(theSrc)

#xList and yList
#xList = my_classes.CoordinateList(theSize - 1).list
#yList = my_classes.CoordinateList(theSize - 1).list
theSum = 0
theCoordinates = [ [False]*theSize for r in range(0, theSize, 1)]
for line in urllib.request.urlopen(theLink):
    #clean
    theLine = str(line, 'utf-8')
    #make the instruction
    iList = my_classes.iMake(theLine, theSize)
    #variables
    theCommand = iList[0]
    x1 = iList[1]
    x2 = iList[3]
    y1 = iList[2]
    y2 = iList[4]
    xRange = range(x1, x2 + 1, 1)
    yRange = range(y1, y2 + 1, 1)
    for x in xRange:
        for y in yRange:
            if theCommand=='on':
                theCoordinates[x][y] = True
            elif theCommand=='off':
                theCoordinates[x][y] = False
            elif theCommand=='switch':
                theCoordinates[x][y] = not bool(theCoordinates[x][y])
            else:
                pass
    
    """
    #theSum
    theSum += my_classes.sSum(iList, xList, yList)
    """
    """
    #xList manipulation
    xList = my_classes.mMain(iList, xList, 'x')
    #yList manipulation
    yList = my_classes.mMain(iList, yList, 'y')    
    """
    
#output
output1 = my_classes.CleanLink(args.source).clean
for s in range(0, theSize, 1):
    theSum += sum(theCoordinates[s])
print(output1, theSum)