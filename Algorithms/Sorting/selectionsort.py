print("Enter array: ", end="")
arr = list(map(int, input().split()))

for i in range(len(arr)): 
	
	min_idx = i 
	for j in range(i+1, len(arr)): 
		if arr[min_idx] > arr[j]: 
			min_idx = j 
				 
	arr[i], arr[min_idx] = arr[min_idx], arr[i] 

print("Sorted array: ", end="") 
for i in arr: 
	print(i, end=" ")

print()