"""
Calculates the greatest common divisor between two very large numbers. 
This is used in Cryptography.
"""

# Iterates over all numbers in the length of the sum of both numbers
def naiveGCD(a,b):
    best = 0
    for d in range(1, a+b):
        if a % d == 0 and  b % d == 0:
            best = d
    return best


# print(naiveGCD(36,12))

# Implements the Euclidean Algorithm
def gcd(a,b):
    if b == 0:
        return a
    aPrime = a % b
    return gcd(b, aPrime)

print(gcd(357, 234))


