import sys
import euler

def inverseEuler(a,upTo=100000):
    for i in range(1,upTo):
        if euler.euler(i) == a:
            return i


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " a")
        quit()
    print(inverseEuler(int(sys.argv[1])))