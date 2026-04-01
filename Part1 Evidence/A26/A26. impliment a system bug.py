numbers = [10, 20, 30]

for i in range(0, len(numbers) + 1):  # BUG: +1 causes overflow
    print(numbers[i])