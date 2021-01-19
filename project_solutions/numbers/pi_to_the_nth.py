import math as m
import decimal as d


precision =0


while precision == 0 or precision > 27:
	try:
		precision = int(input("Select how many numbers you want to display of pie"))
	except ValueError:
		precision = int(input("Select how many numbers you want to display of pie"))
	
	
pi = round((d.Decimal(m.pi)),precision)

print(pi)
