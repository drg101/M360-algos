def crt(p,q,complex=False):
    tab = [ [ -1 for _ in range(q) ] for _ in range(p) ]
    #we now have table with p rows and q cols
    if not(complex):
        for i in range(p*q):
            tab[i%p][i%q] = i
    else:
        for pi in range(p):
            for qi in range(q):
                tab[pi][qi] = crtProblem(pi,qi,p,q)
    return tab

def crtJacobi(p,q):
    from isASquare import jacobi
    tab = [ [ -1 for _ in range(q) ] for _ in range(p) ]
    #we now have table with p rows and q cols
    for a in range(p*q):
        tab[a%p][a%q] = jacobi(a,p*q,0,False)
    return tab

from computeInverse import computeInverse
def crtProblem(a,b,p,q):
    # find an x so that
    # x cong a mod p
    # x cong b q
    #6 + k * 13 = x
    #a + k * p 
    #a + k * p cong b mod q
    z = (b - a)
    #k * p cong z mod q
    zDivP = z * computeInverse(q,p)
    #k cong zDivP mod q
    k = zDivP % q
    return (a + k * p) % (p*q)
