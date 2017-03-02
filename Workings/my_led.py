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

#the action
theSum = 0
theCoordinates = [ [False]*theSize for r in range(0, theSize, 1)]
for line in urllib.request.urlopen(theLink):
    #clean
    theLine = str(line, 'utf-8')
    #make the instruction
    iList = my_classes.iMake(theLine, theSize)
    iInstruc = my_classes.Instruc(iList)
    #the manipulation
    theCoordinates = my_classes.mLED(iInstruc.xRange, iInstruc.yRange, theCoordinates, iInstruc.command)

#output
output1 = my_classes.CleanLink(args.source).clean
for s in range(0, theSize, 1):
    theSum += sum(theCoordinates[s])
print(output1, theSum)