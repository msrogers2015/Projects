start = 0
sequence_length = 0
fibonacci = [0]

while True:
    try:
        start = int(input('Pick a starting number:'))
    except ValueError:
        print('Please enter a numeric value.')
    
    if start != None:
        try:
            sequence_length = int(input('Please select a sequence length:'))
        except ValueError:
            print('Please enter a numeric value.')
        
    for x in range(sequence_length):
        if x == 0:
            fibonacci.append(start)
        else:
            first = fibonacci[-1]
            second = fibonacci[-2]
            new = first + second
            fibonacci.append(new)

    print(fibonacci)
    break