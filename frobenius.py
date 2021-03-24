import sys

def frobeniusPowers(base):
    powers = []
    i = 1
    while not(i == base):
        powers.append(i)
        i *= 2
    print(f"Frobenius pows of {base} are {powers}")
    return powers

def frobeniusMax(base):
    return frobeniusPowers(base)[-1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
            print("Usage: " + sys.argv[0] + " base")
            quit()
    print(frobeniusPowers(int(sys.argv[1])))