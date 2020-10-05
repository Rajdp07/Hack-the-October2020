year = int(input("Enter Any Year : "))

if year%4 == 0 and year%100 != 0:
    print(f"{year} is a leap year.")
elif year%400 == 0:
    print(f"{year} is a century leap year.")
else:
    print(f"{year} is not a leap year.")
