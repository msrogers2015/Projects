data = 0
data_type = 0
decimal = []
binary = []


while data == 0:
	try:
		data = int(input("Input a whole number "))
		break
	except ValueError:
		print("Please enter a whole number")

while data_type == 0:
	try:
		data_type = int(input('Please select a format(1 to conver to binary and  2 to convert to decimal):'))
	except ValueError:
		print('Please enter a valid input')
			
def to_binary(data):
	number = data
	while data >= 0:
		if data % 2 == 0 and data != 0:
			binary.append("0")
			data = data//2
		elif data % 2 == 1 and data != 0:
			binary.append("1")
			data = data//2
		else:
			binary.append("0")
			break
	binary.reverse()
	print(f'{number} in base 10 equals {"".join(binary)} in binary')			


def to_decimal(data):
	tracking = 0
	iteration = 0
	entry = data
	data = str(data)
	for i in data:
		decimal.append(i)
	decimal.reverse()
	for i in decimal:
		if int(i) == 1:
			i = int(i)*(2**iteration)
			tracking += i
		iteration += 1
	print(f'{entry} in decimal is {tracking}')
			

if data_type == 1:
	to_binary(data)

if data_type == 2:
	to_decimal(data)

