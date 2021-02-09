import sys
#found this on the internet

# There is no quick way to calculate the prime factors of a number.
# In fact, prime factorization is so famously hard that it's what puts the "asymmetric" in asymmetric RSA encryption.
# That being said, it can be sped up a little bit by using divisibility rules, like checking if the sum of the digits is divisible by 3.

def pFactor(num):
    ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149] # Primes from https://primes.utm.edu/lists/small/10000.txt. Primes can also be generated by iterating through numbers and checking for factors, or by using a probabilistic test like Rabin-Miller.
    pdict = {}
    for p in ps:
        if p <= num:
            while (num / p).is_integer():
                if str(p) in pdict:
                    pdict[str(p)] += 1
                else:
                    pdict[str(p)] = 1
                num /= p
        if num == 1: break
    return pdict

# Returns a dictionary in the form {"base": "exponent"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " a")
        quit()
    print(pFactor(int(sys.argv[1])))