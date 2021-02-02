import sys

#find greated common denom of a & b, euclids algo
def gcd(a,b):
    #print("gcd(" + str(a) + "," + str(b) + ")")
    print(f"{a} % {b} = {a%b}")
    if a % b == 0: #base
        print(f"GCD = {b}")
        return b
    else:
        return gcd(b, a % b)
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " a b")
        quit()
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(gcd(a,b))