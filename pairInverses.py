import sys
import computeInverse

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " a")
        quit()
    a = int(sys.argv[1])
    resT = []
    res = []
    for i in range(0, a):
        print()
        resT.append(i)
        res.append(computeInverse.computeInverse(a, i))
    print()
    print(resT)
    print(res)