import sys
import generateBigPrime
import coPrime
import computeInverse
import powmod
import basicAlphabetSerializer

if __name__ == "__main__":
    p = 0
    q = 0
    messageToSend = ''
    if len(sys.argv) != 2:
        if len(sys.argv) != 4:
            print("Usage: " + sys.argv[0] + " message [p q]")
            quit()
        messageToSend = sys.argv[1]
        p = int(sys.argv[2])
        q = int(sys.argv[3])
    else:
        messageToSend = sys.argv[1]
        p = generateBigPrime.generateBigPrime(len(messageToSend) + 1)
        q = generateBigPrime.generateBigPrime(len(messageToSend) + 1)

    m = basicAlphabetSerializer.serialize(messageToSend)
    n = p*q
    k = (p - 1) * (q - 1) #phi N

    print(f"\nMessage to send = {messageToSend}")
    print(f"Serialized message = m = {m}")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n = p * q = {n}")
    print(f"k = phi(n) = (p - 1) * (q - 1) = {k}")
    print(f"Finding an e which gcd(e,k) = 1")
    e = coPrime.coPrime(k)
    print(f"e = {e}")
    print(f"Finding d, the inverse of e mod k")
    d = computeInverse.computeInverse(k,e)
    print(f"d = {d}")
    print(f"e * d (mod k) = {(e * d) % k}")

    print("\nNow the sender sets up message using public keys e and n")
    S = powmod.powMod(m,e,1,n)
    print(f"S = encrypted message = m^e mod n = {S}")
    
    print("\nNow the receiver (creator of the key pair) decrypts S")
    t = powmod.powMod(S,d,1,n)
    print(f"t = S^d mod n = (m^e)^n mod n = {t}")
    print(f"Receiver has received '{basicAlphabetSerializer.deSerialize(t)}'")
    
