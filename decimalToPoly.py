import sys
import bitsToPoly
import decimalToBinary

def decimalToPoly(decimal):
    return bitsToPoly.bitsToPoly(decimalToBinary.decimalToBinary(decimal))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " decimal")
        quit()
    print(decimalToPoly(int(sys.argv[1])))