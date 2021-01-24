happy_numbers = 0
def happy(number):
    starting = number
    maths = []
    sums = 0
    for x in range(100):
        for n in number:
            maths.append(int(n)**2)

        for m in maths:
            sums += m

        if sums == 1:
            return True
            break
        if sums != 1:
            number = str(sums)
            sums = 0
            maths = []


while happy_numbers < 8:
    for number in range(100):
        if happy(str(number)) is True:
            print(f'{number} is a happy number')
            happy_numbers += 1
        if happy_numbers == 8:
            break