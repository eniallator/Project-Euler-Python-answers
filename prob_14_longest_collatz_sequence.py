def collatz(num):
    if num <= 1:
        return 1
    elif num % 2:
        return 1 + collatz(3 * num + 1)
    return 1 + collatz(num / 2)

longest_num = 0
longest_length = 0

for i in range(1, 1000001):
    curr_length = collatz(i)
    if curr_length > longest_length:
        longest_length = curr_length
        longest_num = i

print(longest_num, longest_length)
