import sys
import primitive
import allPrimitives
import getCycle
import powmod

def discreteLog(a,n,p):
    allPrim = allPrimitives.allPrimitives(p)
    if a in allPrim:
        print(f"{a} is a primitive element of {p}, getting cycle of {a} mod {p}")
        cycle = getCycle.getCycle(a,p)
        return cycle.index(n) + 1
    else:
        print("Using brute force approach!")
        for k in range(2,9999):
            if powmod.powMod(a,k,1,p) == n:
                return k

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " a n p")
        quit()
    print(discreteLog(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))