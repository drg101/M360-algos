import sys
from random import randint
import probalisticIsPrime

def generateBigPrime(digits=10,log=False):
    while True:
        test = random_with_N_digits(digits)
        if log: print(f"Trying n={test}")
        if probalisticIsPrime.probalisticIsPrime(test,log):
            return test

def random_with_N_digits(n): #https://stackoverflow.com/questions/2673385/how-to-generate-random-number-with-the-specific-length-in-python
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " digits")
        quit()
    print(generateBigPrime(int(sys.argv[1])))