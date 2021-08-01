a = 'Python programming is very easy'
b = list(a)
c = set(b)
s = list(c)
counts = {letter:s.count(letter) for letter in s}
print(counts)