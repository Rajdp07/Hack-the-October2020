def binary_search(ar, key):
    low, high = 0, len(ar)-1
    while low <= high:
        mid = (low + (high-low))//2
        if ar[mid] == key:
            return mid
        elif ar[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    if low > high:
        return -1



if __name__ == "__main__":
    ar = list(map(int, input().split()))
    ar.sort()
    print('Sorted Array :- ', ar)
    key = int(input())
    pos = binary_search(ar, key)
    if pos >= 0:
        print('Key Present at position {}!!'.format(pos+1))
    else:
        print('Key Not Present!!!')