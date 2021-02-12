import sys
import isPrime

def generatePrimes(n):
    primes = []
    for i in range(2, n + 1):
        if isPrime.isPrime(i):
            primes.append(i)

    return primes


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " a")
        quit()
    print(generatePrimes(int(sys.argv[1])))