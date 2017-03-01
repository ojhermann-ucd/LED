import Grid
import Instructions

def entryMod(theI, theBool):
    if theI.command == "on":
        return True
    if theI.command == "off":
        return False
    if theI.command == "switch":
        return not theBool