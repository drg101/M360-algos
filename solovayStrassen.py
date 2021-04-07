from isASquare import jacobi
from powmod import powmod
from random import randint
from coPrime import coPrime

def solovayStrassen(p,iter=5,log=True):
    for _ in range(iter):
        a = coPrime(p)
        if log: print(f"Using a={a}")
        powmodRes = powmod(a,(p-1)//2,p)
        if log: print(f"powmod res = {powmodRes}")
        jacobiRes = jacobi(a,p,0,False)
        if log: print(f"jacobi res = {jacobiRes}")
        resRound = powmodRes == jacobiRes % p
        if not(resRound):
            return False
    return True