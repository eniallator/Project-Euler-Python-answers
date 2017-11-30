digits = 8

largest = 0

startingNum = 10**digits - 1
a,b = startingNum, startingNum

while b > 1:
    prod = a*b

    if str(prod)[::-1] == str(prod):
        if prod > largest:
            print a, b, prod
        largest = prod if prod > largest else largest

    a -= 1

    if a < 1 or prod < largest:
        b -= 1
        a = b
        if a*b < largest:
            break

print largest

"""7 digits output:

999001 9999999 9990009000999
5866663 9999995 58666600666685
6088742 9999993 60887377378806
8237042 9999984 82370288207328
8276488 9999981 82764722746728
9467731 9999979 94677111177649
9634317 9999957 96342755724369
9828181 9999869 98280522508289
9950541 9999539 99500822800599
9993367 9999297 99926644662999
9997647 9998017 99956644665999
99956644665999
[Finished in 246.3s]"""
