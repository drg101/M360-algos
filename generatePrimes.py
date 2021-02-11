#from internet
import sys

def generatePrimes(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)

    return primes


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " a")
        quit()
    print(generatePrimes(int(sys.argv[1])))