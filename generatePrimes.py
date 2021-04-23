import sys
import isPrime

def generatePrimes(n):
    return sieve(n)

def sieve(n):
    tab = [x for x in range(2,n+1)]
    safe = [0 for _ in range(2,n+1)]
    for i in range(len(tab)):
        if safe[i] == 0:
            for multiple in range(i+tab[i],len(safe),tab[i]):
                safe[multiple] = 1
    primes = []
    for i in range(len(safe)):
        if safe[i] == 0:
            primes.append(tab[i])
    return primes

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " a")
        quit()
    print(generatePrimes(int(sys.argv[1])))