my_tuple = ("p", "e", "r", "m", "i", "t")

print(my_tuple[0])
print(my_tuple[5])

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_tuple[0][3])
print(n_tuple[1][1])

my_tuple = ("p", "e", "r", "m", "i", "t")

print(my_tuple[-1])

# Output: 'p'
print(my_tuple[-6])

my_tuple = ("p", "r", "o", "g", "r", "a", "m", "s")

print(my_tuple[1:4])

print(*my_tuple[:-7])

print(my_tuple[7:])

print(my_tuple[:])
