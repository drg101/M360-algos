import sys
import gcdE


#compute inverse of b % a(Find inverse of b when modding by a)
def computeInverse(a,b,log=False):
    if b == 0:
        return 0
    if b > a:
        if log:
            print("Error! a should be more than b!")
            print("Getting congruence class of b")
            print(f"b = {b} % {a}")
        b = b % a
        if log:
            print(f"b is now {b}")

    gcdVal, u, v = gcdE.gcdE(a,b,log)
    if log:
        print(f"GCD = {gcdVal}, u = {u}, v = {v}")

    if gcdVal == 1:
        inverse = v % a
        if log:
            print(f"Inverse = {v} % {a} = {inverse}")
            print(f"Inverse of {b} % {a} = {inverse}")
        return inverse
    else:
        if log:
            print(f"{b} % {a} has no inverse")
        return b


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " b a")
        quit()
    b = int(sys.argv[1])
    a = int(sys.argv[2])
    print(computeInverse(a,b,True))
    