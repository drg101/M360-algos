import sys
import bitsToPoly
from decimalToBinary import decimalToBinary
import decimalToPoly

def polyLongDiv(polyBitString1,polyBitString2,log=False):
    COMPUTESIZE = 25
    BANNER = "#" * COMPUTESIZE
    if log: print(f"{polyBitString1} / {polyBitString2} = ")
    res = polyBitString1
    if log: print(f"{BANNER}")
    while len(res) >= len(polyBitString2):
        if log: print(f"{res:>{COMPUTESIZE}}")
        addWith = polyBitString2 + ("0" * (len(res) - len(polyBitString2)))
        if log: print(f"{addWith:>{COMPUTESIZE}}")
        res = decimalToBinary(int(res,2) ^ int(addWith,2))
        if log: print(f"{res:>{COMPUTESIZE}}")
        if log: print(f"{BANNER}")
    return int(res,2)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " polyBitString1 polyBitString2")
        quit()
    print(polyLongDiv(sys.argv[1],sys.argv[2],True))