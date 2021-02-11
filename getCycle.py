import sys
import powmod

def getCycle(pe,p):
    cycle = []
    for i in range(1,p):
        cycle.append(powmod.powMod(pe,i,1,p))
    return cycle

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " pe p")
        quit()

    print(getCycle(int(sys.argv[1]), int(sys.argv[2])))