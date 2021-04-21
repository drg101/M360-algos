import sys
import powmod
import pFactor
import coPrime

#true = inconclusive
#false = not a prime
def millerRabin(n,iter=5,log=False):
    if log: print(f"Doing miller rabin with {iter} iterations")
    if n <= 2:
        return True
    factors = pFactor.pFactor(n - 1)
    s = -1
    m = 1
    for fac in factors:
        if fac == "2":
            s = factors[fac]
        else:
            m *= int(fac)**factors[fac]
    for z in range(iter):
        a = coPrime.coPrime(n)
        if log: print(f"trying a={a}")
        bNaught = powmod.powMod(a,m,1,n)
        if bNaught == 1 or bNaught == -1 % n:
             continue
        for i in range(s):
            bPlus1 = powmod.powMod(bNaught,2,1,n)
            if bPlus1 == -1 % n:
                break
            if bPlus1 == 1:
                return False
            bNaught = bPlus1
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " a")
        quit()
    print(millerRabin(int(sys.argv[1])))