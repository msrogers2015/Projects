import math as m

def is_prime(n):
    root = m.ceil(m.sqrt(n))
    for i in range(2,root+1):
        if n % i == 0:
            return False
    return True

running = True
starting = 3
while running:
    is_prime(starting)
    if is_prime(starting) is True:
        cont = input(f'{starting} is prime. Do you want to continue?')
        
        if cont.lower() == "y":
            starting += 1
            continue
            
        elif cont.lower() == "n":
            running = False
    else:
        starting += 1
        continue
    



'''
for i in range(2,100):
    if is_prime(i):
        print(f'{i} is a prime number')
        cont = input('Do you want to find the next prime number?')
'''
