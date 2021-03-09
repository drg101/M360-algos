import sys
import bitsToPoly
import decimalToBinary
import decimalToPoly
import polyLongDiv

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
        numMultRes = decimalToBinary.decimalToBinary(int(numMultRes,2) ^ int(bits,2))
    if log: print(f"{numMultRes:>{COMPUTESIZE}}\n")

    return polyLongDiv.polyLongDiv(numMultRes,polyBitString,log)



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " num1 num2 polyBitString")
        quit()
    print(polyMult(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],True))