import sys
import pFactor
import powmod
from polyPowmod import polyPowmod

def primitive(p,log=False):
    if log: print(f"-- primitive({p}) --")
    pm1 = p - 1
    factors = pFactor.pFactor(pm1)
    print(f"Factors: {factors}")
    for a in range(2,pm1):
        if log: print(f"Trying a = {a}")
        flag = False
        for fac in factors:
            if log: print(f"Testing against factor {fac}")
            pwmd = powmod.powMod(a, pm1 / int(fac), 1, p)
            if(pwmd == 1):
                if log: print(f"powMod({a}, {pm1} / {fac}, 1, {p}) == 1, getting new a\n")
                flag = True
                break
            else:
                if log: print(f"powMod({a}, {pm1} / {fac}, 1, {p}) != 1")
        if flag == False:
            if log: print(f"Primitive element = {a}")
            return a

from baseToPoly import baseToPoly
def fieldPrimitive(base):
    poly = baseToPoly(base)
    print(f"-- primitive(F{base}) --")
    bm1 = base - 1
    factors = pFactor.pFactor(bm1)
    print(f"Factors: {factors}")
    for a in range(2,bm1):
        print(f"Trying a = {a}")
        flag = False
        for fac in factors:
            print(f"Testing against factor {fac}")
            pwmd = polyPowmod(a, bm1 / int(fac), 1, poly)
            if(pwmd == 1):
                print(f"polyPowmod({a}, {bm1} / {fac}, 1, {poly}) == 1, getting new a\n")
                flag = True
                break
            else:
                print(f"polyPowmod({a}, {bm1} / {fac}, 1, {poly}) != 1")
        if flag == False:
            print(f"Primitive element = {a}")
            return a



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " p")
        quit()
    print(primitive(int(sys.argv[1]),True))
    