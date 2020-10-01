def bubblesort(ar):
    for i in range(len(ar)):
        for j in range(len(ar)-i-1):
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
        

if __name__ == "__main__":
    ar = list(map(int, input().split()))
    bubblesort(ar)
    print('Sorted Array :- \n')
    print(ar)