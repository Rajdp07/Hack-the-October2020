file_name = input("Enter file name: ")

fh = open(file_name)
print(type(fh))
count = 0
lst = list
for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.rstrip().split()
        count += 1
        print(words[1])

print("There were", count, "lines in the file with From as the first word\n\n")


with open("test.txt", "r") as f:
    count = 0
    lst = list
    for line in f:
        if line.startswith("From") and not line.startswith("From:"):
            words = line.rstrip().split()
            count += 1
            print(words[1])
