power = 1000

powered_num = 2**power
digit_list = list(str(powered_num))

accumulator = 0

for digit in digit_list:
    accumulator += int(digit)

print(accumulator)
