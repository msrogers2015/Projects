cost = 0.00
payment = 0.00
change = 0.00

change_values = [['twenties', 20],['tens', 10],['fives', 5],
    ['ones', 1],['quarters', 0.25],['dimes', 0.10],['nickles', 0.05],['pennies', 0.01]]


try:
    cost = round(float(input('Enter the cost of the product:')), 2)
except ValueError:
    print('Please enter a numeric value')

try:
    payment = round(float(input('Enter the payment for the product:')), 2)
except ValueError:
    print('Please enter a numeric value')

if payment < cost:
    try:
        payment = round(float(input('Please enter a higher payment amount:')), 2)
    except ValueError:
        print('Please enter a numeric value')


if payment > cost:
    change = round(payment - cost, 2)


for item in change_values:
    if change // item[1] > 0:
        current = item[1]
        item[1] = int(change//item[1])
        change = round((change % current),2)
    else:
        item[1] = 0


print(f''' Your change is {change_values[0][1]} twenty bills
    {change_values[1][1]} ten bills,
    {change_values[2][1]} five bills,
    {change_values[3][1]} single bills,
    {change_values[4][1]} quarters,
    {change_values[5][1]} dimes,
    {change_values[6][1]} nickles and 
    {change_values[7][1]} pennies''')
