n = int(input("Enter a positive integer: "))
sum = 0
product = 1
for i in range(1, n + 1):
    product *=i
    sum += i
print("The sum of the first", n, "positive integers is:", sum)
print("The product of the first", n, "positive integers is:", product)