import sys
import euler

def ieuler(a):
    for i in range(1,100000):
        if euler.euler(i) == a:
            return i


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " a")
        quit()
    print(ieuler(int(sys.argv[1])))