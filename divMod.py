from computeInverse import computeInverse

def divMod(a,b,p,log=False):
    invB = computeInverse(p,b)
    return (a * invB) % p