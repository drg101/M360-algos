import sys
import powmod
import gcd
from random import randint

def fermatTest(pTest,iter=5,log=False):
    if log: print(f"Doing fermat test with {iter} iterations")
    iterations = min(pTest - 1, iter)
    for i in range(2,iterations + 1):
        a = -1
        while a == -1:
            rand = randint(2, pTest - 1)
            if gcd.gcd(pTest, rand) == 1:
                a = rand
        if log:
            print(f"Testing with {a}")
        if isNotPrime(pTest,a):
            if log:
                print(f"{pTest} is not prime, because {a}^{pTest-1} != 1 mod {pTest}")
            return False
    return True

def isNotPrime(pTest, a, log=False): #not being prime does not necessarily imply it is prime
    powmodResult = powmod.powMod(a,pTest - 1,1,pTest)
    if log:
        print(f"{a}^{pTest-1} = {powmodResult} mod {pTest}")
    return powmod.powMod(a,pTest - 1,1,pTest) != 1

if __name__ == "__main__":
    iterate = 5
    if len(sys.argv) != 3:
        if len(sys.argv) != 2:
            print("Usage: " + sys.argv[0] + " test iterations")
            quit()
        print("Setting iterations to 5")
    else:
        iterate = int(sys.argv[2])  
    print(fermatTest(int(sys.argv[1]), iterate, True))