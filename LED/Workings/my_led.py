#imports
import argparse
import sys
import urllib.request
from urllib.error import URLError, HTTPError
import my_classes

"""
OVERVIEW
#ARGPARSE: establishes the user interface
#LINK: identifies and tests for a valid link provided by the user
#SIZE: uses the valid link to identify, test, and then define the size of the matrix
#THE ACTION: iterates over the contents of the file at the link and modifies a matrix representing LED status
#OUTPUT: prints the link and number of on LEDs
"""

#ARGPARSE
#keep things short
parser = argparse.ArgumentParser()
#set up the argument and help hint
parser.add_argument("source", help="a valid url")
#great a group (other versions may have different inputs e.g. text file like I had played with before)
group = parser.add_mutually_exclusive_group()
group.add_argument("-i", "--input", action="store_true")
#keep things short
args = parser.parse_args()

#LINK
#clean the link
theLink = my_classes.CleanLink(args.source).clean
#test and exit on fail
if not my_classes.validLink(theLink):
    print("That was not a valid url.")
    sys.exit()   

#SIZE
#open the the link
theSource = urllib.request.urlopen(theLink)
#initialise variable representing the size of the matrix to zero
theSize = 0
#open the link
with theSource as theSrc:
    #obtain and clean the value representing the size of the matrix
    theSrc = theSrc.readline().decode('utf-8')
    #run the relevant checks and exit on failure; done as a single check because precise error detection was not requested or required
    if not my_classes.sChecks(theSrc):
        print("There is something wrong with the input provided for the size of the LED grid.")
        print("Check if: there is more than one number, the value entered is not Python-integer friendly, or if it's out of the range [0, 10^9]")
        sys.exit()
    else:
        #on success the size of the matrix is set
        theSize = int(theSrc)

#THE ACTION
#initialise the sum of all on LEDs to zero
theSum = 0
#generate a matrix for storing LED status
theCoordinates = [ [False]*theSize for r in range(0, theSize, 1)]
#iterate over the source, line by line, creating and dumping data as required
for line in urllib.request.urlopen(theLink):
    #clean the line
    theLine = str(line, 'utf-8')
    #make the instruction
    iList = my_classes.iMake(theLine, theSize)
    iInstruc = my_classes.Instruc(iList)
    #manipulate the matrix tracking the status of the LEDs
    theCoordinates = my_classes.mLED(iInstruc.xRange, iInstruc.yRange, theCoordinates, iInstruc.command)

#OUTPUT
#sum all rows of the matrix to see how many LEDs are on
for s in range(0, theSize, 1):
    theSum += sum(theCoordinates[s])
#print the source and sum
print(my_classes.CleanLink(args.source).clean, theSum)