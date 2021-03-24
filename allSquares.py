import sys
from isASquare import isASquare

def allSquares(base):
    print(f"Finding all squares in F{base}")
    squares = []
    for i in range(base//2):
        if isASquare(i,base) == 1:
            squares.append(i)
            if i:
                squares.append(base - i)
    return squares

def allSquaresAndRoots(base):
    print(f"Finding all squares and their roots in F{base}")
    squaresAndRoots = {}
    for i in range(base):
        square = i*i % base
        if not(square in squaresAndRoots):
            squaresAndRoots[square] = [i]
        else:
            squaresAndRoots[square].append(i)
    return squaresAndRoots

if __name__ == "__main__":
    if len(sys.argv) != 2:
            print("Usage: " + sys.argv[0] + " base")
            quit()
    print(allSquares(int(sys.argv[1])))
    print(allSquaresAndRoots(int(sys.argv[1])))