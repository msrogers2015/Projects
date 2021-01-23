pig = input('Please enter a word or sentence:')
output = []



latin = pig.split(' ')


for l in latin:
    p,l = l[0], l[1:]
    p = '-' +p + "ay"
    output.append(l+p)

print(' '.join(output))