import sys

def gcdEH(a,b,prev1,prev2,prev2a,prev1a,prev2b,prev1b):
    qP = prev2 // prev1
    rP = prev2 % prev1

    if rP == 0:
        print(f"{prev2} % {prev1} = 0")
        return prev1

    m1 = prev2a - qP * prev1a
    m2 = prev2b - qP * prev1b
    print(f">>{prev2} = {qP} * {prev1} + {rP}")
    print(f"{rP} = {m1} * {a} + {m2} * {b}")


    return gcdEH(a,b,rP,prev1,prev1a,m1,prev1b,m2)

#compute inverse of b % a(Find inverse of a when modding by b)
def gcdE(a,b):
    if b > a:
        tB = b
        b = a
        a = tB
    
    q = a // b
    r = a % b

    if r == 0:
        print(f"{a} % {b} = 0")
        return b

    print(f"{a} = 1 * {a} + 0 * {b}")
    print(f"{b} = 0 * {a} + 1 * {b}")
    print(f">>{a} = {q} * {b} + {r}")
    print(f"{r} = 1 * {a} - {q} * {b}")
    
    return gcdEH(a,b,r,b,0,1,1,-q)





    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " a b")
        quit()
    b = int(sys.argv[1])
    a = int(sys.argv[2])
    print(gcdE(a,b))