import sys
from polyMult import polyMult
from baseToPoly import baseToPoly
from polyPowmod import polyPowmod

#brute force algo
def computeFieldInverse(base,a,log=False):
    poly = baseToPoly(base)
    return polyPowmod(a,base-2,poly)
    return -1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " a base")
        quit()
    a = int(sys.argv[1])
    base = int(sys.argv[2])
    print(computeFieldInverse(base,a,True))