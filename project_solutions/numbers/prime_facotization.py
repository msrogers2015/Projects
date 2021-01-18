import math as m
factors = []
primes = []

def isprime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


try:
    digit = int(input('Pick a number:'))
except ValueError:
    print('PLease input a numerical value.')

root = round(m.sqrt(digit))

if m.sqrt(digit) % 1 == 0:
    factors.append(root)

for x in range(1, root+1):
    factor = digit/x
    if factor % 1 == 0:
        if factor not in factors:
            factors.append(int(x))
            factors.append(int(factor))
print(f'The factors of {digit} are {factors}') 

if len(factors) == 2:
    primes = factors
    print(f'The prime numbers of {digit} are {primes}')
else:
    for factor in factors:
        if isprime(factor) == True:
            primes.append(factor)
    print(f'The prime numbers of {digit} are {primes}')