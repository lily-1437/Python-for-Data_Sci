# Number Analysis Program

n = int(input("Enter a positive integer n: "))

if n <= 0:
    print("Invalid input")
else:
    even_sum = 0       
    odd_count = 0       
    div_3_5_sum = 0     
    total = 0           

    for i in range(1, n + 1):
        total += i

        if i % 2 == 0:
            even_sum += i
        else:
            odd_count += 1

        if i % 3 == 0 and i % 5 == 0:
            div_3_5_sum += i

    average = total / n

    print("Sum of even numbers:", even_sum)
    print("Count of odd numbers:", odd_count)
    print("Sum of numbers divisible by both 3 and 5:", div_3_5_sum)
    print("Average of integers from 1 to", n, ":", average)