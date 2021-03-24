import sys
from trace import trace
from sqrtMod import sqrtField
from polyMult import polyMult
from fieldDiv import fieldDiv
from baseToPoly import baseToPoly
from polyPowmod import polyPowmod
from computeFieldInverse import computeFieldInverse

def quadraticEq(a,b,c,base):
    if a == 0 or c == 0:
        return None
    print(f"solving {a}x^2 + {b}x + {c} = 0 in F{base}")
    numSolutions = quadraticNumSolutions(a,b,c,base)
    print(f"There is {numSolutions} solutions.")
    if numSolutions == 0:
        print(f"Returning nothing")
        return None
    if numSolutions == 1:
        print(f"Returning sqrt(c/a)")
        return sqrtField(fieldDiv(c,a,base),base)
    elif numSolutions == 2:
        poly = baseToPoly(base)
        bOverA = fieldDiv(b,a,16)
        sx = f"({bOverA}y)"
        print(f"x = by/a = {sx}")
        print(f"{a}{sx}^2 + {b}{sx} + {c} = 0")
        print(f"{a}{sx}^2 + {b}{sx} = {c}")
        newA = polyPowmod(polyMult(a,bOverA,poly),2,1,poly)
        newB = polyMult(b,bOverA,poly)
        print(f"{newA}y^2 + {newB}y = {c}")
        if not(newA == newB):
            print("something went wrong")
            return None
        print(f"{newA}(y^2 + y) = {c}")
        yPlusY1 = fieldDiv(c,newA,base)
        print(f"y(y+1) = {c}/{newA} = {yPlusY1}")
        print(f"now to find a y * y+1 which = {yPlusY1}")
        ySol = -1
        for y in range(1,base):
            if polyMult(y,y+1,poly) == yPlusY1:
                ySol = y
                break
        print(f"Found y = {ySol}")
        print(f"Returning ({bOverA} * {y}) and ({bOverA} * {y+1})")
        solutions = (polyMult(bOverA,y,poly),polyMult(bOverA,y+1,poly))
        print(f"Solutions = {solutions}")
        return solutions


def quadraticNumSolutions(a,b,c,base):
    if b == 0:
        return 1
    print(f"Finding Tr(ac / b^2)")
    poly = baseToPoly(base)
    ac = polyMult(a,c,poly)
    print(f"ac = {ac}")
    #bSqr = polyMult(b,2,poly)
    bInv = computeFieldInverse(base,b)
    print(f"bInv = {bInv}")
    bInvSq = polyPowmod(bInv,2,1,poly)
    print(f"bInvSq = {bInvSq}")
    tr = trace(polyMult(ac,bInvSq,poly),base)
    print(f"Tr = {tr}")
    if(tr == 0):
        return 2
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 5:
            print("Usage: " + sys.argv[0] + " a b c base")
            quit()
    print(quadraticEq(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])))