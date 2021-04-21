import sys
import primitive
import allPrimitives
import getCycle
from powmod import powmod
from printNB import printmd

def discreteLog(a,n,p):
    printmd(f"Finding $x$ for which ${a}^{{x}}={n}\ mod \ {p}$")
    allPrim = allPrimitives.allPrimitives(p)
    if a in allPrim:
        print(f"{a} is a primitive element of {p}, getting cycle of {a} mod {p}")
        # cycle = getCycle.getCycle(a,p)
        # return cycle.index(n) + 1
        return bsgs(a,n,p)
    else:
        print("Using brute force approach!")
        for k in range(2,99999):
            if powmod(a,k,p) == n:
                return k

from math import floor
from printNB import printTable, latexify, boldify, printex
from divMod import divMod
def bsgs(a,y,p):
    print("doing bsgs algo")
    B = []
    G = []
    iList = [1]
    n = floor((p-1)**0.5) + 1
    print(f"n={n}")
    B.append(a)
    aP = powmod(a,(-n - 1)%p,p)
    G.append(y*aP % p)
    for i in range(1,n):
        B.append(B[i-1]*a % p)
        G.append(G[i-1]*aP % p)
        iList.append(i+1)
    i = -1
    j = -1
    for b in B:
        if b in G:
            i = B.index(b) + 1
            j = G.index(b) + 1
    print(f"i={i}, j={j}")
    B[i-1] = boldify(B[i-1])
    G[j-1] = boldify(G[j-1])
    printTable({
        "i": iList,
        "B[i]": B,
        "G[i]": G
    })
    x = (i + n*j) % p
    assert powmod(a,x,p) == y
    printex(f"{a}^{{{x}}}={y}\ mod\ {p}")
    return x


    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " a n p")
        quit()
    print(discreteLog(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))