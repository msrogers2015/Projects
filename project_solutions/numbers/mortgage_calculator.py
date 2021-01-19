loan = 0

while loan == 0:
	try:
		loan = p = float(input("Please enter loan amount:"))
	except ValueError:
		print("Please enter a integer")

try:
	interest = float(input("Please enter loan interest rate:"))
except ValueError:
	print("Please enter a integer")
	
	
try:
	life = int(input("Please enter loan length in years"))
except ValueError:
	life = int(input("Please enter loan length in years"))
	
	
r = interest/100/12
n = life*12

top = r * ((1+r)**n)
bottom = ((1+r)**n)-1

M = round((p*(top/bottom)),2)

print(f'Your monthly payment is {M}')
