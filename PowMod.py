import sys

#find a^n % p
def powMod(a,n,b,p):
    if n == 1:
        return (a*b) % p
    if n % 2 == 0: #if n is even
        return powMod((a**2) % p, n/2, b, p)
    else: #if n is odd
        return powMod((a**2) % p, n//2, (a*b) % p, p)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " a n p, where a^n % p")
        quit()
    a = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    print(powMod(a,n,1,p))