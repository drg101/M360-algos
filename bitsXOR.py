import sys

def bitsXOR(bits1,bits2):  
    resS = ""
    addToFront = ""
    minSize = -1
    if len(bits1) < len(bits2):
        minSize = len(bits1)
        addToFront = bits2[0:len(bits2) - len(bits1)]
    else:
        minSize = len(bits2)
        addToFront = bits1[0:len(bits1) - len(bits2)]
    #print(minSize)
    for i in range(minSize):
        #print(f"{bits1[len(bits1) - i - 1]} vs {bits2[len(bits2) - i - 1]}")
        resS = ("0" if bits1[len(bits1) - i - 1] == bits2[len(bits2) - i - 1] else "1") + resS
    resS = addToFront + resS
    resS = resS.lstrip("0")
    return resS

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " bitString1 bitString2")
        quit()
    print(bitsXOR(sys.argv[1],sys.argv[2]))