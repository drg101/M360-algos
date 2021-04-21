from powmod import powmod
from generateBigPrime import generateBigPrime
from primitive import primitive
from random import randint
from printNB import printmd

def runDiffie(digits=10):
    N = generateBigPrime(digits)
    printmd(f"Our {digits} digit psuedoprime, $N={N}$")
    G = primitive(N)
    printmd(f"Our primitive generator, $G={G}$")

    a = randint(2, N)
    printmd(f"Alice's private key, $a={a}$")
    b = randint(2, N)
    printmd(f"Bob's private key, $b={b}$")

    A = powmod(G,a,N)
    printmd(f"Alice's public key, $A\ =\ G^{{a}}\ mod \ N\ =\ {G}^{{{a}}}\ mod\ {N}\ =\ {A}$")
    B = powmod(G,b,N)
    printmd(f"Bob's public key, $B\ =\ G^{{b}}\ mod \ N\ =\ {G}^{{{b}}}\ mod\ {N}\ =\ {B}$")

    kA = powmod(A,b,N)
    printmd(f"Bob has received A={A} from Alice, and calculates $k_{{A}}\ =\ A^{{b}}\ mod\ N\ =\ {A}^{{{b}}}\ mod\ {N} = {kA}$")
    kB = powmod(B,a,N)
    printmd(f"Alice has received B={B} from Bob, and calculates $k_{{B}}\ =\ B^{{a}}\ mod\ N\ =\ {B}^{{{a}}}\ mod\ {N} = {kB}$")
    
    assert kA == kB, "Shared secret should be the same"
    printmd(f"Alice and Bob have now agreed on a shared secret of ${kA}$ without sharing their own secrets.")