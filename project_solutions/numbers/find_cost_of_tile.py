try:
    length = int(input('Enter the length of the room:'))
except ValueError:
    print('Please enter a whole number')
    length = int(input('Enter the length of the room:'))


try:
    width = int(input('Enter the width of the room:'))
except ValueError:
    print('Please enter a whole number')
    width = int(input('Enter the width of the room:'))


try:
    cost = float(input('Please enter cost of tiles D.CC format:'))
except ValueError:
    print('Please enter a number with two decimal points')
    cost = float(input('Please enter cost of tiles D.CC format:'))
    

total = round((width * length * cost),2)

print(f'The total cost for the room is {total}')