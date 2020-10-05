# mistake values
odd = [2, 4, 6, 8]
# change the 1st item
odd[0] = 1
# Output: [1, 4, 6, 8]
print(odd)
# change 2nd to 4th items
odd[1:4] = [3, 5, 7]
# Output: [1, 3, 5, 7]
print(odd)

odd.append(9)
# Output: [1, 3, 5, 7, 9]
print(odd)
odd.extend([11, 13])
# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)


odd = [1, 3, 5]
# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])
# Output: ["re", "re", "re"]
print(["re"] * 3)

odd = [1, 9]
odd.insert(1, 3)
# Output: [1, 3, 9]
print(odd)
odd[2:2] = [5, 7]
# Output: [1, 3, 5, 7, 9]
print(odd)

odd.append([1,3])
print(odd)