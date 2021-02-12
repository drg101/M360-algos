import sys
import gcd

def zStarN(n):
    ret = set()
    for i in range(1,n):
        if gcd.gcd(i,n) == 1:
            ret.add(i)
    return ret


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " n")
        quit()
    print(zStarN(int(sys.argv[1])))