import sys

IRPT = {
    "4":   "111",
    "8":   "1101",
    "16":  "11001",
    "32":  "100101",
    "64":  "1100001",
    "128": "11000001",
    "256": "100011101",
    "512": "1000010001",
    "1024":"10000001001"
}

def baseToPoly(base):
    return IRPT[str(base)]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " base")
        quit()
    print(baseToPoly(int(sys.argv[1])))