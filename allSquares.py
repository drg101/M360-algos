import sys
from isASquare import isASquare, jacobi

def allSquares(base):
    print(f"Finding all squares in F{base}")
    return list(allSquaresAndRoots(base).keys())

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