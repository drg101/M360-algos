from isASquare import jacobi
from powmod import powmod
from random import randint
from pFactor import pFactor

# lets find an x for which x^2 = a mod p
def rootsModP(a,p):
    print(f"Finding roots mod P for a={a},p={p}")
    assert jacobi(a,p,0,False) == 1
    c = case(p)
    print(f"Case is {c}")
    assert c != -1
    if c == 1:
        return powmod(a,(p+1)//4,p)
    elif c == 2:
        z = powmod(a,(p-1)//4,p)
        if z == 1:
            return powmod(a,(p+3)//8,p)
        elif z == -1:
            return (powmod(4*a,(p-5)//8,p) * (2*a)) % p
        assert False
    elif c == 3:
        print("Doing tonelli shanks algo!")
        factors = pFactor(p-1)
        e = -1
        q = 1
        for fac in factors:
            if fac == "2":
                e = factors[fac]
            else:
                q *= int(fac)**factors[fac]

        assert p-1 == 2**e * q
        print(f"{p-1} = {2**e} * {q}")
        print(f"q={q}, e={e}")

        n = -1
        while(n == -1):
            ra = randint(2,p-1)
            if jacobi(ra,p,0,False) == -1:
                n = ra
        print(f"Found our nonsquare mod {p} to be n={n}")

        y = powmod(n,q,p)
        x = powmod(a,(q+1)//2,p)
        b = powmod(a,q,p)
        r = e
        while(True):
            assert a*b % p == powmod(x,2,p)
            assert powmod(y,powmod(2,r-1,p),p) == -1 % p
            assert powmod(b,powmod(2,r-1,p),p) == 1
            print(f"y={y}, x={x}, b={b}, r={r}")
            if b % p == 1:
                return x
            m = -1
            for i in range(1,r):
                if powmod(b,powmod(2,i,p),p) == 1:
                    m = i
                    break
            assert m <= r-1
            print(f"m={m}")
            yP = powmod(y,powmod(2,r-m,p),p)
            xP = x * powmod(y,powmod(2,r-m-1,p),p) % p
            bP = b * powmod(y,powmod(2,r-m,p),p) % p
            rP = m

            y = yP
            x = xP
            b = bP
            r = rP



        


def case(p):
    if p % 4 == 3:
        return 1
    elif p % 8 == 1:
        return 3
    elif p % 8 == 5:
        return 2
    return -1
        