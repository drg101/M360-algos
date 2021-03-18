import sys
def binom(n,k):
    return facTo(n,n-k+1) // facTo(k)

def facTo(a,b=2):
    res = 1
    for i in range(a,b-1,-1):
        res *= i
    return res

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " n k")
        quit()
    print(binom(int(sys.argv[1]),int(sys.argv[2])))