from powmod import powmod
from generateBigPrime import generateBigPrime
from primitive import primitive
from random import randint

def runDiffie():
    N = generateBigPrime(10)
    G = primitive(N)

    a = randint(2, N)
    b = randint(2, N)

    A = powmod(G,a,N)
    B = powmod(G,b,N)

    kA = powmod(A,b,N)
    kB = powmod(B,a,N)
    print(kA)
    print(kB)