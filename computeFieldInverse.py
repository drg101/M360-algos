import sys
from polyMult import polyMult
from baseToPoly import baseToPoly

#brute force algo
def computeFieldInverse(base,a,log=False):
    poly = baseToPoly(base)
    for i in range(1,base):
        if polyMult(a,i,poly) == 1:
            return i
    return -1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " a base")
        quit()
    a = int(sys.argv[1])
    base = int(sys.argv[2])
    print(computeFieldInverse(base,a,True))