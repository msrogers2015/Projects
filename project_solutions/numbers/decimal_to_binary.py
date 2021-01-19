data = 0
decimal = []
binary = []


while data == 0:
	try:
		data = int(input("Input a whole number "))
		break
	except ValueError:
		print("Please enter a whole number")
			
def to_binary(data):
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
			

to_binary(data)
binary.reverse()
print(f'{data} in base 10 equals {"".join(binary)} in binary')

