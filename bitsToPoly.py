import sys
#turns a bitstring into a poly representation
def bitsToPoly(bitString):
    resString = ""
    polyIndex = len(bitString) - 1
    for i in range(0,len(bitString) - 1):
        if bitString[i] == "1": 
            resString += f"x^{polyIndex - i} + "
    if bitString[len(bitString) - 1] == "1":
        resString += "1"
    else:
        resString = resString[0:len(resString) - 3]
    
    if resString == "":
        resString = "0"
    return resString

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " bitString")
        quit()
    print(bitsToPoly(sys.argv[1]))