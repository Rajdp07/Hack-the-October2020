def insertionsort(ar):
    for i in range(1, len(ar)):
        t = ar[i]
        j=i-1
        while j >=0 and ar[j] > t:
            ar[j+1] = ar[j]
            j-=1
        ar[j+1] = t

if __name__ == "__main__":
    ar = list(map(int, input().split()))
    insertionsort(ar)
    print('Sorted Array :- \n')
    print(ar)