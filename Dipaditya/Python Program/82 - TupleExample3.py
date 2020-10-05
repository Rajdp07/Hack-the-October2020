my_tuple = (4, 2, 3, [6, 5])

my_tuple[3][0] = 9  
print(my_tuple)

my_tuple = ('p','r','o','g','r','a','m','s')

print(my_tuple)

print((1, 2, 3) + (4, 5, 6))

print(("Repeat",) * 3)



my_tuple = ('p','r','o','g','r','a','m','s')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple

# NameError: name 'my_tuple' is not defined
print(my_tuple)