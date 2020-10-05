STR = input("Enter any string : ")
char = input("Enter the character to be searched and counted : ")

count = 0
if char in STR:
    for letter in STR:
        if letter == char:
            count += 1
    print(f"Number of letter '{char}' present in string '{STR}' is {count}.")
else:
    print(f"{char} is not present in {STR}")
