import sys
import primitive
import getCycle
import zStarN

def allPrimitives(p):
    prim = primitive.primitive(p)
    cycle = getCycle.getCycle(prim, p)
    zStarn = zStarN.zStarN(p - 1)
    
    print(f"Cycle: {cycle}")
    print(f"ZstarN: {zStarn}")
    #now read off primitives 
    prims = []
    for i in zStarn:
        prims.append(cycle[i - 1])
    return prims

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " p")
        quit()
    print(allPrimitives(int(sys.argv[1])))