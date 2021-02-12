import sys

def isPrime(a):
    if a > 1:
        for i in range(2, a):  
            if (a % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " n")
        quit()
    print(isPrime(int(sys.argv[1])))