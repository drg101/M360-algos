import sys
import fermatTest

def probalisticIsPrime(pTest,log=False): #work in progress, only doing a fermat test now
    return fermatTest.fermatTest(pTest)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " test")
        quit()
    print(probalisticIsPrime(int(sys.argv[1]),True))