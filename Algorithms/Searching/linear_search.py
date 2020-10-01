def linear_search(ar, key):
    for i in range(len(ar)):
        if ar[i] == key:
            return i
    return -1



if __name__ == "__main__":
    ar = list(map(int, input().split()))
    key = int(input())
    pos = linear_search(ar, key)
    if pos >= 0:
        print('Key Present at position {}!!'.format(pos+1))
    else:
        print('Key Not Present!!!')