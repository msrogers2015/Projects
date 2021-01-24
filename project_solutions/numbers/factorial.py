factorial = int(input('Please enter a positive integer:'))

output = factorial

if factorial == 0:
    output = 1
else:
    for x in range(1, factorial):
        output *= x

print(output)
