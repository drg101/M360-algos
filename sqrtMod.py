import sys
from primitive import fieldPrimitive
from getCycle import getFieldCycle
from computeInverse import computeInverse
from polyPowmod import polyPowmod
from baseToPoly import baseToPoly
from frobenius import frobeniusSqrt


def sqrtField(a,base):
    # qm1 = base - 1
    # print(f"Finding sqrt({a}) in F{base}")
    # primitive = fieldPrimitive(base)
    # print(f"Primitive element F{base} is {primitive}")
    # cycle = getFieldCycle(primitive,base)
    # print(f"Cycle F{base} is {cycle}")
    # k = cycle.index(a) + 1
    # print(f"k is {k}")
    # s = computeInverse(qm1,2) - 1
    # print(f"s is {s}")
    # res = polyPowmod(a,k*(s+1),1,baseToPoly(base),True)
    # print(f"Ans = (a^k)^(s+1) = {res}")
    #return res
    return polyPowmod(a,frobeniusSqrt(base),1,baseToPoly(base))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " a base")
        quit()
    print(sqrtField(int(sys.argv[1]),int(sys.argv[2])))