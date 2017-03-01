#imports
import argparse
import my_classes
import sys

#argparse
parser = argparse.ArgumentParser()
parser.add_argument("source", help="a valid url")

group = parser.add_mutually_exclusive_group()
group.add_argument("-i", "--input", action="store_true")

args = parser.parse_args()

#link
theSource = CleanLink(args.source).clean
if not my_classes.validLink(theSource):
    print("That was not a valid url.")    

#size
theSource = urllib.request.urlopen(theSource)
theSize = 0
with theSource as theSrc:
    #clean
    theSrc = theSrc.readline().decode('utf-8')
    theSrc = sRemoveLeftWhiteSpace(theSrc)
    #checks
    if not sCheckSize(theSrc):
        print("There was more than one number input for size")
        sys.exit()
    if not sCheckInt(theSrc):
        print("Whatever was entered for size is not Python-integer friendly.")
        sys.exit()
    if not sCheckRange(theSrc):
        print("The integer entered for the size is not within the appropriate range [0, 10^9]")
        sys.exit()
    theSize = int(theSrc)

#xList and yList
xList = CoordinateList(theSize).list
yList = CoordinateList(theSize).list
count = 0
with theSource as theSrc:
    for line in theSrc:
        if count == 0:
            pass
        else:
            #make the instruction
            iList = my_classes.iMake(line)
            #xList manipulation
            xList = mMain(iList, xList, 'x')
            #yList manipulation
            yList = mMain(iList, yList, 'y')
        count += 1

#output
theSum = sum(xList) + sum(yList)
print(theSource, theSum)