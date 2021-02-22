import sys

def serialize(m):
    numStr = ""
    for char in m:
        numStr += str(ord(char) - 22)
    return int(numStr)

def deSerialize(num):
    numStr = str(num)
    ret = ''
    for i in range(0,len(numStr) - 1,2):
        step = numStr[i] + numStr[i+1]
        ret += chr(int(step) + 22)
    return ret

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " message")
        quit()
    m = sys.argv[1]
    s = serialize(m)
    d = deSerialize(s)

    print(f"Serialized '{m}' = {s}")
    print(f"de-Serialized {s} = '{d}'")