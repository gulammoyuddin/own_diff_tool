import sys
from LCS import get_diff


oldfile = sys.argv[1]
newfile = sys.argv[2]

oldData = []
newData = []

try:
    with open(oldfile) as file:
        oldData = file.readlines()
    with open(newfile) as file:
        newData = file.readlines()
except IOError:
    print("Error In Opening file", IOError)

diff = get_diff(oldData,newData)

for s in diff:
    print(s)