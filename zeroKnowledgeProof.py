import sys
from powmod import powmod

def zeroKnowledgeProof(y,b,z,n,x=None):
    if b == 0:
        return powmod(z,2,n) == y
    elif b == 1:
        return powmod(z,2,n) == (x * y) % n

if __name__ == "__main__":
    if len(sys.argv) != 6:
            print("Usage: " + sys.argv[0] + " y b z n x")
            quit()
    print(zeroKnowledgeProof(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])))
