import sys
import pFactor

def euler(p):
    factors = pFactor.pFactor(p)
    print(f"Factors: {factors}")
    ret = 1
    for fac in factors:
        ret *= primeEuler(int(fac), factors[fac])
    return ret

def primeEuler(p, k):
    return p**k - p**(k-1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " p")
        quit()
    print(euler(int(sys.argv[1])))