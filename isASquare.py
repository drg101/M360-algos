import sys 
from pFactor import pFactor
from isPrime import isPrime

#using legendre symbol
#0 iff p//a
#1 iff a is a nonzero square mod p
#-1 iff a is a nonsquare mod p

#a is int, p is prime
def isASquare(a,p,d=0,log=False):
    space = "  " * d
    if log: print(f"{space}({a}/{p})",end = " => ")
    if a == 0: 
        if log: print("0")
        return 0
    if a == 1: 
        if log: print(1)
        return 1
    if a == -1: 
        if log: print(-1)
        return (-1)**(p-1 // 2)
    if a == 2: 
        res = (-1)**((p**2 - 1) // 8)
        if log: print(res)
        return res
    if a >= p: 
        if log: print()
        return isASquare(a % p, p,d+1, log)
    if not(isPrime(a)): 
        print(f"factoring {a}")
        aFactored = pFactor(a)
        res = 1
        for factor in aFactored:
            for _ in range(aFactored[factor]):
                if log: print()
                res *= isASquare(int(factor),p,d+1, log)
        return res
    if log: print(f"* {((-1)**(((p-1)//2) * ((a-1)//2)))}")
    return isASquare(p,a,d+1,log) * ((-1)**(((p-1)//2) * ((a-1)//2)))
        
def verboseLegendreSquare(v):
    if v == 0:
        print("p//a")
    elif v == 1:
        print("a is square mod p")
    elif v == -1: 
        print("a is non-square mod p")

if __name__ == "__main__":
    if len(sys.argv) != 3:
            print("Usage: " + sys.argv[0] + " a p")
            quit()
    sol = isASquare(int(sys.argv[1]),int(sys.argv[2]),0,True)
    print(f"\n{sol}")
    verboseLegendreSquare(sol)