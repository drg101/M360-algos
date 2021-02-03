import sys
import argparse

#find a^n % p
def powMod(a,n,b,p):
    print(f"\nn = {n}")
    if n == 1:
        print("n == 1, so:")
        print(f"ans = ({a} * {b}) % {p}")
        return (a*b) % p
    if n % 2 == 0: #if n is even
        print("n is even, so:")
        print(f"powMod({a}^2 % {p}, {n} / 2, {b}, {p})")
        print(f"= powMod({(a**2) % p}, {n//2}, {b}, {p})")
        return powMod((a**2) % p, n//2, b, p)
    else: #if n is odd
        print("n is odd, so:")
        print(f"powMod({a}^2 % {p}, ({n}-1) / 2, ({a} * {b}) % {p}, {p})")
        print(f"= powMod({(a**2) % p}, {n//2}, {(a*b) % p}, {p})")
        return powMod((a**2) % p, n//2, (a*b) % p, p)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " a n p, where a^n % p")
        quit()
    a = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    print(f"powMod({a}, {n}, 1, {p})")
    print(powMod(a,n,1,p))