import sys
import bitsToPoly
import decimalToBinary
import decimalToPoly
import bitsXOR

def polyMult(num1,num2,polyBitString,log=False):
    COMPUTESIZE = 25
    BANNER = "#" * COMPUTESIZE
    if log: print(f"Finding {num1} * {num2} mod ({bitsToPoly.bitsToPoly(polyBitString)})")
    bits1 = decimalToBinary.decimalToBinary(num1)
    bits2 = decimalToBinary.decimalToBinary(num2)
    if log: print(f"{num1} * {num2} = ")
    if log: print(f"{bits1} * {bits2} = ")
    if log: print(f"{BANNER}")
    addUp = []
    for i in range(len(bits2)):
        if bits2[i] == "1":
            toAdd = bits1 + ("0" * (len(bits2) - i - 1))
            if log: print(f"{toAdd:>{COMPUTESIZE}}")
            addUp.append(toAdd)
    if log: print(f"{BANNER}")
    numMultRes = "0"
    for bits in addUp:
        numMultRes = bitsXOR.bitsXOR(numMultRes,bits)
    if log: print(f"{numMultRes:>{COMPUTESIZE}}\n")

    if log: print(f"{numMultRes} / {polyBitString} = ")
    res = numMultRes
    if log: print(f"{BANNER}")
    while int(res,2) > int(polyBitString,2):
        if log: print(f"{res:>{COMPUTESIZE}}")
        addWith = polyBitString + ("0" * (len(res) - len(polyBitString)))
        if log: print(f"{addWith:>{COMPUTESIZE}}")
        res = bitsXOR.bitsXOR(res,addWith)
        print(f"{res:>{COMPUTESIZE}}")
        if log: print(f"{BANNER}")
    return int(res,2)



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " num1 num2 polyBitString")
        quit()
    print(polyMult(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],True))