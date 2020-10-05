N = int(input("Enter ay number : "))

f = 1
for i in range(1, N + 1):
    f *= i

print(f"Factorial of {N} is {f}.")
