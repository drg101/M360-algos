import sys
import powmod

def deCryptCipher(d,n,m):
    plain = powmod.powMod(m,d,1,n)
    retS = ""
    plain = str(plain)
    if(len(plain) % 2 != 0):
        plain = "0" + plain
    print(plain)
    for i in range(0,len(plain),2):
        retS += chr(int(plain[i] + plain[i + 1]) + ord("A") - 1)
    return retS
 
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " d n m")
        quit()
    
    print(deCryptCipher(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))