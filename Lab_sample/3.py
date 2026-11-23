numbers = [12, 7, -4, 12, 18, 5, -3, 8, 18]

non_negative = []
unique_non_negative = []
even_sum = 0
negative_count = 0

for num in numbers:
    if num < 0:
        negative_count += 1
        continue

    non_negative.append(num)

    if num not in unique_non_negative:
        unique_non_negative.append(num)

    if num % 2 == 0:
        even_sum += num

sliced = numbers[1:8:2]

print("Original list:", numbers)
print("Non-negative list:", non_negative)
print("Unique non-negative list:", unique_non_negative)
print("Sum of even non-negative numbers:", even_sum)
print("Count of negative numbers:", negative_count)
print("Elements at indices 1, 3, 5, 7:", sliced)