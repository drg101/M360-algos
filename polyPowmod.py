import sys
from polyMult import polyMult
from bitsToPoly import bitsToPoly

def polyPowmod(a,n,b,p,log=False):
    print(f"doing polyPowmod({a},{n},{b},{p})")
    if n == 1:
        print(f"Returning {a} * {b} mod ({bitsToPoly(p)})")
        return polyMult(a,b,p)
    if n % 2 == 0:
        return polyPowmod(polyMult(a,a,p),n//2,b,p,log)
    else:
        return polyPowmod(polyMult(a,a,p),n//2,polyMult(a,b,p),p,log)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " num1 num2 polyBitString")
        quit()
    polyPowmodRes = polyPowmod(int(sys.argv[1]),int(sys.argv[2]),1,sys.argv[3],True)
    print(f"polyPowmod = {polyPowmodRes}")
    res = 1
    for i in range(int(sys.argv[2])):
        res = polyMult(int(sys.argv[1]),res,sys.argv[3])
    print(f"Iterative = {res}")