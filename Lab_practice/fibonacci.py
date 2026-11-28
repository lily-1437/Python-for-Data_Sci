num = int(input("Enter a number: "))
a, b = 0, 1
product = 1
for i in range(num):
    print(a, end=' ')
    product *= a
    a, b = b, a + b
print("\nProduct of Fibonacci numbers:", product)