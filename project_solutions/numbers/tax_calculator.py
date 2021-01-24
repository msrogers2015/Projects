cost = float(input('Enter total cost of transaction:'))
tax = float(input('Enter the tax percentage for your state or country(P.xx format):'))


cost = round(cost, 2)
tax = 1+ ((round(tax,2))/100)

total = round((cost * tax), 2)

print(f'Total for this purchase is {total}')