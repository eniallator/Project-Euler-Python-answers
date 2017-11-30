a, b = 0, 1
even_nums = 0

while b <= 4*10**6:
    # print b
    a,b = b,a+b
    even_nums += b if not b%2 else 0

print 'Even numbers: ' + str(even_nums)
