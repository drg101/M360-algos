import sys
import bitsToPoly
from decimalToBinary import decimalToBinary
import decimalToPoly
import polyLongDiv

def polyAdd(num1,num2,polyBitString,log=False):
    COMPUTESIZE = 25
    BANNER = "#" * COMPUTESIZE
    if log: print(f"Finding {num1} + {num2} mod ({bitsToPoly.bitsToPoly(polyBitString)})")
    bits1 = decimalToBinary(num1)
    bits2 = decimalToBinary(num2)
    if log: print(f"{num1} + {num2} = ")
    if log: print(f"{bits1} + {bits2} = ")
    numAddRes = decimalToBinary(int(bits1,2)^int(bits2,2))
    if log: print(f"{numAddRes:>{COMPUTESIZE}}\n")

    return polyLongDiv.polyLongDiv(numAddRes,polyBitString,log)



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " num1 num2 polyBitString")
        quit()
    print(polyAdd(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],True))