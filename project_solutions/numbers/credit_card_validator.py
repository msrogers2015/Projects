cc = input('Please enter a 16 digit number(you can use spaces to create 4 groups of 4)')
card_drop = []

# remove all white spaces
cc = cc.replace(' ','')
print(cc)
# Convert string into a list
for c in cc:
    card_drop.append(int(c))

#Drop the last number and save in its own variable for later
last_digit = card_drop[15]
card_drop = card_drop[:-1]
print(f'Card has been parsed to {card_drop}')

# Reverse the number
card_drop.reverse()
print(f'Card has been reversed to {card_drop}')

# Multiple odd numbers by 2
l = 1
for c in card_drop:
    if l % 2 != 0:
        card_drop[(l-1)] = c*2
        l += 1
    else:
        l += 1

print(f'Numbers have been multipled {card_drop}')


# Subtract 9 from values greater than 9
l=0
for c in card_drop:
    if c > 9:
        card_drop[l] = c-9
    l += 1
print(f'Brought back to single digits {card_drop}')


#Add all values
l = 0
for c in card_drop:
    l += c
print(f'sum is {l}')


# Mod 10
valid = None
if l % 10 == last_digit:
    valid = True
else:
    valid = False



if valid is True:
    print(f'{cc} is a valid credit card number')
else:
    print(f'{cc} is not a valid credit card number')
