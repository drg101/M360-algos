import sys

def decimalToBinary(n):  
    return bin(n).replace("0b", "")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " decimalNumber")
        quit()
    print(decimalToBinary(int(sys.argv[1])))