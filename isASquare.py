import sys 
from pFactor import pFactor
from isPrime import isPrime

#using legendre symbol
#0 iff p//a
#1 iff a is a nonzero square mod p
#-1 iff a is a nonsquare mod p

def legendre(a,p):
    return isASquare(a,p,0,True)

def jacobi(a,b,d=0,log=True):
    assert b % 2 != 0, f"b should be odd, but b was {b}"

    space = "  " * d
    if log: print(f"{space}({a}/{b})",end = " => ")
    d = d+1

    if a == 0:
        if log: print("2a = 0")
        return 0
    if a == 1:
        if log: print("2b = 1")
        return 1
    if a == -1:
        res = (-1)**((b-1)//2)
        if log: print(f"2c = {res}")
        return res
    if a == 2:
        res = (-1)**((b**2 - 1)//8)
        if log: print(f"2d = {res}")
        return res

    if a % 2 == 0 and b % 2 == 1:
        aFactored = pFactor(a)
        res = 1
        if log: print(f"1a {a} / 2")
        res *= jacobi(2,b,d,log)
        res *= jacobi(a//2,b,d,log)
        return res
        # if not(isPrime(b)):
        #     bFactored = pFactor(b)
        #     res = 1
        #     if log: print(f"1b factoring {b}")
        #     for factor in bFactored:
        #         for _ in range(bFactored[factor]):
        #             res *= jacobi(a,int(factor),d,log)
        #     return res

    if a >= b:
        if log: print(f"1c, doing a = {a} % {b}")
        return jacobi(a % b, b, d,log)

    if a % 2 == 1 and b % 2 == 1:   
        reciprocityMult = (-1)**(((a-1)//2)*((b-1)//2))
        if log: print(f"2e * {reciprocityMult}")
        return jacobi(b,a,d,log) * reciprocityMult


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