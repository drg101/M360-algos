import sys

def computeInverseH(a,b,r,p,prev2a,prev1a,prev2b,prev1b):
    qP = p // r
    rP = p % r

    m1 = prev2a - qP * prev1a
    m2 = prev2b - qP * prev1b
    print(f">>{p} = {qP} * {r} + {rP}")
    print(f"{rP} = {m1} * {a} + {m2} * {b}")
    
    if rP == 1:
        print(f"{m2} % {a}")
        return m2 % a

    return computeInverseH(a,b,rP,r,prev1a,m1,prev1b,m2)

#compute inverse of b % a(Find inverse of a when modding by b)
def computeInverse(a,b):
    if b > a:
        print("Error! a should be more than b!")
        print("Getting congruence class of b")
        print(f"b = {b} % {a}")
        b = b % a
        print(f"b is now {b}")
    
    q = a // b
    r = a % b

    print(f"{a} = 1 * {a} + 0 * {b}")
    print(f"{b} = 0 * {a} + 1 * {b}")
    print(f">>{a} = {q} * {b} + {r}")
    print(f"{r} = 1 * {a} - {q} * {b}")
    
    if r == 1: 
        print(f"{-q} % {a}")
        return (-q) % a
    return computeInverseH(a,b,r,b,0,1,1,-q)





    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " a b")
        quit()
    b = int(sys.argv[1])
    a = int(sys.argv[2])
    print(computeInverse(a,b))