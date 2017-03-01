import urllib.request
from urllib.error import URLError, HTTPError
from venv import create

#input: str
#output: boolean
def validLink(strLink):
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
    
aLink = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
print(validLink(aLink))