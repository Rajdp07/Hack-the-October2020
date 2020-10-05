N = int(input("Enter a natural number : "))

i = 1
running = True
while running:

    if i == 10:
        print(f"{N} x {i} = {N * i}")
        running = False
    else:
        print(f"{N} x {i} = {N * i}")
        i += 1

