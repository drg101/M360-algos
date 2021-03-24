import sys
from isPrime import isPrime
from pFactor import pFactor


def characteristic(base):
    if isPrime(base):
        return base
    factors = pFactor(base)
    if len(factors) != 1:
        return None
    return int(next(iter(factors)))

if __name__ == "__main__":
    if len(sys.argv) != 2:
            print("Usage: " + sys.argv[0] + " base")
            quit()
    print(characteristic(int(sys.argv[1])))