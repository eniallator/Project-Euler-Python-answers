limit = 1000
output = 0

for i in range(limit):
    output += i if not (i%3 and i%5) else 0

print(output)
