import sys
from powmod import powMod

def zeroKnowledgeProof(y,b,z,n,x=None):
    if b == 0:
        return powMod(z,2,1,n) == y
    elif b == 1:
        return powMod(z,2,1,n) == (x * y) % n
