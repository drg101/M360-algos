import sys
from powmod import powmod

def zeroKnowledgeProof(y,b,z,n,x=None):
    if b == 0:
        return powmod(z,2,n) == y
    elif b == 1:
        return powmod(z,2,n) == (x * y) % n
