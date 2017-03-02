# LED
comp30670 Assignment3

NOTE TO USER: this will assist you in using the program, but the best way to understand it is to follow the flow of contrl in my_led.py, reading the comments, and refer to other files as necessary.

README.md
LED/
  Workings/
    __init__.py
    my_classes.py
    my_led.py
  Tests/
    Test.py
  Setup.py

Summary
This program will use the data on a url, provided via a command line input, to calculate how many LEDs are on after all commands are executed.  The url is vetted, and then the data is formatted and evaluated line by line until all commands have been executed.

The implications of these commands are recorded by modifying boolean values stored in a matrix represented as a list of lists in Python.  The summation occurs by summing all the True values, which is then printed to the screen next to the url.

Below I will demonstrate the design by following the flow of control of the primary program; for details of the program, please review the code in my_led.py, as well as the comments.  Doing this will also allow you to better examine my_classes.py as it provides some context for why a class or function was developed.

Each file of code contains significant comments which a curious user will find helpful; for a detailed explanation of my program, one is expected to review the code and comments.  This document is merely an overview of the code and the process to develop it.

Components

README.md
LED/
  Workings/
    __init__.py
    my_classes.py
    my_led.py
  Tests/
    Test.py
  Setup.py

README.md
This contains some elements of this text to assist users of the program.

Workings
This program was expected to be activated by inputs to the command line.  I achieved this using ARGPARSE, which allowed me to quickly develop the user input into the following format:
python my_led.py --input url
e.g. python my_led.py --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt

While developing this program I had used a .txt input file to load the given urls, so I had created mutually exclusive groups to accommodate this additional means of input.  While I have not retained the functionality in my submission, I have left the mutually exclusive adder in the event someone would like to modify this program for alternative methods of input.

LINK is the section where the url is “cleaned” and checked to be valid; if it is not valid, a message is printed and the program is exited.

SIZE is where the the first line of the data, which should represent the size of each row and column of the matrix, is evaluated, formatted, and then retained to generate a matrix.  If the information relating the size of the matrix is invalid, a message is printed and the program exits.

THE ACTION is where the core of the program occurs: the matrix, represented by a list of lists, is generated and then manipulated as each line of the data on the url is formatted, evaluated, and acted on.  

OUTPUT is where the values of the matrix are summed and then printed to the screen, along with the url leading to the data.
Tests
The tests provided are run using nose.  For the submission I adhered to the requested range of 5 ~ 10 tests, though each component was also tested by bespoke methods while being made.  As is explained in Test.py, I chose to submit tests for atomic functions used in my program; if an atomic function doesn’t work, that has levered repercussion in higher-level functions utilising the atomic elements (by atomic, I mean they only rely on built-in Python methods and form the basis for larger, more complex elements of the program).

Though for purposes of clarity for the reviewers I haven’t included every test I conducted, I have at least indicated what my testing methodology was for each test e.g. enumerate the possible input errors and test for how the function accommodates them.

I have also structured the tests so that for a given test, new inputs can easily be added e.g. simple data structures and clear formatting.  I always found this a useful feature when testing my financial models at my old job, so employing it here seemed natural.  Also, using nose, it should be easy for other users to develop and implement new tests.
setup.py

This is a basic setup.py file; you can review it for details, but its simplicity reflects the requirements of this project.  It worked on my EC2 instance, as well as on a server hosted by Digital Ocean.  In both cases, I uninstalled and then reinstalled the file without issue.
