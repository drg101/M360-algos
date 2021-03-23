import sys
from frobenius import frobeniusPowers
from polyPowmod import polyPowmod
from baseToPoly import baseToPoly
from polyAdd import polyAdd

def trace(a,base):
    print(f"Tr({a}) in F{base}")
    poly = baseToPoly(base)
    powers = frobeniusPowers(base)
    res = 0
    for power in powers:
        print(f"{a}^(x){power} (+) ", end = '')
        res = polyAdd(res,polyPowmod(a,power,1,poly),poly)
    print(f"= {res}")
    return res

if __name__ == "__main__":
    if len(sys.argv) != 3:
            print("Usage: " + sys.argv[0] + " a base")
            quit()
    print(trace(int(sys.argv[1]),int(sys.argv[2])))