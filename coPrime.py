import sys
import gcd
from random import randint

def coPrime(p):
    while True:
        rand = randint(2, p - 1)
        if gcd.gcd(p,rand) == 1:
            return rand

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " p")
        quit()
    print(coPrime(int(sys.argv[1])))