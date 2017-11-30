digits = 8
largest = 0
limit = 10**digits - 1

for a in range(limit, 0, -1):
    if a * limit < largest:
        break

    for b in range(limit, a - 1, -1):
        prod = a * b
        if str(prod) == str(prod)[::-1] and prod > largest:
            largest = prod
            print(a, b, prod)

        if prod < largest:
            break

print(largest)
