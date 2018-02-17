index = 2
a = 1
b = 1
while len(str(b)) < 1000:
    index += 1
    a, b = b, a + b
print(index)
