import sys
import fermatTest
import millerRabin
from solovayStrassen import solovayStrassen

def probalisticIsPrime(pTest,log=False): 
    return fermatTest.fermatTest(pTest,log) and millerRabin.millerRabin(pTest,log) and solovayStrassen(pTest,log)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " test")
        quit()
    print(probalisticIsPrime(int(sys.argv[1]),True))