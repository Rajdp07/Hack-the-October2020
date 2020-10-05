N = int(input("Enter ay number : "))

f = 1
i = 1
running = True
while running:
    
    if i == N:
        f *= i
        running = False
    else:
        f *= i
        i += 1

print(f"Factorial of {N} is {f}.")


