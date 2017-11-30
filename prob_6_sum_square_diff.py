limit = 100
sumSquare, squareSum = 0, 0

for i in range(limit + 1):
    sumSquare += i ** 2
    squareSum += i

print(squareSum ** 2 - sumSquare)
