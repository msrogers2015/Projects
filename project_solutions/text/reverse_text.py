word = input('enter a single word or sentence:')
reverse_it = []


for w in word:
    reverse_it.append(w)

reverse_it.reverse()

print(''.join(reverse_it))