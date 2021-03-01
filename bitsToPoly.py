import sys

def bitsToPoly(bitString):
    #1001
    resString = ""
    polyIndex = len(bitString) - 1
    for bit in range(0,len(bitString) - 1):
        if bit == "1": 
            resString += f"x^{polyIndex} + "
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " bitString")
        quit()
    print(bitsToPoly(int(sys.argv[1])))