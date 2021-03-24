import sys
from polyMult import polyMult
from computeFieldInverse import computeFieldInverse
from baseToPoly import baseToPoly

def fieldDiv(a,b,base,log=False):
    inv = computeFieldInverse(base,b)
    if log: print(f"Doing {a} (x) {inv}")
    return polyMult(a,inv,baseToPoly(base),log)

if __name__ == "__main__":
    if len(sys.argv) != 4:
            print("Usage: " + sys.argv[0] + " a b base")
            quit()
    print(fieldDiv(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),True))