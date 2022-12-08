"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def Prime(n):
    # iterate through the length of n //2 + 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 0
    return 1


# taking input the value of n
N = int(input("Enter the value of N:"))
i = 2
prime_numbers = []
while 1:
    if Prime(i):
        prime_numbers.append(i)
        if len(prime_numbers) == N:
            break
    i += 1

# printing the numbers
print("First " + str(N) + " Prime numbers are:", end="")
print(*lst)
