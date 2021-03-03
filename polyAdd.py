import sys
import bitsToPoly
import decimalToBinary
import decimalToPoly
import bitsXOR
import polyLongDiv

def polyAdd(num1,num2,polyBitString,log=False):
    COMPUTESIZE = 25
    BANNER = "#" * COMPUTESIZE
    if log: print(f"Finding {num1} + {num2} mod ({bitsToPoly.bitsToPoly(polyBitString)})")
    bits1 = decimalToBinary.decimalToBinary(num1)
    bits2 = decimalToBinary.decimalToBinary(num2)
    if log: print(f"{num1} + {num2} = ")
    if log: print(f"{bits1} + {bits2} = ")
    numAddRes = bitsXOR.bitsXOR(bits1,bits2)
    if log: print(f"{numAddRes:>{COMPUTESIZE}}\n")

    return polyLongDiv.polyLongDiv(numAddRes,polyBitString,log)



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " num1 num2 polyBitString")
        quit()
    print(polyAdd(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],True))