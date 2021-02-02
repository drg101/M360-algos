import sys
import gcd

def lcm(a,b):
    gcdR = gcd.gcd(a,b)
    atb = (a*b)
    r = atb // gcdR
    print(f"a * b = {atb}")
    print("a * b / gcd = lcm")
    print(f"{atb} / {gcdR} = {r}")
    return r
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " a b")
        quit()
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(lcm(a,b))