import sys
import pFactor
import powmod

def primitive(p):
    print(f"-- primitive({p}) --")
    pm1 = p - 1
    factors = pFactor.pFactor(pm1)
    for a in range(2,pm1):
        print(f"Trying a = {a}")
        flag = False
        for fac in factors:
            print(f"\nTesting against factor {fac}")
            print(f"////////////powMod({a}, {pm1} / {fac}, 1, {p}):////////////")
            pwmd = powmod.powMod(a, pm1 / int(fac), 1, p)
            print("///////////////////////////////\n")
            if(pwmd == 1):
                print(f"powMod({a}, {pm1} / {fac}, 1, {p}) == 1, getting new a")
                flag = True
                break
            else:
                print(f"powMod({a}, {pm1} / {fac}, 1, {p}) != 1")
        if flag == False:
            print(f"Primitive element = {a}")
            return a



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " p")
        quit()
    print(primitive(int(sys.argv[1])))
    