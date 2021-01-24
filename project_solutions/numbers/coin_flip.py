import random as r
coin = ['heads','tails']
heads = 0
tails = 0

flips = int(input('How many times do you want to flip the coin?'))

for x in range(flips):
    side = r.choice(coin)
    print(f'The coin landed on {side}')
    if side == 'heads':
        heads += 1
    if side == 'tails':
        tails += 1

print(f'The coin landed on heads {heads} times and on tails {tails} time')