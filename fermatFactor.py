import sys

def fermatFactor(n,iter=20):
    for y in range(1,iter+1):
        nSq = (n + y**2)**0.5
        if int(nSq) == nSq:
           print(f"Found @y={y}, int(nSq)")
           f0 = int(nSq - y)
           f1 = int(nSq + y)
           fac = {}
           fac[str(f0)] = 1
           fac[str(f1)] = 1
           print(f"Factors of {n} are {fac}")
           return fac

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " test")
        quit()
    print(fermatFactor(int(sys.argv[1])))
