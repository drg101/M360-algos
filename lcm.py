import sys
import gcd

def lcm(a,b):
    return (a*b) // gcd.gcd(a,b)
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " a b")
        quit()
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(lcm(a,b))