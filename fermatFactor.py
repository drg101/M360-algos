import sys

def fermatFactor(n,iter=20,log=False):
    for y in range(1,iter+1):
        nSq = (n + y**2)**0.5
        if int(nSq) == nSq:
           if log: print(f"Found @y={y}, {int(nSq)}")
           f0 = int(nSq - y)
           f1 = int(nSq + y)
           fac = {}
           fac[str(f0)] = 1
           fac[str(f1)] = 1
           if log: print(f"Factors of {n} are {fac}")
           return fac

if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " n [iterations]")
        quit()
    if len(sys.argv) == 2:
        print(fermatFactor(int(sys.argv[1])))
    if len(sys.argv) == 3:
        print(fermatFactor(int(sys.argv[1]),int(sys.argv[2])))
