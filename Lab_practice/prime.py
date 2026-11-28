num = int(input("Enter an integer: "))
n = 2
for i in range(2, int(num**0.5)+1):
    if (num%i) == 0:
        print(num, "is not a prime number")
        flag_prime = False
        break
n +=1
# sum of prime numbers