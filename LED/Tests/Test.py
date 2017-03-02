from nose.tools import *
from Workings.my_classes import *

"""
CONTENTS
#guide
#instructions
#links
size
"""


"""
GUIDE
#refer to my_classes for an explanation of each function being test
#each test is categorised by the related function area in my_class
#only atomic functions were tested
#complex functions could have been tested, but that would not have been efficient in the time available
#atomic functions are the material components of the complex functions anyway
#ADDING TESTS
##if you want to add to a test, please follow the convention of adding to the relevant data structure
## if you want to create a new test, please follow the convention of using data structures and iteration
"""


"""
INSTRUCTIONS
"""
def test_iFormat():
    #equality pair lists
    equalList = [
        ("turn on 1,2 through 3, 4", ['on', '1', '2', '3', '4']),
        ("turn off 1,2 through 3, 4", ['off', '1', '2', '3', '4']),
        ("switch 1,2 through 3, 4", ['switch', '1', '2', '3', '4']),
        ("",[]),
        ("apple", ['apple'])
        ]
    #test related pairs for equality
    for i in equalList:
        eq_(iFormat(i[0]), i[1])

def test_iValid():
    #valid lists
    trueList = [
        ['on', '1', '2','3','4'],
        ['off', '1', '2','3','4'],
        ['switch', '1', '2','3','4'],
                ]
    #bogus lists
    bogusList = [
        ['on', '1', '2','3','4', 'morethings'], #too long
        ['offf', '1', '2','3','4'], #bad command
        ['switch', '1', '2','3','tobyd'], #not an integer value
                ]
    for t in trueList:
        eq_(iValid(t), True)
    for b in bogusList:
        eq_(iValid(b), False)

def test_iRange():
    #input tests
    equalList = [
        ((['on', 1, 2, 3, 7], 5),['on', 1, 2, 3, 4]), #too big
        ((['on', 1, 16, 3, 7], 5),['on', 1, 4, 3, 4]), #too big
        ((['on', -1, 2, 3, 7], 5),['on', 0, 2, 3, 4]), #too small
        ]
    for e in equalList:
        eq_(iRange(e[0][0], e[0][1]), e[1])
            
def test_iOrder():
    #equal list
    equalList = [
        (['on', 1, 2, 1, 2], True),
        (['on', 1, 2, 0, 2], False),
        (['on', 1, 2, 3, -2], False),
        ]
    for e in equalList:
        eq_(iOrder(e[0]), e[1])    


"""
LINKS
"""
def test_validLink():
    #valid links
    validLinks = ["http://www.google.com", 
                  "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt", 
                  "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a_v2.txt", 
                  "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b_v2.txt",
                  "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt",
                  "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt"]
    #bogus links
    bogusLinks = ["a;lksdjfl;adjs",
                  "notalink",
                  "stuff is better than stuff"]
    #test valid links
    for link in validLinks:
        eq_(validLink(link), True)
    #test bogus links
    for link in bogusLinks:
        eq_(validLink(link), False)


"""
SIZE
"""
def test_sCheckSize():
    validLengths = [
        "asdfasfsad",
        "10",
        "100",
        "99999999999999999999",
        ]
    bogusLengths = [
        "1 0",
        "asdfasdf asdfasdf asdfasdf",
        "10923 1",
        ]
    for v in validLengths:
        eq_(sCheckSize(v), True)
    for b in bogusLengths:
        eq_(sCheckSize(b), False)
        
def test_sCheckInt():
    validEntries = [
        "1",
        "1999999999",
        "2000"
        ]
    bogusEntries = [
        "ted",
        "cruz",
        "goblin",
        "1.05",
        ]
    for v in validEntries:
        eq_(sCheckInt(v), True)
    for b in bogusEntries:
        eq_(sCheckInt(b), False)
        
def test_sCheckRange():
    validEntries = [
        "0",
        "1",
        "2000"
        ]
    bogusEntries = [
        "99999999999999999999999999999999999999999999",
        "-2",
        ]
    for v in validEntries:
        eq_(sCheckRange(v), True)
    for b in bogusEntries:
        eq_(sCheckRange(b), False)