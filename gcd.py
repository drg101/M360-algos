import sys

#find greated common denom of a & b, euclids algo
def gcd(a,b):
    #print("gcd(" + str(a) + "," + str(b) + ")")
    if a % b == 0: #base
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