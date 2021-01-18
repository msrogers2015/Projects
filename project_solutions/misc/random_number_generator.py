import random as r
lower = 0
upper = 0
digit = 0

while True:
    try:
        lower = int(input('Plase select a lower limit:'))
    except ValueError:
        print('Please input a numerical value')

    try:
        upper = int(input('Please select a upper limit:'))
    except ValueError:
        print('Please input a numerical value')


    if upper < lower:
        try:
            upper = int(input('Please select a higher upper limit:'))
        except ValueError:
            print('Please input a numerical value')
    
    if lower < upper:
        digit = r.randint(lower, upper)
        print(f'Your random number is {digit}')
        
    break