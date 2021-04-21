from isASquare import jacobi
from powmod import powmod
from random import randint
from coPrime import coPrime
from eulerCriterion import eulerCriterion

def solovayStrassen(p,iter=5,log=True):
    if p < 1 or p % 2 == 0:
        return False
    if log: print(f"doing solovay strassen with {iter} iterations")
    for _ in range(iter):
        a = coPrime(p)
        if log: print(f"Using a={a}")
        powmodRes = eulerCriterion(a,p)
        if log: print(f"powmod res = {powmodRes}")
        jacobiRes = jacobi(a,p,0,False)
        if log: print(f"jacobi res = {jacobiRes}")
        resRound = powmodRes == jacobiRes % p
        if not(resRound):
            return False
    return True